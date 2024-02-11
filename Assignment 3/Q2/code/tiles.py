import pygame
from support import import_folder

class Tile(pygame.sprite.Sprite):
    def __init__(self,pos,size,kind):
        super().__init__()
        if kind == "wall":
            self.image = pygame.image.load('graphics/Tile_36.png').convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.collectable = False
        elif kind == "coin":
            self.image = pygame.image.load('graphics/ui/Coin32.png').convert_alpha()
            self.rect = self.image.get_rect(center = pos)
            self.collectable = True
        elif kind == "bound":
            self.image = pygame.Surface((64,64))
            self.rect = self.image.get_rect(center = pos)

    def update(self,x_shift):
        self.rect.x += x_shift
