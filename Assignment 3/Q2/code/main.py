import pygame, sys
from settings import *
from level import Level
from menu import Menu
from ui import UI
#Main Game Controller

class Game:
    def __init__(self):
        #Parameters
        self.max_level = 0
        self.menu = Menu(0,self.max_level,screen,self.create_level)
        self.status = 'menu'
        self.coins = 0
        #UI setup
        self.ui = UI(screen)

    #Passes values for the level generator into the level constructor
    def create_level(self, current_level):
        self.level = Level(self.max_level,screen,self.create_menu,self.coin_update,self.ui)
        self.status = 'level'

    #Method for exiting Level
    def create_menu(self, current_level,new_max_level):
        #checks if player beat level if not reload level
        if new_max_level > self.max_level:
            self.max_level = new_max_level
        self.menu = Menu(current_level,self.max_level,screen,self.create_level)
        self.status = 'menu'

    #Coin update is passed into the level as a function for UI update
    def coin_update(self, amount):
        self.coins += amount

    #Run Script 
    def run(self):
        #swapping between main menu and level based game on status
        if self.status == 'menu':
            self.menu.run()
        else:
            self.level.run()
            #coins ui stored within the main file. 
            self.ui.show_coins(self.coins)

#Pygame Setup and Parameters
pygame.init()
screen = pygame.display.set_mode((screen_width,screen_height))
clock = pygame.time.Clock()
game = Game()
#Runing the game loop
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    screen.fill('black')
    game.run()
    pygame.display.update()
    clock.tick(60)