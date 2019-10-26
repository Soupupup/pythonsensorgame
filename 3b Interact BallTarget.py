#imports required modules for programe to run
import sys,pygame,os,time,math
pygame.init()
#size of window
size = width,height = 600,400
speed = [4,4]
#sets window size and insert backgorund image
screen = pygame.display.set_mode(size)

#loads up ball and targe image
target = pygame.image.load('Target.png')
ball = pygame.image.load('Ball-2.png')

#loads up startup background image
startupbg=pygame.image.load('Click_To_Start.png')
#loads up game background image
background= pygame.image.load('Background-1.png')
#loads up game over image
youmiss= pygame.image.load('Game_Over.png')
youwin=pygame.image.load('Nice_Work.png')

#retreives the coodrinates of the ball
ballPos= ball.get_rect()
#retreives the coordinates of the targer
targetPos=target.get_rect()
#reset the initial coord of ball
ballPos.x=0
ballPos.y=332
#resets initial coord of the target
targetPos.x=570
targetPos.y=100

#variable that tells the programe to run        
running = True
#gravitational cosntant
g=1
#timestep
dt=1
#tells you whether the mouse has been clicked
mouseclick=False
screen.blit(startupbg, (0,0))
pygame.display.update()




#display text for when the ball hits something
def GameOver(strike):
    running = False
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    #displays 'you win' image for when ball hits the target
    if strike==True:
        screen.blit(youwin, (0,0))
    #displays 'you miss' image when the ball hits everywhere else
    else:
        screen.blit(youmiss, (0,0))

#runs the programe forever
while running==True:
    #checks all the possible events that could happen in the game
    for event in pygame.event.get():
        #if the game has quit, the system exists
        if event.type == pygame.QUIT: sys.exit()
        #only run if the mouse has been click on the pygame display
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseclick==False:
                #updates the display
                pygame.display.update()
                #asks user to input the projection speed
                speed=float(input('Enter the speed of the ball:'))
                #asks user to input the projection angle
                angle=float(input('Enter the angle of projection:'))
                #calcualtes the horizontal component of the speed
                inixspeed=speed*math.cos(angle)
                #calculates the vertical component of the speed
                iniyspeed=-speed*math.sin(angle)
                mouseclick=True
            

    #only runs if the mouse has been clicked
    if mouseclick==True:
    #displays the background first
        screen.blit(background, (0,0))
        #displays ball
        screen.blit(ball,ballPos)
        #displays the target
        screen.blit(target,targetPos)
        #over time, horizontal speed stays the same
        xspeed=inixspeed
        #over time,vertical speed slows down by gravitational pull
        iniyspeed+=0.5*g*dt
        
        #position of ball changes with speed
        ballPos.x+=xspeed*dt
        ballPos.y+=iniyspeed*dt
        
        #stops game with ball collides with target
        if ballPos.colliderect(targetPos):
            GameOver(True)
            running = False
        #stops game with ball collides edges of the window
        elif (ballPos.y>height):
            GameOver(False)
            running = False
        elif ballPos.x>width:
            GameOver(False)
            running = False
        elif ballPos.y==0:
            GameOver(False)
            running = False
    #animates game after every loop
        pygame.display.update()
