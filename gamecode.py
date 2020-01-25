import sys
import pygame 
import pygame.ftfont
import random #used for randomly generating something

pygame.init() #pygame will always be running
pygame.font.init() #initializes the fonts

class Bad_object: 
"""defining the bad objects and how they fall from the top of the screen"""
    def __init__(self, x, speed):
        self.x = x
        self.y = 0
        self.speed = speed 
    def move_down(self):
        self.y += self.speed
    def return_coords(self):
        return (int(self.x), int(self.y))

font1 = pygame.font.SysFont("comicsansms", 60) #these are the fonts used for the end game screen and live score
font2 = pygame.font.SysFont("comicsansms", 15)

screen = pygame.display.set_mode( (800, 600) ) #create the screen for the game
print(pygame.QUIT)

width = 800 #variable for the width of the screen
lives = 5 #variable for the lives of the game 
usermoverate = [.5,0] #speed at which the user will move

userpos = [368, 535] #the users start position

user = pygame.image.load("src/img/donut.png") #the user 
userrect = user.get_rect()
badobject = pygame.image.load("src/img/ketchup1.png") #the bad guys

pygame.mouse.set_visible(False) #the mouse cursor cannot be seen

moveLeft = moveRight = moveUp = moveDown = False

count = 0
bad_objects = []

def add_to_bad_objects(): #spawns and creates a speed for the falling object
    x = random.randint(0, 800)
    speed = random.randint(1, 5) 
    bad_objects.append(Bad_object(x, speed / 10.0))
score = 0

time = 0 #Timing for the loop that quits out of the game

while True:
    while lives != 0: #main game loop
        screen.fill( (0,0,0) )
        text_livescore = font2.render(f"score: {score}", False,(0,122,0)) #score system as the game is playing
        screen.blit(text_livescore, (700,20))
        if count % 200 == 0: #spawns the bad objects at random intervals
            # print(f"There are {len(bad_objects)} bad objects")
            add_to_bad_objects()
        for i in bad_objects:
            i.move_down()
            screen.blit(badobject, i.return_coords())
     
        keystate = pygame.key.get_pressed() #moves the user left and right
        if keystate[pygame.K_a]:
            if userpos[0] >5: #stops the user from moving off of the left side of the screen
                userpos[0] -= usermoverate[0]
                userpos[1] -= usermoverate[1]
        if keystate[pygame.K_d]:
            if userpos[0] < 730: #stops the user from moving off of the right side of the screen
                userpos[0] += usermoverate[0]
                userpos[1] += usermoverate[1]
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(user, (userpos[0], userpos[1])) #constantly updates the users position 
        count += 1
        user_rect = user.get_rect(center = (userpos[0], 535)) #creates the hitbox for the user
        for i in bad_objects: #when the bad objects reach a certain y coordinate the score will be changed
            i_rect = badobject.get_rect(center = (i.return_coords())) #creates the hitbox for the enemy
            if i.y >= 600 and i.y <= 655:
                score += 10 
                i.y += 60 #telepors the object out of the score range to make sure it is only added once
            if user_rect.colliderect(i_rect): #when a collision happens a life is lost
                i.y += 700 #teleports the bad object out of the screen
                lives -=1
                print(lives)
        pygame.display.update()
        if lives == 0: #if the user runs out of lives the main loops ends
            while time < 1000: #shows the final screen for a count of 50 then quits out of the game
                time += 1
                screen.fill( (0,0,0) ) #displays the final score and game over
                text_score = font1.render(f"Final Score: {score}", True, (0,127,0)) 
                screen.blit(text_score, (200,400)) 
                text_end = font1.render("GAME OVER", True, (0,127,0)) 
                screen.blit(text_end, (230,100))
                pygame.display.update()
            sys.quit #quits out of the game

