import os
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg, mingus
from mingus.midi import fluidsynth
fluidsynth.init('Resources/' + "Florestan_Piano.sf2")
pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

for this in os.listdir('Structure/'):
    if this[-3:] == '.py': exec('from Structure.'  + this[:-3] + ' import *')

"""
Apollo is my first attempt at a music creation program thing.
I am using pygame for key input, and I plan on using the screen to make it cool and usable and stuff.
I am planning on using mingus for the music part.
Maybe this is one of my better works; I will give it my best right now during this pandemic.
- Jonathan Binns, 10/6/20 (I'm 17)
"""

jsondata = json_obj()
input = input_object(jsondata)
UI = UI_obj(jsondata)
synth = synth_obj(jsondata)

for this in jsondata.preferences:
    exec(this + ' = ' + jsondata.preferences[this])

while running:
    input.update(jsondata, screen)
    if process_return(input):
        break
    synth.play(jsondata, input, 'oopsie')
    UI.draw(jsondata, input, screen)
    pg.time.wait(1); pg.display.flip(); screen.fill(bg_color)
