__author__ = '성소윤'
import game_framework
from pico2d import *

import MainState


name = "TitleState"
image = []
bgm = None
frameTimer = 0
frame = 0


def enter():
    global image, bgm
    image.append(load_image('Resource/Sprites/spr_intro_animated_0.png'))
    image.append(load_image('Resource/Sprites/spr_intro_animated_1.png'))
    image.append(load_image('Resource/Sprites/spr_intro_animated_2.png'))
    image.append(load_image('Resource/Sprites/spr_intro_animated_3.png'))
    image.append(load_image('Resource/Sprites/spr_intro_animated_4.png'))
    image.append(load_image('Resource/Sprites/spr_intro_animated_5.png'))
    image.append(load_image('Resource/Sprites/spr_intro_animated_6.png'))
    image.append(load_image('Resource/Sprites/spr_intro_animated_7.png'))
    image.append(load_image('Resource/Sprites/spr_intro_animated_8.png'))
    image.append(load_image('Resource/Sprites/spr_intro_animated_9.png'))
    image.append(load_image('Resource/Sprites/spr_intro_animated_10.png'))
    image.append(load_image('Resource/Sprites/spr_intro_animated_11.png'))
    bgm = load_music('Resource/Sound/bgm_menu.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

def exit():
    global image, bgm
    image.clear()
    bgm.stop()
    bgm = None

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if(event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif(event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(MainState)



def draw():
    global frame, image
    clear_canvas()
    image[frame].clip_draw(0, 0, 1280, 720, 640, 360 )
    game_framework.bigfont.draw(500, 130, 'Press Space Key', (255, 255, 255))
    update_canvas()


def update(frameTime):
    global frame, frameTimer
    frameTimer += frameTime
    if(frameTimer >= 0.2):
        increaseRate = int(frameTimer / 0.2)
        frame = (frame + increaseRate) % 12
        frameTimer = 0


def pause():
    pass


def resume():
    pass






