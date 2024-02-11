import pygame 
from support import import_folder
from random import randint

class Enemy(pygame.sprite.Sprite):
	def __init__(self,pos):
		super().__init__()
		print("Heya")
		self.frames = import_folder('graphics/enemy/run')
		print("Hello World")
		self.frame_index = 0
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(topleft = pos)
		self.speed = randint(3,5)

	def move(self):
		self.rect.x += self.speed

	def reverse_image(self):
		if self.speed > 0:
			self.image = pygame.transform.flip(self.image,True,False)

	def reverse(self):
		self.speed *= -1

	def animate(self):
		self.frame_index += 0.15
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]
		
	def update(self,shift):
		self.rect.x += shift
		self.animate()
		self.move()
		self.reverse_image()