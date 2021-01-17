import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption('KingdomDark')

for this in ['Structure/', 'Gamefiles/']:
    for that in os.listdir(this):
        if that[-3:] == '.py': exec('from ' + this[:-1] + '.' + that[:-3] + ' import *')

jsondata = json_obj()
input = input_object(jsondata)

bg_color = (125, 55, 0)
while True:
    input.update(jsondata, screen)
    if process_return(input):
        break
    images.blit()
    pg.time.wait(1); pg.display.flip(); screen.fill(bg_color)
