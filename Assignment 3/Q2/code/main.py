import pygame, sys
from settings import *
from level import Level

#Pygame Setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
currentlevel = 2
if currentlevel == 1:
    level_map = level_map1
elif currentlevel == 2:
    level_map = level_map2
if currentlevel == 3:
    level_map = level_map1
level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('white')
    level.run()

    pygame.display.flip()
    clock.tick(60)