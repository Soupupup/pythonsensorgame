import pygame
import sys
import time

def rotate45(gameObject, rotations={}):
    r = rotations.get(gameObject,0) + 20
    rotations[gameObject] = r
    return pygame.transform.rotate(gameObject, r)

def main():
    pygame.init()
    screen = pygame.display.set_mode((800,600))
    Tardis = pygame.image.load('Ball-2.png')

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.fill( (0,0,0) )
        rotatedTardis = rotate45(Tardis)
        screen.blit(rotatedTardis, (400,300))
        pygame.display.update()
        time.sleep(1)

main()
