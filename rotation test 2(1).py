import pygame

#necessary pygame initializing
pygame.init()

#create a surface that will be seen by the user
screen =  pygame.display.set_mode((600, 400))
background= pygame.image.load('Background-1.png')

#create a varible for degrees pf rotation
degree = 0
while True:
    screen.blit(background, (0,0))

    #create shapes so you can tell rotation is happenning
    ball =  pygame.image.load('arrow.png')

    ##ORIGINAL UNCHANGED
    #what coordinates will the static image be placed:
    where = 200, 200

    #draw surf to screen and catch the rect that blit returns
    blittedRect = screen.blit(ball, where)

    screen.blit(background, (0,0))
    ##ROTATED
    #get center of surf for later
    oldCenter = blittedRect.center

    #rotate surf by DEGREE amount degrees
    rotatedSurf =  pygame.transform.rotate(ball, degree)

    #get the rect of the rotated surf and set it's center to the oldCenter
    rotRect = rotatedSurf.get_rect()
    rotRect.center = oldCenter

    #draw rotatedSurf with the corrected rect so it gets put in the proper spot
    screen.blit(rotatedSurf, rotRect)

    degree-=5

    if degree <-90:
        degree = 0



    #show the screen surface
    pygame.display.flip()
    pygame.time.wait(60)

