import pygame
from settings import levels
#Button class for the progress indicators
class Button(pygame.sprite.Sprite):
    def __init__(self,pos,status):
        super().__init__()
        #Main Menu Indicates current progress through game
        self.image = pygame.Surface((100,80))
        if status == 'available':
            self.image.fill('green')
        else:
            self.image.fill('grey')
        self.rect = self.image.get_rect(center = pos)

#Could not Get working
#class Text():
#    def __init__(self,pos,level_text):
#        super().__init__()
#        #Main Menu Indicates current progress through game
#        self.font = pygame.font.SysFont('None', 40)
#        self.text_surface = self.font.render(str(level_text),False,'white')
#        self.rect = self.text_surface.get_rect()
        
#Menu Controller, Specifics what level should be loaded 
class Menu:
    def __init__(self, start_level, max_level,surface,create_level):
        #Setup
        self.display_surface = surface
        self.max_level = max_level
        self.current_level = start_level
        self.create_level = create_level
        #Generate buttons on menu load
        self.setup_buttons()

    #Generates buttons
    def setup_buttons(self):
        self.buttons = pygame.sprite.Group()
        #iterate over level data
        for index, data in enumerate(levels.values()):
            level_text = data['text']
            if index <= self.max_level:
                #Create image from position data in level values, change color based on level progress
                button_sprite = Button(data['pos'],'available')
                            #Could not get working
                            #text_sprite = Text(level_text,data['pos'])
            
            else:
                #Grey square to show locked level
                button_sprite = Button(data['pos'],'locked')
            self.buttons.add(button_sprite)            
        
    #Controls for Menu
    def get_input(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_SPACE]:
            self.create_level(self.current_level)
        font = pygame.font.SysFont(None, 24)
        img = font.render('Press Space to start level, defeat the enemies and collect the coins to advance', True, 'White')
        self.display_surface.blit(img, (20, 20))
        
    #Update cycle
    def run(self):
        self.get_input()
        self.buttons.draw(self.display_surface)