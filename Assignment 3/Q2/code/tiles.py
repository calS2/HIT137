import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size):
        super().__init__()
        self.image = pygame.image.load("Assignment 3\Q2\graphics\Tile_36.png")
        #self.image.fill('grey')
        #self.image = pygame.Surface((size,size))
        self.rect = self.image.get_rect(topleft = pos)

    def update(self,x_shift):
        self.rect.x += x_shift