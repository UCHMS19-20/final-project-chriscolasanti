import sys
import pygame 

pygame.init() #pygame will always be running


screen = pygame.display.set_mode( (800, 400) ) #create the screen for the game
print(pygame.QUIT)
 #Make the screen black
screen_height = 500
screen_width = 300

usermoverate = [.5,0] #Speed at which the user will move
badobjectminspeed = [0,1] #Min and max speed the objects will fall from the sky at
badobjectmaxspeed = [0,10] 
addnewbadobject = 5

userpos = [368, 368]

user = pygame.image.load("src/img/donut.png")
userrect = user.get_rect()
badobjects = pygame.image.load("src/img/ketchup.png")

    
        
pygame.mouse.set_visible(False)

moveLeft = moveRight = moveUp = moveDown = False
badobjectAddCounter = 0

while True:
    screen.fill( (0,0,0) )
    if moveLeft:
        userpos[0] -= usermoverate[0]
        userpos[1] -= usermoverate[1]
    if moveRight:
        userpos[0] += usermoverate[0]
        userpos[1] += usermoverate[1]
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        if event.type == pygame.KEYDOWN:
                if event.key == ord('a'):
                    moveRight = False
                    moveLeft = True
                if event.key == ord('d'):
                    moveLeft = False
                    moveRight = True
                if event.type == pygame.KEYUP:
                    if event.key == K_LEFT or event.key == ord('a'):
                        moveLeft = False
                    if event.key == K_RIGHT or event.key == ord('d'):
                        moveRight = False
    screen.blit(user, (userpos[0], userpos[1]))
    pygame.display.update()
