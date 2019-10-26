#imports required modules for programe to run
import sys,pygame,os,time,math
pygame.init()
#size of window
size = width,height = 600,400
speed = [4,4]
#sets window size and insert backgorund image
screen = pygame.display.set_mode(size)
mouseclick=1
click2start=pygame.image.load('Instructions.png')
screen.blit(click2start, (0,0))
#updates the display
pygame.display.update()


#loads up ball and targe image
target = pygame.image.load('Target.png')
ball = pygame.image.load('Ball-2.png')
background= pygame.image.load('Background-1.png')

#loads up background image
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

def display():
    screen.blit(background, (0,0))
    #displays ball
    screen.blit(ball,ballPos)
    #displays the target
    screen.blit(target,targetPos)

def SelectAngle():
    degree=0
    arrow =  pygame.image.load('arrow.png')
    arrowPos=arrow.get_rect()
    arrowPos.x=0
    arrowPos.y=300
    run=True
    while run==True:
        arrowblit=screen.blit(arrow,arrowPos)
        display()
        oldCenter = arrowblit.center

        rotatedArrow =  pygame.transform.rotate(arrow, degree)

        rotPos = rotatedArrow.get_rect()

        rotPos.center = oldCenter

        screen.blit(rotatedArrow, rotPos)

        degree-=5
        if degree < -90:
            degree = 0

        pygame.display.update()
        pygame.time.wait(60)

        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                run=False
                degree=math.radians(90+degree)
                return abs(degree)

def SelectVel():
    velocity=0
    run=True
    Bar=pygame.image.load('Power_Bar.png')
    Pointer=pygame.image.load('Pointer.png')
    BarPos=Bar.get_rect()
    PointPos=Pointer.get_rect()
    BarPos=(200,200)
    initx=185
    endx=365
    step=5
    x=185
    while run==True:
        display()
        screen.blit(Bar, BarPos)
        x+=step
        if x>endx:
            x-=step
            step*=-1
        if x<initx:
            x-=step
            step*=-1
        PointPos=(x,225)
        screen.blit(Pointer, PointPos)
        pygame.display.update()
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                run=False
                velocity=((x-initx)/(endx-initx))*40
                return velocity

def Result():
    #stops game with ball collides with target
    if ballPos.colliderect(targetPos):
     GameOver(True)
     return False
    #stops game with ball collides edges of the window
    elif (ballPos.y>height):
     GameOver(False)
     return False
    elif ballPos.x>width:
     GameOver(False)
     return False
    else:
        return True

#display text for when the ball hits something
def GameOver(strike):
    #loads up game over image
    youmiss= pygame.image.load('Game_Over.png')
    youwin=pygame.image.load('Nice_Work.png')
    running = False
    for event in pygame.event.get():
       if event.type == pygame.QUIT: sys.exit()
    #displays 'you win' image for when ball hits the target
    if strike==True:
       screen.blit(youwin, (0,0))
       pygame.display.update()
    #displays 'you miss' image when the ball hits everywhere else
    else:
       screen.blit(youmiss, (0,0))
       pygame.display.update()

velocity=0
startup=True
while startup==True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseclick==1:
                display()
                angle=0
                angle=SelectAngle()
                mouseclick=2
                print(angle)
            if mouseclick==2:
                velocity=SelectVel()
                print(velocity)
                startup=False
                
#variable that tells the programe to run        
running = True
#gravitational cosntant
g=1
#timestep
dt=1
inixvelocity=velocity*math.cos(angle)
#calculates the vertical component of the speed
iniyvelocity=-velocity*math.sin(angle)
print(inixvelocity)
print(iniyvelocity)
#runs the programe forever
while running==True:
    #checks all the possible events that could happen in the game
    for event in pygame.event.get():
        #if the game has quit, the system exists
        if event.type == pygame.QUIT:
            sys.exit()
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
    running=Result()
    


