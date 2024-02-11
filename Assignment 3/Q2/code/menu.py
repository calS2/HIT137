import pygame
from settings import levels

class Button(pygame.sprite.Sprite):
    def __init__(self,pos,status):
        super().__init__()

        self.image = pygame.Surface((100,80))
        if status == 'available':
            self.image.fill('green')
        else:
            self.image.fill('grey')
        self.rect = self.image.get_rect(center = pos)

class Menu:
    def __init__(self, start_level, max_level,surface,create_level):
        #setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level
        self.create_level = create_level
        #sprites
        self.setup_buttons()

    def setup_buttons(self):
        self.buttons = pygame.sprite.Group()
        for index, data in enumerate(levels.values()):
            if index <= self.max_level:
                button_sprite = Button(data['pos'],'available')
            else:
                button_sprite = Button(data['pos'],'locked')
            self.buttons.add(button_sprite)            

    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            print("Space")
            self.create_level(self.current_level)
    def run(self):
        self.get_input()
        self.buttons.draw(self.display_surface)