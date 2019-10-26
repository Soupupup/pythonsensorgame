#imports required modules for programe to run
import sys,pygame,os,time,math
import time
pygame.init()
#size of window
size = width,height = 600,400
speed = [4,4]
#sets window size and insert backgorund image
screen = pygame.display.set_mode(size)
mouseclick=1
startupBG=pygame.image.load('Click_to_Start.png')
instructions=pygame.image.load('Instructions.png')
screen.blit(startupBG, (0,0))
#updates the display
pygame.display.update()
angle=0


startup=True
while startup==True:
    for event in pygame.event.get():
        if event.type == pygame.MOUSEBUTTONDOWN:
            if mouseclick==1:
                screen.blit(instructions, (0,0))
                pygame.display.update()
            if mouseclick==2:
                #loads up ball and targe image
                target = pygame.image.load('Target.png')
                ball = pygame.image.load('Ball-2.png')
                arrow =  pygame.image.load('arrow.png')
                #loads up background image
                background= pygame.image.load('Background-1.png')
                #loads up game over image
                youmiss= pygame.image.load('Game_Over.png')
                youwin=pygame.image.load('Nice_Work.png')

                #retreives the coodrinates of the ball
                ballPos= ball.get_rect()
                #retreives the coordinates of the targer
                targetPos=target.get_rect()

                arrowPos=arrow.get_rect()
                #reset the initial coord of ball
                ballPos.x=0
                ballPos.y=332
                #resets initial coord of the target
                targetPos.x=570
                targetPos.y=100

                arrowPos.x=0
                arrowPos.y=300

                degree = 0
                run=True
                while run==True:
                    arrowblit=screen.blit(arrow,arrowPos)
                    screen.blit(background, (0,0))
                    #displays ball
                    screen.blit(ball,ballPos)
                    #displays the target
                    screen.blit(target,targetPos)
                    oldCenter = arrowblit.center

                    rotatedArrow =  pygame.transform.rotate(arrow, degree)

                    rotPos = rotatedArrow.get_rect()

                    rotPos.center = oldCenter

                    screen.blit(rotatedArrow, rotPos)

                    degree-=5
                    if degree < -90:
                        degree = 0

                    pygame.display.flip()
                    pygame.time.wait(60)

                    for event in pygame.event.get():
                        if event.type == pygame.MOUSEBUTTONDOWN:
                            mouseclick=3
                            run=False
            if mouseclick==3:
                angle=abs(math.radians(90+degree))
                run=True
                Power=pygame.image.load('Power_Bar.png')
                Pointer=pygame.image.load('Pointer.png')
                PowerPos=Power.get_rect()
                PointPos=Pointer.get_rect()
                initx=185
                endx=365
                step=5
                x=185

                PowerPos=(200,200)
                while run==True:
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
                        #displays ball
                        screen.blit(ball,ballPos)
                        #displays the target
                        screen.blit(target,targetPos)
                        pygame.display.update()
                        for event in pygame.event.get():
                            if event.type == pygame.MOUSEBUTTONDOWN:
                                run=False
                                velocity=((x-initx)/(endx-initx))*40
                startup=False
            mouseclick+=1

inixvelocity=velocity*math.cos(angle)
#calculates the vertical component of the speed
iniyvelocity=-velocity*math.sin(angle)

#variable that tells the programe to run        
running = True
#gravitational cosntant
g=1
#timestep
dt=1

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
     
  #displays the background first
  screen.blit(background, (0,0))
  #displays ball
  screen.blit(ball,ballPos)
  #displays the target
  screen.blit(target,targetPos)
  #over time, horizontal speed stays the same
  xvelocity=inixvelocity
  #over time,vertical speed slows down by gravitational pull
  iniyvelocity+=0.5*g*dt

  #position of ball changes with speed
  ballPos.x+=xvelocity*dt
  ballPos.y+=iniyvelocity*dt

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


