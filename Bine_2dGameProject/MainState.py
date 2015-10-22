__author__ = '성소윤'


import random
import json
import os

from pico2d import *
import game_framework
from Player import *
import Graphic
import InputManager
import Stage
import BulletManager

name = "MainState"

Hero = None
GraphicList = {}

def enter():
    global Hero
    Graphic.InitMainStateGraphic()
    Stage.LoadStageData()
    Stage.LoadStageImage()
    Stage.SetNowStage("Stage1Room1")
    Hero = Player(797, 935, 55, 80)

def exit():
    global  Hero
    del(Hero)

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



def update():
    global Hero
    Hero.Update()
    BulletManager.Update()
    delay(0.01)


def draw():
    global Hero
    clear_canvas()
    Stage.Draw()
    Hero.Render()
    BulletManager.Rener()
    update_canvas()


