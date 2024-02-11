import pygame
from tiles import Tile
from settings import tile_size, screen_width, screen_height, levels
from player import Player

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
        self.tiles = pygame.sprite.Group()
        self.coins = pygame.sprite.Group()
        self.player = pygame.sprite.GroupSingle()

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



    def scroll_x(self):
        player = self.player.sprite
        player_x = player.rect.centerx
        direction_x = player.direction.x
        if player_x < screen_width / 4 and direction_x < 0:
            self.world_shift = 8
            player.speed = 0
        elif player_x > screen_width * (3 / 4) and direction_x > 0:
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
    #Level state Controller
    def levelstate(self):
        #check Death State
        self.isdead()
        #Escape Level
        keys = pygame.key.get_pressed()
        if keys[pygame.K_ESCAPE]:
            self.create_menu(self.currentlevel,0)
        player = self.player.sprite
        if player.status == 'dead':
            print("you are dead")
            self.create_menu(self.currentlevel,0)
            pass
        if len(self.coins) == 0:
            #code to go to next level
            self.create_menu(self.currentlevel,self.new_max_level)
            pass
        else:
            #print("Coins to collect: " + str(len(self.coins)))
            pass
    
    #Checks if player is below the screen
    def isdead(self):
        player = self.player.sprite
        player_y = player.rect.centery
        if player_y > screen_height:
            player.status = 'dead'

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

    def run(self):
        #level tiles
        self.tiles.update(self.world_shift)
        self.tiles.draw(self.display_surface)
        self.coins.update(self.world_shift)
        self.coins.draw(self.display_surface)
        self.scroll_x()

        #player
        self.player.update()
        self.coin_collection()
        self.horizontal_movement_collision()
        self.vertical_movement_collision()
        self.player.draw(self.display_surface)

        #level state
        self.levelstate()
