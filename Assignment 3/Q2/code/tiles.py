import pygame
from support import import_folder

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


class AnimatedTile(Tile):
	def __init__(self,size,x,y,path):
		super().__init__(size,x,y)
		self.frames = import_folder(path)
		self.frame_index = 0
		self.image = self.frames[self.frame_index]

	def animate(self):
		self.frame_index += 0.15
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]

	def update(self,shift):
		self.animate()
		self.rect.x += shift
