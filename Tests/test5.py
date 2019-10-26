from tkinter import *
#imports required modules for programe to run
import sys,pygame,os,time
import numpy as np
import math


def run():
   print("Velocity: %s\nAngle: %s" % (e1.get(), e2.get()))
   pygame.init()
   #size of window
   size = width,height = 600,400
   speed = [4,4]
   #sets window size and insert backgorund image
   screen = pygame.display.set_mode(size)

   #loads up ball and targe image
   target = pygame.image.load('Target.png')
   ball = pygame.image.load('Ball-2.png')
   #loads up background image
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
   running = False
   #gravitational cosntant
   g=1
   #timestep
   dt=1
   speed=float(e1.get())
   angle=float(e2.get())
   inixspeed=speed*math.cos(angle)
   iniyspeed=-speed*math.sin(angle)
   print(inixspeed,iniyspeed)
   running=True
   while running==True:
      
      #checks all the possible events that could happen in the game
      for event in pygame.event.get():
           #if the game has quit, the system exists
           if event.type == pygame.QUIT: sys.exit()
           #only run if the mouse has been click on the pygame display
      #calcualtes the horizontal component of the speed
      inixspeed=speed*math.cos(angle)
      #calculates the vertical component of the speed
      iniyspeed=-speed*math.sin(angle)
      
      #over time, horizontal speed stays the same
      xspeed=inixspeed
      #over time,vertical speed slows down by gravitational pull
      iniyspeed+=0.5*g*dt

      #position of ball changes with speed
      ballPos.x+=xspeed*dt
      ballPos.y+=iniyspeed*dt

      #displays the background first
      screen.blit(background, (0,0))
      #displays ball
      screen.blit(ball,ballPos)
      #displays the target
      screen.blit(target,targetPos)
      #updates the display for every loop

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
   return True, speed, angle
   

master = Tk()
Label(master, text="Velocity").grid(row=0)
Label(master, text="Angle").grid(row=1)

e1 = Entry(master)
e2 = Entry(master)

e1.grid(row=0, column=1)
e2.grid(row=1, column=1)

Button(master, text='Quit', command=master.quit).grid(row=3, column=0, sticky=W, pady=4)
Button(master, text='Show', command=run).grid(row=3, column=1, sticky=W, pady=4)

mainloop( )



