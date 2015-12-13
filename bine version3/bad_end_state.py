__author__ = '성소윤'

import game_framework
from pico2d import *

import title_state


name = "BadEndState"
image = None
logo_time = 0.0


def enter():
    global image
    image = load_image('Resource/Sprites/bg_pause.png')


def exit():
    global image
    image = None

def update(frameTime):
    global logo_time

    if(logo_time > 1.0):
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