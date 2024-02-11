import pygame
from tiles import Tile
from settings import tile_size, screen_width, screen_height, levels
from player import Player
from enemy import Enemy
#Level constructor
class Level:    
    def __init__(self,currentlevel,surface,create_menu, change_coins,ui):
        self.score = 0
        # level setup
        self.ui = ui
        self.display_surface = surface
        self.currentlevel = currentlevel
        level_data = levels[currentlevel]
        level_content = level_data['mapdata']
        self.setup_level(level_content)
        self.new_max_level = level_data['unlock']
        self.create_menu = create_menu
        self.world_shift = 0
        #ui setup
        self.change_coins = change_coins
        self.collected_coins = 0
        self.curr_health = 100
        self.max_health = 100

    def setup_level(self,layout):
        #Containers
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy = pygame.sprite.Group()
        self.bound = pygame.sprite.Group()
        #Iterate over level data and generate level based on values
        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                #Walls
                if cell == "X":
                    tile = Tile((x,y),tile_size,"wall")
                    self.tiles.add(tile)
                #Coins
                if cell == "C":
                    tile = Tile((x,y),tile_size,"coin")
                    self.coins.add(tile)
                #Player
                if cell == "P":
                    player_sprite = Player((x,y),self.health_update)
                    self.player.add(player_sprite)
                #Minions(Enemy)
                if cell == 'E':	
                    enemy_sprite = Enemy((x,y),"minion")
                    self.enemy.add(enemy_sprite)
                #King(Bosses)
                if cell == 'K':	
                    enemy_sprite = Enemy((x,y),"king")
                    self.enemy.add(enemy_sprite)
                #Boundary, Invisible for enemy collisions
                if cell == 'B':
                    tile = Tile((x,y),tile_size,"bound")
                    self.bound.add(tile)
    #Screen scroller when player reaches sides of screen
    #Stops player moving and shifts entire level instead
    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        #Left
        if player_x < screen_width * (1 / 3) and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        #Right
        elif player_x > screen_width * (2 / 3) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

            
    #Coin collision detection and update
    def coin_collection(self):
        player = self.player.sprite
        for sprite in self.coins.sprites():
            if sprite.rect.colliderect(player.rect) and sprite.collectable==True:
               self.coins.remove(sprite)
               self.score += 1
               self.collected_coins +=1
               self.change_coins(1)

    #Enemy Collisions detection with boundary
    def enemy_collision_reverse(self):
        for enemy in self.enemy.sprites():
            #If touching boundary reverse x
            if pygame.sprite.spritecollide(enemy,self.bound,False):
                enemy.reverse()

    #Health Update for UI
    def health_update(self, damage):
        self.curr_health += damage
    
    #Collision detection with enemys, includes killing enemies from above health update
    def enemy_collisions(self):
        enemy_collisions = pygame.sprite.spritecollide(self.player.sprite,self.enemy,False)
        if enemy_collisions:
            #Check touching
            for enemy in enemy_collisions:
                enemy_center = enemy.rect.centery
                enemy_top = enemy.rect.top
                player_bottom = self.player.sprite.rect.bottom
                #If player is landing on their head, deal damage, if fatal kill
                if enemy_top < player_bottom < enemy_center and self.player.sprite.direction.y >= 0:
                    #Mario bounce
                    self.player.sprite.direction.y = -15
                    enemy.get_hurt()
                    if enemy.get_hurt() == 'rip':
                            self.enemy.remove(enemy)
                #If player not landing on head, player takes damage
                else:
                    player = self.player.sprite
                    player.get_damage()

    #Level state Controller
    def levelstate(self):
        #Escape Level
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.create_menu(self.currentlevel,0)
        #Skip Level
        if keys[pygame.K_RETURN]:
            self.create_menu(self.currentlevel,self.new_max_level)  
        player = self.player.sprite
        #Reset Level if player died
        if player.status == 'dead':
            print("you are dead")
            self.change_coins(-self.collected_coins)
            self.create_menu(self.currentlevel,0)       
        #Final boss level logic
        if len(self.coins) == 0 and len(self.enemy) == 0:
            self.create_menu(self.currentlevel,self.new_max_level)
        else:
            pass
    

    #Boundary Collision for walls(Horizontal)
    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed
        #If player is touching a wall find which side of the wall they should stay on and teleport them there.
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True
    #Boundary Collision for walls(Vertical), also gravity application
    def vertical_movement_collision(self):
        player = self.player.sprite
        #Gravity application
        player.apply_gravity()
        #If player is touching a wall find which side of the wall they should stay on and teleport them there.
        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.y > 0:
                    player.rect.bottom = sprite.rect.top
                    player.direction.y = 0
                    player.on_ground = True
                elif player.direction.y < 0:
                    player.rect.top = sprite.rect.bottom
                    player.direction.y = 0
                    player.on_ground = False
        #Ceiling
        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False
    #Update
    def run(self):
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        self.bound.update(self.world_shift)
        self.bound.draw(self.display_surface)
        self.ui.show_health(self.curr_health,self.max_health)
        self.scroll_x()



        #player
        self.player.update()
        self.coin_collection()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

		# enemy 
        self.enemy.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemy.draw(self.display_surface)
        self.enemy_collisions()
        #level state
        self.levelstate()


    #Experimentation with y axis scrolling (unused)
    #def scroll_y(self):
    #    player = self.player.sprite
    #    player_y = player.rect.centery
    #    direction_y = player.direction.y
    #    if player_y < screen_height * (1 / 3) and direction_y < 0:
    #        self.world_shift = 8
    #        player.speed = 0
    #    elif player_y > screen_width * (2 / 3) and direction_y > 0:
    #        self.world_shift = -8
    #        player.speed = 0
    #    else:
    #        self.world_shift = 0
    #        player.speed = 8