import os, threading, time as chronic_tacos
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)

pg.display.set_caption('KingdomDark'); pg.mouse.set_visible(False)

for this in ['Structure/', 'Gamefiles/']:
    for that in os.listdir(this):
        if that[-3:] == '.py': exec('from ' + this[:-1] + '.' + that[:-3] + ' import *')

def magic(screen, oxygen, inpt, origin_taco):
    import time as chronic_tacos, pygame as pg
    pg.display.update()
    pg.time.wait(1); screen.fill((60, 20, 70))
    oxygen.rect_list = []
    return(chronic_tacos.time() - origin_taco)

jsondata = json_obj()
inpt = input_object(jsondata)
oxygen = oxygen_obj()
ticksync = ticksync_obj()
text = text_box()
mouse = mouse_obj()
event = event_obj()

initobj_list = []
for this in os.listdir('Ass/'):
    if this[-5:] == "3.png":
        info_string = this[:-5]
        obj_title, null = info_string.split('_')
        image_list = []; pose_list = []
        if not obj_title in initobj_list:
            for that in os.listdir('Ass/'):
                if that[:len(obj_title)] == obj_title:
                    image_list.append(that)
                    pose = that[len(obj_title) + 1:-5]
                    if not pose in pose_list:
                        pose_list.append(pose)
            if len(image_list) / 3 != len(pose_list):
                print("Error! The following image list is incomplete or incorrect: \n" + str(image_list))
                raise Exception("The format for naming assets is object_name + '_' + pose + number.png")
            elif len(pose_list) == 1 and pose_list[0] == "be":
                obj_type = "gen_obj"
            elif "stand" in pose_list and "flipp" in pose_list:
                obj_type = "person_obj"
            else:
                obj_type = obj_title + "_obj"
            exec(obj_title + ' = ' + obj_type + '(' + str(image_list) + '); ' + obj_title + '.poses = ' + str(pose_list))
            initobj_list.append(obj_title)

menu = ass(['menu.png'])

mode = "main_menu"
origin_taco = chronic_tacos.time(); ticksync.tick = 1
while True:
    inpt.update(jsondata, screen)
    oxygen.breathe(inpt)
    mouse.curse(screen, inpt, ticksync.tick); mouse.rect_intake(screen, inpt)
    inpt.mouse = mouse
    current_taco = magic(screen, oxygen, inpt, origin_taco)
    if process_return(inpt):
        break
    ticksync.update(current_taco)
    if mode == "main_menu":
        menu.blit(screen, "menu", (0, 0))
        if inpt.t1:
            mode = "game_loop"
            time = "dawn"
    if mode == "game_loop":
        if time == "dawn":
            view.pose(screen, oxygen, 'be', (620, 200), ticksync.tick, -2, (500, 500, 670, 490))
            click_box = curtain.waiting(screen, oxygen, inpt, 'wait', (587, 122), ticksync.tick, 1.5)
            if click_box.collidepoint(inpt.mx, inpt.my): mouse.rect_list.append('curtain')
            throneroom.pose(screen, oxygen, 'be', (0, 20), ticksync.tick)
            if mouse.rect_over == 'curtain' and inpt.t1:
                time = 'day'
        if time == "day":
            view.pose(screen, oxygen, 'be', (620, 200), ticksync.tick, -2, (500, 500, 670, 490))
            opencurtain.pose(screen, oxygen, 'be', (587, 122), ticksync.tick, 1.5)
            throneroom.pose(screen, oxygen, 'be', (0, 20), ticksync.tick)
            character_dict = {advisor: 1, jester: 2}
            if event.go(screen, oxygen, inpt, current_taco, ticksync.tick, jsondata, text, character_dict):
                time = 'dusk'
    if mode == "write":
        inpt.screenlist = [(1, 1), pg.RESIZABLE]
        if not hasattr(inpt, 'count'):
            inpt.count = 0
        else:
            break

if mode == "write":
    write_mode(jsondata)
