import sys,pygame,os,time,math
import time
pygame.init()
#size of window
size = width,height = 600,400
speed = [4,4]
#sets window size and insert backgorund image
screen = pygame.display.set_mode(size)

background= pygame.image.load('Background-1.png')
Power=pygame.image.load('Power_Bar.png')
Pointer=pygame.image.load('Pointer.png')
running=True
initx=185
endx=365
step=5
x=185
PowerPos=Power.get_rect()
PointPos=Pointer.get_rect()
PowerPos=(200,200)
while running==True:
    screen.blit(background, (0,0))
    screen.blit(Power, PowerPos)
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
            running=False
            speed=((x-initx)/(endx-initx))*40
            print(speed)
            screen.blit(background, (0,0))
            pygame.display.update()

