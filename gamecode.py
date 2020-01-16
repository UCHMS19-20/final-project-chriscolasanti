import sys
import pygame 
import random

class Bad_object:
    def __init__(self, x, speed):
        self.x = x
        self.y = 0
        self.speed = speed
    def move_down(self):
        self.y += self.speed
    def return_coords(self):
        return (int(self.x), int(self.y))

pygame.init() #pygame will always be running

screen = pygame.display.set_mode( (800, 600) ) #create the screen for the game
print(pygame.QUIT)
 #Make the screen black
screen_height = 600
width = 800
lives = 5

usermoverate = [.5,0] #Speed at which the user will move

userpos = [368, 535]

user = pygame.image.load("src/img/donut.png")
userrect = user.get_rect()
badobject = pygame.image.load("src/img/ketchup1.png")

pygame.mouse.set_visible(False)

moveLeft = moveRight = moveUp = moveDown = False

count = 0
bad_objects = []

def add_to_bad_objects():
    x = random.randint(0, 800)
    speed = random.randint(1, 5)
    bad_objects.append(Bad_object(x, speed / 10.0))
score = 0
count = 0
while True:
    print(score)
    while lives != 0: 
        screen.fill( (0,0,0) )
        if count % 200 == 0:
            # print(f"There are {len(bad_objects)} bad objects")
            add_to_bad_objects()
        for i in bad_objects:
            i.move_down()
            screen.blit(badobject, i.return_coords())

        if i[1] == 600:
            score += 1        
     
        keystate = pygame.key.get_pressed()
        if keystate[pygame.K_a]:
            if userpos[0] >5:
                userpos[0] -= usermoverate[0]
                userpos[1] -= usermoverate[1]
        if keystate[pygame.K_d]:
            if userpos[0] < 730:
                userpos[0] += usermoverate[0]
                userpos[1] += usermoverate[1]
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(user, (userpos[0], userpos[1]))
        count += 1
        pygame.display.update()

user_rect = user.get.rect(center(user_x, user_y))
badobject_rect = badobject.get_rect(center(badobject_x, badobject_y))
if user_rect.colliderect(badobject_rect):
    badobjectpos_x = random.randrange(0, width)
    badobjectpos_y = 5000
    lives -=1

if lives == 0:
    pygame.quit()
    sys.exit()
    




