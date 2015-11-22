__author__ = '성소윤'

import DrawManager
import json
import Camera

StageDataList = {}
curStage = None


def GenStageData() :
    global StageDataList, curStage
    curStage = 'stage2_exit'
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


def Render():
    global curStage
    DrawManager.StageGraphicList[curStage].Draw()


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


def ChangeStage():
    pass


def CreateInTeleport():
    pass


def ActiveOutTeleport():
    pass