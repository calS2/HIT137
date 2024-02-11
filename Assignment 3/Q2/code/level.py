import pygame
from tiles import Tile
from settings import tile_size, screen_width, screen_height, levels
from player import Player
from enemy import Enemy

class Level:
    def __init__(self,currentlevel,surface,create_menu):
        self.score = 0
        # level setup
        self.display_surface = surface
        self.currentlevel = currentlevel
        level_data = levels[currentlevel]
        level_content = level_data['mapdata']
        self.setup_level(level_content)
        self.new_max_level = level_data['unlock']
        self.create_menu = create_menu
        self.world_shift = 0


    def setup_level(self,layout):
        #Containers
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()
        self.enemy = pygame.sprite.Group()
        self.bound = pygame.sprite.Group()

        for row_index,row in enumerate(layout):
            for col_index,cell in enumerate(row):
                x = col_index * tile_size
                y = row_index * tile_size
                if cell == "X":
                    tile = Tile((x,y),tile_size,"wall")
                    self.tiles.add(tile)
                if cell == "C":
                    tile = Tile((x,y),tile_size,"coin")
                    self.coins.add(tile)
                if cell == "P":
                    player_sprite = Player((x,y))
                    self.player.add(player_sprite)
                if cell == 'E':	
                    enemy_sprite = Enemy((x,y),"minion")
                    self.enemy.add(enemy_sprite)
                if cell == 'K':	
                    enemy_sprite = Enemy((x,y),"king")
                    self.enemy.add(enemy_sprite)
                if cell == 'B':
                    tile = Tile((x,y),tile_size,"bound")
                    self.bound.add(tile)

    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < screen_width * (1 / 3) and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width * (2 / 3) and direction_x > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def scroll_y(self):
        player = self.player.sprite
        player_y = player.rect.centery
        direction_y = player.direction.y
        if player_y < screen_height * (1 / 3) and direction_y < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_y > screen_width * (2 / 3) and direction_y > 0:
            self.world_shift = -8
            player.speed = 0
        else:
            self.world_shift = 0
            player.speed = 8

    def coin_collection(self):
        player = self.player.sprite
        for sprite in self.coins.sprites():
            if sprite.rect.colliderect(player.rect) and sprite.collectable==True:
               self.coins.remove(sprite)
               self.score += 1

    def enemy_collision_reverse(self):
        for enemy in self.enemy.sprites():
            if pygame.sprite.spritecollide(enemy,self.bound,False):
                enemy.reverse()

    def enemy_collisions(self):
        enemy_collisions = pygame.sprite.spritecollide(self.player.sprite,self.enemy,False)
        if enemy_collisions:
            for enemy in enemy_collisions:
                enemy_center = enemy.rect.centery
                enemy_top = enemy.rect.top
                player_bottom = self.player.sprite.rect.bottom
                if enemy_top < player_bottom < enemy_center and self.player.sprite.direction.y >= 0:
                    self.player.sprite.direction.y = -15
                    enemy.get_hurt()
                    if enemy.get_hurt() == 'rip':
                            self.enemy.remove(enemy)
                else:
                    player = self.player.sprite
                    player.get_damage()


    #Level state Controller
    def levelstate(self):
        #check Death State
        #Escape Level
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.create_menu(self.currentlevel,0)
        if keys[pygame.K_RETURN]:
            self.create_menu(self.currentlevel,self.new_max_level)  
        player = self.player.sprite
        if player.status == 'dead':
            print("you are dead")
            self.create_menu(self.currentlevel,0)       
        if len(self.coins) == 0 and len(self.enemy) == 0:
            self.create_menu(self.currentlevel,self.new_max_level)
        else:
            #print("Coins to collect: " + str(len(self.coins)))
            pass
    


    def horizontal_movement_collision(self):
        player = self.player.sprite
        player.rect.x += player.direction.x * player.speed

        for sprite in self.tiles.sprites():
            if sprite.rect.colliderect(player.rect):
                if player.direction.x < 0:
                    player.rect.left = sprite.rect.right
                    player.on_left = True
                elif player.direction.x > 0:
                    player.rect.right = sprite.rect.left
                    player.on_right = True

    def vertical_movement_collision(self):
        player = self.player.sprite
        player.apply_gravity()

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

        if player.on_ground and player.direction.y < 0 or player.direction.y > 1:
            player.on_ground = False
        if player.on_ceiling and player.direction.y > 0:
            player.on_ceiling = False


##  def hitboxes(self):
##          for enemy in self.enemy.sprites():
##              rect = enemy.rect
##              pygame.draw.rect(self.display_surface,'red',rect,0)
##          for bound in self.bound.sprites():
##              rect = bound.rect
##              pygame.draw.rect(self.display_surface,'blue',rect,0)



    def run(self):
        #level tiles
##        self.tiles.update_x(self.world_shift)
##        self.tiles.update_y(self.world_shift)
##        self.coins.update_x(self.world_shift)
##        self.coins.update_y(self.world_shift)
##        self.bound.update_x(self.world_shift)
##        self.bound.update_y(self.world_shift)
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        self.bound.update(self.world_shift)
        self.bound.update(self.world_shift)
        self.bound.draw(self.display_surface)
        self.scroll_x()
#        self.scroll_y()

        #UI
        #self.display_surface.blit(self.text_surf,self.text_rect)

        #Hitboxes (readability)
        #self.hitboxes()

        #player
        self.player.update()
        self.coin_collection()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

		# enemy 
##        self.enemy.update_x(self.world_shift)
##        self.enemy.update_y(self.world_shift)
        self.enemy.update(self.world_shift)
        self.enemy_collision_reverse()
        self.enemy.draw(self.display_surface)
        self.enemy_collisions()

        #level state
        self.levelstate()
