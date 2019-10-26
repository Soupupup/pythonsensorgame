## Script 5: Angle
## This script uses PyGame as a tool for animating a moving arrow
## that allows user to select a launch angle for a projectile motion

##################################################################
### Importing necessary Modules ##################################
##################################################################
import sys,pygame,os,time, math
##################################################################

##################################################################
### Initialising PyGame         ##################################
##################################################################
pygame.init()
##################################################################

## Initial set up
## Loading images used in the game
target = pygame.image.load('Target.png')
ball = pygame.image.load('Mountain.png')
background= pygame.image.load('Snowball.png')

size = width,height = 1080,720 # defines size of pygame window
screen = pygame.display.set_mode(size) # sets screen size to 
                                       # defined size

ballPos= ball.get_rect() # position of ball on screen
targetPos=target.get_rect() # position of target on screen

## setting x and y position of the ball on screen
ballPos.x = 50
ballPos.y = 720-100

## setting x and y position of the target on screen
targetPos.x = 950
targetPos.y = 150

##################################################################
##Function that allows user to select a launch angle
##################################################################
def SelectAngle():
    degree=0 #initialise angle in degrees
    arrow =  pygame.image.load('arrow.png') #loading arrow image
    arrowPos=arrow.get_rect()
    
    ## setting x and y position of the arrow on screen
    arrowPos.x=0
    arrowPos.y=300
    
    ## Loop where the game lives
    run=True
    while run==True:
        arrowblit=screen.blit(arrow,arrowPos) # displays original arrow
        screen.blit(background, (0,0)) # displays background image on 
                                       # screen (from origin (0,0))
        screen.blit(ball,ballPos) # displays ball
        screen.blit(target,targetPos) # displays the target
        
        ## Transforming arrow image to a certain angle
        oldCenter = arrowblit.center #saves original center coord
        ## Rotate the original image without modifying it
        rotatedArrow =  pygame.transform.rotate(arrow, degree)
        #setting center of newly rotated image to original center coord
        rotPos = rotatedArrow.get_rect()
        rotPos.center = oldCenter 
        screen.blit(rotatedArrow, rotPos)# displays the rotated arrow

        
        degree-=5 #increase rotation angle(clock-wise) by 5
        ## When angle is bigger 90, resets rotation to zero
        if degree < -90: 
            degree = 0

        pygame.display.update()  #increase rotation angle(clock-wise) by 5
        pygame.time.wait(60) #updates window display

        ## the code below waits until a "MOUSEDOW" event happens, i.e. when mouse 
        ## is pressed, and an angle has been selected
        for event in pygame.event.get():
            if event.type == pygame.MOUSEBUTTONDOWN:
                run=False #stops animation
                degree=math.radians(90+degree) #convert angle to radians
                return abs(degree) #returns an absolute value of the angle
            
##################################################################
##################################################################
