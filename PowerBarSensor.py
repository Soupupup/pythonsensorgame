#!/usr/local/bin/python

import RPi.GPIO as GPIO
import time
import sys,pygame,os,time,math

GPIO.setmode(GPIO.BOARD)

#define the pin that goes to the circuit
pin_to_circuit = 37

def rc_time (pin_to_circuit):
    count = 0
  
    #Output on the pin for 
    GPIO.setup(pin_to_circuit, GPIO.OUT)
    GPIO.output(pin_to_circuit, GPIO.LOW)
    time.sleep(0.1)

    #Change the pin back to input
    GPIO.setup(pin_to_circuit, GPIO.IN)
  
    #Count until the pin goes high
    while (GPIO.input(pin_to_circuit) == GPIO.LOW):
        count += 1

    return count


pygame.init()
#size of window
size = width,height = 600,400
speed = [4,4]
#sets window size and insert background image
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

#this piece of code allows user to select a velocity
#on a power bar and stopping it by covering a LDR
def SelectVel():
    
    velocity=0
    count=0
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
    #loops forever until the ldr is covered i.e. velocity is picked
    while run==True:
        count=rc_time(pin_to_circuit)
        screen.blit(background, (0,0))
        #displays ball
        screen.blit(ball,ballPos)
        #displays the target
        screen.blit(target,targetPos)
        screen.blit(Bar, BarPos)
        #moves pointer 5 across the screen every loop
        x+=step
        #if the pointer reaches the edge of right side of the bar
        if x>endx:
            #
            x-=step
            #direciton of the pointer change to the left
            step*=-1

        #if the pointer reaches the edge of left side of the bar
        #direction of the pointer change to the right
        if x<initx:
            x-=step
            step*=-1

        #
        PointPos=(x,225)
        screen.blit(Pointer, PointPos)
        pygame.display.update()
        if count>100000:
            run=False
            velocity=((x-initx)/(endx-initx))*40
            return velocity
        





