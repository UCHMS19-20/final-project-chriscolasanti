import sys
import pygame 

pygame.init() #pygame will always be running


screen = pygame.display.set_mode( (300, 500) ) #create the screen for the game
print(pygame.QUIT)

screen.fill( (0,0,0) ) #Make the screen black

usermove rate = 5 #Speed at which the user will move
objectminspeed = [0,1] #Min and max speed the objects will fall from the sky at
objectmaxspeed = [0,10] 

user = pygame.image.load("img/")
userrect = user.get_rect()
Objects = pygame.image.load("img/")


