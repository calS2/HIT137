import pygame, sys
from settings import *
from level import Level
from menu import Menu
from ui import UI
#MAIN Game Controller

class Game:
    def __init__(self):
        #Parameters
        self.max_level = 0
        self.menu = Menu(0,self.max_level,screen,self.create_level)
        self.status = 'menu'
        self.coins = 0



        #UI setup
        self.ui = UI(screen)


    #Method for entering Level
    def create_level(self, current_level):
        self.level = Level(self.max_level,screen,self.create_menu,self.coin_update,self.ui)
        self.status = 'level'


    #Method for exiting Level
    def create_menu(self, current_level,new_max_level):
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.menu = Menu(current_level,self.max_level,screen,self.create_level)
        self.status = 'menu'

    

    def coin_update(self, amount):
        self.coins += amount

    def run(self):
        if self.status == 'menu':
            self.menu.run()
        else:
            self.level.run()

            self.ui.show_coins(self.coins)


#Pygame Setup
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    game.run()

    pygame.display.update()
    clock.tick(60)