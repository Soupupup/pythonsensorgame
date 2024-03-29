
#text box example use

import pygooey
import pygame as pg

pg.init()
screen = pg.display.set_mode((600,400))
screen_rect = screen.get_rect()
done = False
speed=""
def print_on_enter(id, final):
    if event.type==pg.KEYDOWN:
        if event.key==pg.K_:
            return final

#see all settings help(pygooey.TextBox.__init__)
settings = {
    "command" : print_on_enter,
    "inactive_on_enter" : False,
}
entry = pygooey.TextBox(rect=(70,100,150,30), **settings)

while not done:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            done = True
        entry.get_event(event)
    speed=entry.update()
    if event.type == pg.MOUSEBUTTONDOWN:   
        print ("Speed= ",speed)
    entry.draw(screen)
    pg.display.update()
