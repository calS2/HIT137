import pygame, sys
from pygame.locals import *
from settings import *
from level import Level

#Pygame Setup
white = (255,255,255)
black = (0,0,0)
red = (255,0,0)
screen = pygame.display.set_mode(resolution)
clock = pygame.time.Clock()
level = Level(level_map,screen)

while True:
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    screen.fill(white)
    level.run()

    pygame.display.flip()
    clock.tick(60)