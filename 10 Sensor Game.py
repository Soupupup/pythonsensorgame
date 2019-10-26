#imports required modules for programe to run
import sys,pygame,os,time,math
import Angle
import PowerBarSensor
import GameOver
pygame.init()
#size of window
size = width,height = 600,400
#sets window size and insert backgorund image
screen = pygame.display.set_mode(size)

#loads up ball and targe image
target = pygame.image.load('Target.png')
ball = pygame.image.load('Ball-2.png')
#loads up background image
background= pygame.image.load('Background-1.png')

#name the coodrinates of the ball
ballPos= ball.get_rect()
#name the coordinates of the targer
targetPos=target.get_rect()

#reset the initial coord of ball
ballPos.x=0
ballPos.y=1.2*height
#resets initial coord of the target
targetPos.x=width-30
targetPos.y=height/4

#
def display():
    #displays the backgroundfirst
    screen.blit(background, (0,0))
    #then it displays ball
    screen.blit(ball,ballPos)
    #then it displays the target
    screen.blit(target,targetPos)

#
def Result():
    #stops game with ball collides with target
    if ballPos.colliderect(targetPos):
     GameOver.GameOver(True)
     return False
    #stops game with ball collides edges of the window
    elif (ballPos.y>height):
     GameOver.GameOver(False)
     return False
    elif ballPos.x>width:
     GameOver.GameOver(False)
     return False
    else:
        return True

#counts howmany times the mouse has been clicked
mouseclick=0
#loads up the insturction image
click2start=pygame.image.load('Instructions.png')
#displays the instructions
screen.blit(click2start, (0,0))
#updates the window so the insutrciton is displayed first
pygame.display.update()

startup=True
#The continuously checks for a mouse being pressed
while startup==True:
    #checks eveyrthing that's happening in the game
    for event in pygame.event.get():
        #if mouse is pressed down
        if event.type == pygame.MOUSEBUTTONDOWN:
            #counts when it's being clicked
            mouselick+=1
            #if it's the first time mouse is clicked
            if mouseclick==1:
                #calls fn that displays bg, bal,target
                display()
                #initalise angle
                angle=0
                #sets angle to value resulted from animated arrow
                angle=Angle.SelectAngle()
            # if it's clicked the second time
            if mouseclick==2:
                #initalise velocity
                velocity=0
                #sets velocity to value resulted from powerbar selection
                velocity=PowerBarSensor.SelectVel()
                startup=False


##  ACTUAL GAME   ##
                
#variable that tells the programe to run        
running = True
#gravitational cosntant
g=1
#timestep
dt=1
#calculates the horizontal component of the velocity
inixvelocity=velocity*math.cos(angle)
#calculates the vertical component of the velocity
iniyvelocity=-velocity*math.sin(angle)

#runs the programe forever
while running==True:
    #checks all the possible events that could happen in the game
    for event in pygame.event.get():
        #if the game has quit, the system exists
        if event.type == pygame.QUIT:
            sys.exit()
    #displays images on the window
    display()
    #over time, horizontal speed stays the same
    xvelocity=inixvelocity
    #over time,vertical speed slows down by gravitational pull
    iniyvelocity+=0.5*g*dt

    #position of ball changes with speed
    ballPos.x+=xvelocity*dt
    ballPos.y+=iniyvelocity*dt
    #animates game after every loop
    pygame.display.update()
    #checks if the ball has collided with anything
    #only turns false when the ball has collided with target
    running=Result()

