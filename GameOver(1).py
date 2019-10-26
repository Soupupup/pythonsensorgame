import pygame
pygame.init()
#size of window
size = width,height = 600,400
speed = [4,4]
#sets window size and insert backgorund image
screen = pygame.display.set_mode(size)

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
