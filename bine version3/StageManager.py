__author__ = '성소윤'

import DrawManager
import json
import Camera
import DrawManager
from pico2d import *


StageDataList = {}
curStage = None
MonsterList = {}
fireFrame, frameTimer = 0,0

bgm = None

def GenStageData() :
    global StageDataList, curStage, MonsterList, bgm
    bgm = load_music('bgm_stage3.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()
    curStage = 'stage1_1'
    with open('StageData.json') as f:
        StageDataList = json.load(f)
    #text Load
    stage1_1 = []
    f = open('Resource/Sprites/Stage/stage1_room1.txt','r')
    lines = f.readlines()
    for line in lines:
        list = line.split()
        stage1_1.append(list)
    StageDataList["stage1_1"]["data"] = stage1_1
    f.close()
    stage1_2 = []
    f = open('Resource/Sprites/Stage/stage1_room2.txt','r')
    lines = f.readlines()
    for line in lines:
        list = line.split()
        stage1_2.append(list)
    StageDataList["stage1_2"]["data"] = stage1_2
    f.close()
    stage2_boss = []
    f = open('Resource/Sprites/Stage/stage2_boss.txt','r')
    lines = f.readlines()
    for line in lines:
        list = line.split()
        stage2_boss.append(list)
    StageDataList["stage2_boss"]["data"] = stage2_boss
    f.close()
    stage2_exit = []
    f = open('Resource/Sprites/Stage/stage2_exit.txt','r')
    lines = f.readlines()
    for line in lines:
        list = line.split()
        stage2_exit.append(list)
    StageDataList["stage2_exit"]["data"] = stage2_exit
    f.close()
    shop = []
    f = open('Resource/Sprites/Stage/shop.txt','r')
    lines = f.readlines()
    for line in lines:
        list = line.split()
        shop.append(list)
    StageDataList["shop"]["data"] = shop
    f.close()
    Camera.SetPos(StageDataList[curStage]['inTeleportX'], StageDataList[curStage]['inTeleportY'])
    MonsterList['stage1_1'] = []
    MonsterList['stage1_2'] = []
    MonsterList['shop'] = []
    MonsterList['stage2_boss'] = []
    MonsterList['stage2_exit'] = []

def DrawFire():
    global fireFrame, frameTimer
    DrawManager.EffectGraphicList['fire'].Draw(Camera.x + 152  ,Camera.y, fireFrame)
    DrawManager.EffectGraphicList['fire'].Draw(Camera.x + 152  ,Camera.y+300, (fireFrame+ 10)%15)
    DrawManager.EffectGraphicList['fire'].Draw(Camera.x + 152  ,Camera.y+100, (fireFrame+ 2)%15)
    DrawManager.EffectGraphicList['fire'].Draw(Camera.x + 152  ,Camera.y-100, (fireFrame+ 5)%15)
    DrawManager.EffectGraphicList['fire'].Draw(Camera.x + 152  ,Camera.y-200, (fireFrame+ 8)%15)
    frameTimer += 1
    if frameTimer >= 10 :
        frameTimer = 0
        fireFrame = (fireFrame+1)%15

def ChangeState(stageName, player):
    global curStage
    curStage = stageName
    player.x = StageDataList[curStage]['inTeleportX']
    player.y = StageDataList[curStage]['inTeleportY']
    Camera.SetPos(player.x, player.y)

def Render():
    global curStage, MonsterList
    DrawManager.StageGraphicList[curStage].Draw()
    for i in MonsterList[curStage] :
            i.Render()
    if curStage == 'stage2_exit' :  DrawFire()


def Update(frameTime):
    global curStage, MonsterList
    for i in MonsterList[curStage] :
        i.Update(frameTime)
    DrawFire()

def GetMapDate(row, col):
    global StageDataList, curStage
    return StageDataList[curStage]['data'][row][col]


def MapCollisionCheck(charcter, shiftX, shiftY):
    global StageDataList, curStage
    row = int((StageDataList[curStage]['tileHeight']*StageDataList[curStage]['height'] - (charcter.y + shiftY)) / StageDataList[curStage]['tileHeight'])
    rightCol = int((charcter.x + (charcter.wCollisionBox/2) + shiftX) / StageDataList[curStage]['tileWidth'])
    leftCol = int((charcter.x - (charcter.wCollisionBox/2) + shiftX) / StageDataList[curStage]['tileWidth'])
    if GetMapDate(row, rightCol) != '0' : return True
    if GetMapDate(row, leftCol) != '0' : return True
    return False


def GetMyPoistion(x , y):
    global StageDataList, curStage
    row = int((StageDataList[curStage]['tileHeight']*StageDataList[curStage]['height'] - y) / StageDataList[curStage]['tileHeight'])
    col = int( x / StageDataList[curStage]['tileWidth'])
    return row, col

def GetTileData(row, col) :
    global StageDataList, curStage
    cx = col*StageDataList[curStage]['tileWidth'] + StageDataList[curStage]['tileWidth']/2.0
    cy = StageDataList[curStage]['tileHeight']*StageDataList[curStage]['height'] - (row*StageDataList[curStage]['tileHeight'] + StageDataList[curStage]['tileHeight']/2.0)
    w = StageDataList[curStage]['tileWidth']
    h = StageDataList[curStage]['tileHeight']
    return cx, cy, w, h


def CreateInTeleport():
    pass


def ActiveOutTeleport():
    pass