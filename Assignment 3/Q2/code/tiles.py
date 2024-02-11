import pygame

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size,kind):
        super().__init__()
        if kind == "wall":
            self.image = pygame.image.load("Assignment 3\Q2\graphics\Tile_36.png").convert_alpha()
            self.rect = self.image.get_rect(topleft = pos)
            self.collectable = False
        elif kind == "coin":
            self.image = pygame.image.load('Assignment 3\Q2\graphics\Coin32.png').convert_alpha()
            self.rect = self.image.get_rect(center = (pos[0]+32,pos[1]+32))
            self.collectable = True
        #self.image.fill('grey')
        #self.image = pygame.Surface((size,size))
        

    def update(self,x_shift):
        self.rect.x += x_shift