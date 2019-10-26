import sys,pygame,os,time,math
pygame.init()
#size of window
size = width,height = 600,400
speed = [4,4]
#sets window size and insert backgorund image
screen = pygame.display.set_mode(size)
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
        screen.blit(background, (0,0))
        #displays ball
        screen.blit(ball,ballPos)
        #displays the target
        screen.blit(target,targetPos)
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
