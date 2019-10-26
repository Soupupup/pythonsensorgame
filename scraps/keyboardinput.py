import pygame
from pygame.locals import *

pygame.init()
screen = pygame.display.set_mode((200,200))

while(True):
   for event in pygame.event.get():
      if (event.type == KEYDOWN):
	 x = pygame.key.get_mods()
	 print pygame.key.name(x)
         if (event.key == K_RETURN):
           print "numpad 0"
         if (event.key == K_BACKSPACE):
           print "numpad 1"
