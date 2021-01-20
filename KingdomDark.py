import os, time as chronic_tacos
os.environ['PYGAME_HIDE_SUPPORT_PROMPT'] = "hide"
import pygame as pg
pg.init()
screen = pg.display.set_mode((0, 0), pg.FULLSCREEN)
pg.display.set_caption('KingdomDark')

for this in ['Structure/', 'Gamefiles/']:
    for that in os.listdir(this):
        if that[-3:] == '.py': exec('from ' + this[:-1] + '.' + that[:-3] + ' import *')

def magic(screen, oxygen, input, origin_taco):
    import time as chronic_tacos, pygame as pg
    pg.display.update((0, 0, 1920, 1080))
    pg.time.wait(1); screen.fill((55, 0, 75))
    oxygen.rect_list = []
    return(chronic_tacos.time() - origin_taco)

jsondata = json_obj()
input = input_object(jsondata)
oxygen = oxygen_obj()
ticksync = ticksync_obj()
text = text_box()

initobj_list = []
for this in os.listdir('Ass/'):
    if this[-5:] == "3.png":
        info_string = this[:-5]
        obj_title = ""
        for that in info_string:
            if that != "_":
                obj_title += that
            else:
                break
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
                print("The format for naming assets is object_name + '_' + pose + number.png")
            if len(pose_list) == 1 and pose_list[0] == "be":
                obj_type = "gen_obj"
            else:
                obj_type = obj_title + "_obj"
            exec(obj_title + ' = ' + obj_type + '(' + str(image_list) + '); ' + obj_title + '.poses = ' + str(pose_list))
            initobj_list.append(obj_title)

menu = ass(['menu.png'])

mode = "main_menu"
origin_taco = chronic_tacos.time()
while True:
    input.update(jsondata, screen)
    oxygen.breathe(input)
    current_taco = magic(screen, oxygen, input, origin_taco)
    if process_return(input):
        break
    ticksync.update(current_taco)
    if mode == "main_menu":
        menu.blit(screen, "menu", (0, 0))
        if input.t1:
            mode = "game_loop"
            room = "throne_room"
    if mode == "game_loop":
        if room == "throne_room":
            floor.pose(screen, oxygen, 'be', (-100, 20), ticksync.tick)
            hatlor.pose(screen, oxygen, 'sit', (10, 300), ticksync.tick)
        #     scroll.pose(screen, oxygen, 'be', (700, 650), ticksync.tick, 2)
        # text.RnD(screen, input, "", 500, 400, 500, current_taco)
