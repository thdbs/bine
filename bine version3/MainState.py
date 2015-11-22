__author__ = '성소윤'

import random
import json
import os

from pico2d import *
import game_framework
from Character import *
import Bullet
import InputManager
import GenData
import StageManager

name = "MainState"

jimmy = None
MonsterList = []

def enter():
    global jimmy
    GenData.GenData()
    jimmy = Jimmy(StageManager.StageDataList[StageManager.curStage]['inTeleportX'] ,StageManager.StageDataList[StageManager.curStage]['inTeleportY'])

def exit():
    global jimmy
    del(jimmy)

def pause():
    pass


def resume():
    pass


def handle_events():
    global running
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN:
            InputManager.KeyDown(event.key)
            if event.key == SDLK_ESCAPE:
                game_framework.quit()
        elif event.type == SDL_KEYUP:
            InputManager.KeyUp(event.key)
        elif event.type == SDL_MOUSEMOTION:
            InputManager.mouseX, InputManager.mouseY = event.x, 720 - event.y
        elif event.type == SDL_MOUSEBUTTONDOWN:
            if event.button == SDL_BUTTON_LEFT:
                InputManager.LButton = True
            elif event.button == SDL_BUTTON_RIGHT:
                InputManager.RButton = True
        elif event.type == SDL_MOUSEBUTTONUP:
            if event.button == SDL_BUTTON_LEFT:
                InputManager.LButton = False
            elif event.button == SDL_BUTTON_RIGHT:
                InputManager.RButton = False



def update(frameTime):
    global jimmy
    Bullet.Update(frameTime)
    jimmy.Update(frameTime)
    delay(0.01)


def draw():
    global jimmy
    clear_canvas()
    StageManager.Render()
    Bullet.Rener()
    jimmy.Render()
    update_canvas()