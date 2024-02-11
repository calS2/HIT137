import pygame 
from support import import_folder
from random import randint
#Enemy Constructor, Generates either a boss or minions when specified.
class Enemy(pygame.sprite.Sprite):
	def __init__(self,pos,school):
		super().__init__()
		#General Enemy Params
		self.frames = import_folder('graphics/'+school+'/run')
		self.frame_index = 0
		self.image = self.frames[self.frame_index]
		self.rect = self.image.get_rect(center = (pos[0]+10,pos[1]+10))
		        
        #Enemy specific Stats
		if school == 'minion':
			self.monster_health = 1
			self.speed = randint(3,5)
		elif school == 'king':
			self.monster_health = 3
			self.speed = 10

		#Invuln Timer
		self.invincible = False
		self.invincibility_duration = 300
		self.hurt_time = 0
	#Movement
	def move(self):
		self.rect.x += self.speed
	#Flip image based on direction
	def reverse_image(self):
		if self.speed > 0:
			self.image = pygame.transform.flip(self.image,True,False)
	
	#Reverse direction, called when touching boundary
	def reverse(self):
		self.speed *= -1
	#Frame animations
	def animate(self):
		self.frame_index += 0.15
		if self.frame_index >= len(self.frames):
			self.frame_index = 0
		self.image = self.frames[int(self.frame_index)]
	#Health calculations on damage
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
	#Invuln timer
	def invincibility_timer(self):
		if self.invincible:
			current_time = pygame.time.get_ticks()
			if current_time - self.hurt_time >= self.invincibility_duration:
				self.invincible = False
	#Update loop
	def update(self,shift):
		self.rect.x += shift
		self.animate()
		self.move()
		self.reverse_image()
		self.invincibility_timer()