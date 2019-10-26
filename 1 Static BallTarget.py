
#imports required modules for programe to run
import sys,pygame,os,time
pygame.init()
#size of window
size = width,height = 600,400
speed = [4,4]
#sets window size and insert backgorund image
screen = pygame.display.set_mode(size)
skyblue=0,231,252
#loads up ball and targe image
target = pygame.image.load('Target.png')
ball = pygame.image.load('Ball.png')
#loads up background image
background= pygame.image.load('Background-1.png')
#retreives the coodrinates of the ball
ballPos= ball.get_rect()
#retreives the coordinates of the targer
targetPos=target.get_rect()
#reset the initial coord of ball
ballPos.x=0
ballPos.y=332
#resets initial coord of the target
targetPos=(570,150)
        
running = True
angle=45
g=10
dt=1
i=0
#runs the programe forever
while running==True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    #displays the background first
    screen.blit(background, (0,0))
    #displays ball
    screen.blit(ball,ballPos)
    #displays the target
    screen.blit(target,targetPos)
    
    i+=1
    #updates the display for every loop
    pygame.display.update()
