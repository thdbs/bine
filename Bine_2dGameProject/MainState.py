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
from Monster import *
import random

name = "MainState"

Hero = None
MonsterList = []

def enter():
    global Hero
    Graphic.InitMainStateGraphic()
    Stage.LoadStageData()
    Stage.LoadStageImage()
    Stage.SetNowStage("Stage1Room1")
    Hero = Player(797, 935, 55, 80)
    #Create Monster
    m1 = TurtleMonster(797 + 500 + random.randint(10, 100), 935, 55, 80, Hero)
    MonsterList.append(m1)

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
            #나중에 없애기
            if event.key == SDLK_m:
                m1 = TurtleMonster(797 + 500+ random.randint(10, 500), 935, 55, 80, Hero)
                MonsterList.append(m1)
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
    for i in MonsterList:
        i.Update()
    BulletManager.Update()
    for i in MonsterList:
        for j in BulletManager.BulletList:
            if i.BulletCollisionCheck(j):
                MonsterList.remove(i)
                BulletManager.BulletList.remove(j)
                break
    delay(0.01)


def draw():
    global Hero, MonsterList
    clear_canvas()
    Stage.Draw()
    Hero.Render()
    for i in MonsterList:
        i.Render()
    BulletManager.Rener()
    update_canvas()


