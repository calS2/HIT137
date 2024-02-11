import pygame, sys
from settings import *
from level import Level
from menu import Menu

class Game:
    def __init__(self):
        self.max_level = 0
        self.menu = Menu(2,self.max_level,screen,self.create_level)
        self.status = 'menu'
        self.level = Level(0,screen)
    
    def create_level(self, current_level):
        self.level = Level(current_level, screen)
        self.status = 'level'


    def run(self):
        if self.status == 'menu':
            self.menu.run()
        else:
            self.level.run()


#Pygame Setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

#level selection
currentlevel = 0
if currentlevel == 1:
    level_map = level_map1
elif currentlevel == 2:
    level_map = level_map2
elif currentlevel == 3:
    level_map = level_map1

#level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    game.run()
    #level.run()

    pygame.display.update()
    clock.tick(60)