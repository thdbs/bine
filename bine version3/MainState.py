__author__ = '성소윤'

import start_state

import game_framework
import GenData
from Character import *
from Monster import *
import Bullet
import UIManager
from pico2d import *
import CoinManager
import bad_end_state
import happy_end_state


name = "MainState"

jimmy = None
created = False

def enter():
    global jimmy, created
    if not created :
        GenData.GenData()
        created = True
    StageManager.GenStageData()
    jimmy = Jimmy(StageManager.StageDataList[StageManager.curStage]['inTeleportX'] ,StageManager.StageDataList[StageManager.curStage]['inTeleportY'])
    StageManager.MonsterList['stage1_1'].append(DashDuck(StageManager.StageDataList['stage1_1']['inTeleportX'] + 500 ,StageManager.StageDataList['stage1_1']['inTeleportY'], jimmy))
    StageManager.MonsterList['stage1_1'].append(Turtle(StageManager.StageDataList['stage1_1']['outTeleportX']  ,StageManager.StageDataList['stage1_1']['outTeleportY'], jimmy))
    StageManager.MonsterList['stage1_1'].append(Turtle(1517 ,1211, jimmy))
    StageManager.MonsterList['stage1_1'].append(Turtle(1513 ,1127, jimmy))
    StageManager.MonsterList['stage1_1'].append(DashDuck(2017 ,1211, jimmy))
    StageManager.MonsterList['stage1_1'].append(Turtle(2010 ,1099, jimmy))
    StageManager.MonsterList['stage1_1'].append(DashDuck(2237 ,1455, jimmy))
    StageManager.MonsterList['stage1_1'].append(Turtle(2381 ,1463, jimmy))
    StageManager.MonsterList['stage1_1'].append(Turtle(3501 ,1259, jimmy))
    StageManager.MonsterList['stage1_1'].append(DashDuck(3725 ,1119, jimmy))
    StageManager.MonsterList['stage1_1'].append(Turtle(3735 ,1171, jimmy))

    StageManager.MonsterList['stage1_2'].append(DashDuck(StageManager.StageDataList['stage1_2']['inTeleportX'] - 500 ,StageManager.StageDataList['stage1_2']['inTeleportY'], jimmy))
    StageManager.MonsterList['stage1_2'].append(Kaze(857 ,2039, jimmy))
    StageManager.MonsterList['stage1_2'].append(SniperDuck(785 ,1943, jimmy))
    StageManager.MonsterList['stage1_2'].append(Turtle(1265 ,2095, jimmy))
    StageManager.MonsterList['stage1_2'].append(SniperDuck(905 ,1543, jimmy))
    StageManager.MonsterList['stage1_2'].append(DashDuck(849 ,1439, jimmy))
    StageManager.MonsterList['stage1_2'].append(Kaze(1721 ,951, jimmy))
    StageManager.MonsterList['stage1_2'].append(Turtle(2023 ,1967, jimmy))
    StageManager.MonsterList['stage1_2'].append(DashDuck(2145 ,1847, jimmy))
    StageManager.MonsterList['stage1_2'].append(Kaze(2849 ,1415, jimmy))
    StageManager.MonsterList['stage1_2'].append(Kaze(3041 ,1385, jimmy))
    StageManager.MonsterList['stage1_2'].append(DashDuck(2905 ,1247, jimmy))

    StageManager.MonsterList['stage2_boss'].append(SniperDuck(StageManager.StageDataList['stage2_boss']['inTeleportX'] + 500 ,StageManager.StageDataList['stage2_boss']['inTeleportY'], jimmy))
    StageManager.MonsterList['stage2_boss'].append(DashDuck(StageManager.StageDataList['stage2_boss']['inTeleportX'] + 1000 ,StageManager.StageDataList['stage2_boss']['inTeleportY'], jimmy))
    StageManager.MonsterList['stage2_boss'].append(DashDuck(1353,1455, jimmy))
    StageManager.MonsterList['stage2_boss'].append(Turtle(1457,1399, jimmy))
    StageManager.MonsterList['stage2_boss'].append(Turtle(1577,1636, jimmy))
    StageManager.MonsterList['stage2_boss'].append(DashDuck(1665,967, jimmy))
    StageManager.MonsterList['stage2_boss'].append(Boss(2257,1647, jimmy))
    StageManager.MonsterList['stage2_boss'].append(SniperDuck(2773,2231, jimmy))
    StageManager.MonsterList['stage2_boss'].append(Turtle(2877,2343, jimmy))
    StageManager.MonsterList['stage2_boss'].append(DashDuck(2881,1495, jimmy))
    StageManager.MonsterList['stage2_boss'].append(SniperDuck(3041,1511, jimmy))
    StageManager.MonsterList['stage2_boss'].append(SniperDuck(3001,1303, jimmy))



    StageManager.MonsterList['stage2_exit'].append(Turtle(StageManager.StageDataList['stage2_exit']['inTeleportX'] + 500 ,StageManager.StageDataList['stage2_exit']['inTeleportY'], jimmy))
    StageManager.MonsterList['stage2_exit'].append(Turtle(1609 ,1295, jimmy))
    StageManager.MonsterList['stage2_exit'].append(DashDuck(2721 ,855, jimmy))
    StageManager.MonsterList['stage2_exit'].append(Kaze(3297 ,1183, jimmy))
    StageManager.MonsterList['stage2_exit'].append(Turtle(4297 ,1287, jimmy))
    StageManager.MonsterList['stage2_exit'].append(Kaze(4337 ,735, jimmy))
    StageManager.MonsterList['stage2_exit'].append(DashDuck(4881 ,791, jimmy))
    StageManager.MonsterList['stage2_exit'].append(Kaze(3041 ,1111, jimmy))
    StageManager.MonsterList['stage2_exit'].append(Turtle(5533 ,903, jimmy))
    #StageManager.MonsterList['stage2_exit'].append(DashDuck(6897 ,999, jimmy))



def exit():
    global jimmy
    jimmy = None
    Camera.Init()
    StageManager.Init()
    CoinManager.Init()

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
            InputManager.mPos.x, InputManager.mPos.y = event.x + Camera.x, 720 - event.y + Camera.y
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
        EffectManager.Update(frameTime)
        CoinManager.Update(frameTime, jimmy)
        #수정해주기
        if not jimmy.alive:
            delay(0.2)
            game_framework.change_state(bad_end_state)
        if StageManager.happy_end :
            delay(0.2)
            game_framework.change_state(happy_end_state)
    delay(0.01)


def draw():
    global jimmy
    clear_canvas()
    StageManager.Render()
    CoinManager.Render()
    Bullet.Render()
    jimmy.Render()
    EffectManager.Render()
    UIManager.Render()
    # debug_print('test')
    update_canvas()