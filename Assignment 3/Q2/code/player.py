import pygame
from support import import_folder
from settings import screen_height

#Player Class
class Player(pygame.sprite.Sprite):
    def __init__(self,pos,health_update):
        super().__init__()
        #General Parameters/Setup
        self.import_character_assets()
        self.frame_index = 0
        self.animation_speed = 0.15
        self.image = self.animations['idle'][self.frame_index]
        self.rect = self.image.get_rect(topleft = pos, size = (64,64))

        #Player movement
        self.direction = pygame.math.Vector2(0,0)
        self.speed = 8
        self.gravity = 0.8
        self.jump_speed = -16

        #Player status, used for collision check and directions
        self.status = 'idle'
        self.facing_right = True
        self.on_ground = False
        self.on_ceiling = False
        self.on_left = False
        self.on_right = False

        #Health Parameters, Used to update UI and Reset Gamestates
        self.health_update = health_update
        self.max_health = 100
        self.cur_health = 100
        self.invincible = False
        self.invincibility_duration = 300
        self.hurt_time = 0

    #Import Assets
    def import_character_assets(self):
        character_path = "graphics/character2/"
        self.animations = {'idle':[],'run':[],'jump':[]}
        #Create an array of animations based of files in folder
        for animation in self.animations.keys():
            full_path = character_path + animation
            self.animations[animation] = import_folder(full_path)
    #Determins the animation state of the player character
    def animate(self):
        if self.status == 'dead':
            animation = self.animations['idle']
        else:
            animation = self.animations[self.status]

        #loop over frame index for animations
        self.frame_index += self.animation_speed
        #Reset to start of animation
        if self.frame_index >= len(animation):
            self.frame_index = 0
        image = animation[int(self.frame_index)]
        #Direction Flipper
        if self.facing_right:
            self.image = image
        else:
            flipped_image = pygame.transform.flip(image, True, False)
            self.image = flipped_image

        #Hit Box Parameters
        if self.on_ground:
            self.rect = self.image.get_rect(midbottom = self.rect.midbottom)
        elif self.on_ceiling:
            self.rect = self.image.get_rect(midtop = self.rect.midtop)
        else:
            self.rect = self.image.get_rect(center = self.rect.center)
    #Controllers for character
    def get_input(self):
        keys = pygame.key.get_pressed()
        #Right
        if keys[pygame.K_RIGHT]:
            self.direction.x = 1
            self.facing_right = True
        #Left
        elif keys[pygame.K_LEFT]:
            self.direction.x = -1
            self.facing_right = False
        else:
            self.direction.x = 0
        #Jump
        if keys[pygame.K_SPACE] and self.on_ground:
            self.jump()
    #Gravity Modifier application
    def apply_gravity(self):
        self.direction.y += self.gravity
        self.rect.y += self.direction.y
    #Jump function
    def jump(self):
        self.direction.y = self.jump_speed
    #On damage update player statue and invicibility
    def get_damage(self):
        if not self.invincible:
            self.health_update(-50)
            self.cur_health -= 50
            self.invincible = True
            self.hurt_time = pygame.time.get_ticks()
    #I Frames
    def invincibility_timer(self):
        if self.invincible:
            current_time = pygame.time.get_ticks()
            if current_time - self.hurt_time >= self.invincibility_duration:
                self.invincible = False
    #Status controller
    def get_status(self):
        #Death
        if self.rect.centery > screen_height or self.cur_health < 0:
            self.status = 'dead'
        #Jumping
        elif self.direction.y < 0:
            self.status = 'jump'
        #Idles
        elif self.direction.y > 1:
            self.status = 'idle'
        else:
            #Run
            if self.direction.x != 0:
                self.status = 'run'
            else:
                self.status = 'idle'
    #update
    def update(self):
        self.get_input()
        self.invincibility_timer()
        self.get_status()
        self.animate()

