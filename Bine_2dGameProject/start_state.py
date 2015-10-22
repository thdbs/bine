import game_framework
from pico2d import *

import MainState


name = "StartState"
image = None
logo_time = 0.0


def enter():
    global image
    open_canvas(1280, 720)
    image = load_image('Resource/kpu_credit.png')


def exit():
    global image
    del(image)
    close_canvas()


def update():
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




