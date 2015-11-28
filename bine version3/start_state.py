import game_framework
from pico2d import *

import MainState


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(1280, 720)
    game_framework.font = load_font('Resource/wendy.ttf', 30)
    game_framework.bigfont = load_font('Resource/wendy.ttf', 60)
    image = load_image('Resource/Sprites/kpu_credit.png')
    hide_cursor()


def exit():
    global image
    del(image)
    close_canvas()


def update(frameTime):
    global logo_time

    if(logo_time > 1.0):
        logo_time = 0.0
        game_framework.push_state(MainState)
    delay(0.01)
    logo_time += 0.01



def draw():
    global image
    clear_canvas()
    image.draw(640, 360)
    update_canvas()




def handle_events():
    events = get_events()
    pass


def pause(): pass


def resume(): pass




