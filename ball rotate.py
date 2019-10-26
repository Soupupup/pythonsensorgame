import sys,pygame,os,time,math

pygame.init()
#size of window
size = width,height = 600,400
speed = [4,4]
#sets window size and insert backgorund image
screen = pygame.display.set_mode(size)


ball= pygame.image.load('arrow.png')
ballimage=ball
background= pygame.image.load('Background-1.png')

ballposs=ballimage.get_rect()
ballposs.x=100
ballposs.y=100

ballposs.center=(ballposs.x,ballposs.y)
#retreives the coodrinates of the ball
angle=0



running=True

while running== True:
    angle=(angle-2)% -90
    screen.blit(background, (0,0))

    rotatedball=pygame.transform.rotate(ball, angle)

    screen.blit((100,100))    

    pygame.display.update()

    
