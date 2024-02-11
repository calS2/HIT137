import pygame 
from support import import_folder
from random import randint

class Enemy(pygame.sprite.Sprite):
	def __init__(self,pos,school):
		super().__init__()
		self.frames = import_folder('graphics/'+school+'/run')
		self.frame_index = 0
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(center = (pos[0]+10,pos[1]+10))
		        
        #monster status
		if school == 'minion':
			self.monster_health = 1
			self.speed = randint(3,5)
		elif school == 'king':
			self.monster_health = 3
			self.speed = 10

		#health misc
		self.invincible = False
		self.invincibility_duration = 300
		self.hurt_time = 0

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
		
	def get_hurt(self):
		if not self.invincible:
			print(self.monster_health)
			self.monster_health -= 1
			self.invincible = True
			self.hurt_time = pygame.time.get_ticks()
			if self.monster_health <= 0:
				self.status = 'rip'
			else:
				self.status = 'alive'
		return self.status

	def invincibility_timer(self):
		if self.invincible:
			current_time = pygame.time.get_ticks()
			if current_time - self.hurt_time >= self.invincibility_duration:
				self.invincible = False
				
	def update(self,shift):
		self.rect.x += shift
		self.animate()
		self.move()
		self.reverse_image()
		self.invincibility_timer()