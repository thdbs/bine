__author__ = '성소윤'

import game_framework
from pico2d import *

import title_state


name = "HappyEndState"
image = None
bgm = None
logo_time = 0.0


def enter():
    global image, bgm
    image = load_image('Resource/Sprites/bg_menu_main.png')
    bgm = load_music('Resource/Sound/bgm_victory.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()


def exit():
    global image, bgm
    image = None
    bgm.stop()
    bgm = None


def update(frameTime):
    global logo_time

    if(logo_time > 3.0):
        logo_time = 0.0
        game_framework.change_state(title_state)
    delay(0.01)
    logo_time += 0.01



def draw():
    global image
    clear_canvas()
    image.clip_draw(0, 0, 1280, 720, 640, 360 )
    update_canvas()




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass