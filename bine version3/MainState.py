__author__ = '성소윤'

import random
import json
import os

import start_state

from pico2d import *
import game_framework
from Character import *
from Monster import *
import InputManager
import GenData
import StageManager
import Bullet

name = "MainState"


jimmy = None

def enter():
    global jimmy, MonsterList
    GenData.GenData()
    jimmy = Jimmy(StageManager.StageDataList[StageManager.curStage]['inTeleportX'] ,StageManager.StageDataList[StageManager.curStage]['inTeleportY'])
    StageManager.MonsterList['stage2_exit'].append(Turtle(StageManager.StageDataList['stage2_exit']['inTeleportX'] + 500 ,StageManager.StageDataList['stage2_exit']['inTeleportY'], jimmy))
    StageManager.MonsterList['stage1_1'].append(DashDuck(StageManager.StageDataList['stage1_1']['inTeleportX'] + 500 ,StageManager.StageDataList['stage1_1']['inTeleportY'], jimmy))
    StageManager.MonsterList['stage1_1'].append(Kaze(StageManager.StageDataList['stage1_1']['outTeleportX']  ,StageManager.StageDataList['stage1_1']['outTeleportY'], jimmy))
    StageManager.MonsterList['stage2_boss'].append(SniperDuck(StageManager.StageDataList['stage2_boss']['inTeleportX'] + 500 ,StageManager.StageDataList['stage2_boss']['inTeleportY'], jimmy))


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
    if(frameTime<0.1):
        Bullet.Update(frameTime)
        StageManager.Update(frameTime)
        jimmy.Update(frameTime)
        for i in Bullet.BulletList:
            jimmy.CollisionCheck_Bullet(i)
        for i in StageManager.MonsterList[StageManager.curStage]:
            jimmy.CollisionCheck_Character(i)
        for i in Bullet.BulletList:
            for j in StageManager.MonsterList[StageManager.curStage]:
                j.CollisionCheck_Bullet(i)
        #수정해주기
        if not jimmy.alive:
            delay(0.2)
            game_framework.push_state(start_state)
    delay(0.01)


def draw():
    global jimmy
    clear_canvas()
    StageManager.Render()
    Bullet.Render()
    jimmy.Render()
    update_canvas()