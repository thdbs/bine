__author__ = '성소윤'

import Camera
import DrawManager
from pico2d import *
from Item import Portal

import Bullet
import CoinManager
import EffectManager
from Item import *
import SoundManager
happy_end = False


StageDataList = {}
curStage = None
MonsterList = {}
PortalList = {}
PortalState = {}
PortalEffect = None
ShopItemList = []
miniMapX = 900
miniMapY = 10
fireframe = 0
fireframeTimer = 0
bgmList = {}

def Init():
    global StageDataList, curStage, MonsterList, PortalList, PortalState, PortalEffect, ShopItemList, miniMapX, miniMapY, fireframe, fireframeTimer, happy_end, bgmList
    bgmList[curStage].stop()
    StageDataList = {}
    curStage = None
    MonsterList = {}
    PortalList = {}
    PortalState = {}
    PortalEffect = None
    ShopItemList = []
    miniMapX = 900
    miniMapY = 10
    fireframe = 0
    fireframeTimer = 0
    happy_end = False
    bgmList = {}

class Pos:
    def __init__(self, x, y):
        self.x = x
        self.y = y

pos = Pos(0, 0)

def ChangeStage(player, goTo ):
    global curStage, StageDataList, miniMapX, happy_end, bgmList
    if goTo == 'shop':
        PortalList['shop'][0].goTo = curStage
    if curStage == 'stage2_exit' and goTo == 'stage2_exit':
        happy_end = True
        curStage = goTo
        return
    if curStage != goTo:
        Bullet.BulletList.clear()
        CoinManager.coinList.clear()
        EffectManager.EffectList.clear()
    curStage = goTo
    bgmList[curStage].repeat_play()
    player.x = StageDataList[curStage]['inTeleportX']
    player.y = StageDataList[curStage]['inTeleportY'] + 30
    Camera.SetPos(player.x, player.y)
    EffectManager.CallEffect('chStage', pos , False)
    if curStage == 'stage2_exit': miniMapX = 700
    else : miniMapX = 900

def MiniMapRender(x, y , r,g,b):
    global miniMapX, miniMapY, curStage
    drawX = miniMapX + (x/10)*(7/10)
    drawY = miniMapY + (y/10)*(7/10)
    draw_rectangle(drawX -2, drawY, drawX+2, drawY+4, r, g, b, True)

def GenStageData() :
    global StageDataList, curStage, MonsterList, PortalList, PortalState, ShopItemList, bgmList
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
    PortalList['stage1_1'] = []
    PortalList['stage1_2'] = []
    PortalList['shop'] = []
    PortalList['stage2_boss'] = []
    PortalList['stage2_exit'] = []
    PortalList['stage1_1'].append(Portal(StageDataList['stage1_1']['inTeleportX'], StageDataList['stage1_1']['inTeleportY'], 'stage1_1', True))
    PortalList['stage1_1'].append(Portal(StageDataList['stage1_1']['outTeleportX'], StageDataList['stage1_1']['outTeleportY'], 'stage1_2', False))
    PortalList['stage1_1'].append(Portal(StageDataList['stage1_1']['inTeleportX'] + 100, StageDataList['stage1_1']['inTeleportY'], 'shop', True))
    PortalList['stage1_2'].append(Portal(StageDataList['stage1_2']['inTeleportX'], StageDataList['stage1_2']['inTeleportY'], 'stage1_1', True))
    PortalList['stage1_2'].append(Portal(StageDataList['stage1_2']['outTeleportX'], StageDataList['stage1_2']['outTeleportY'], 'stage2_boss', False))
    PortalList['stage1_2'].append(Portal(StageDataList['stage1_2']['inTeleportX'] - 100, StageDataList['stage1_2']['inTeleportY'], 'shop', True))
    PortalList['stage2_boss'].append(Portal(StageDataList['stage2_boss']['inTeleportX'], StageDataList['stage2_boss']['inTeleportY'], 'stage1_2', True))
    PortalList['stage2_boss'].append(Portal(StageDataList['stage2_boss']['outTeleportX'], StageDataList['stage2_boss']['outTeleportY'], 'stage2_exit', False))
    PortalList['stage2_boss'].append(Portal(StageDataList['stage2_boss']['inTeleportX'] + 100, StageDataList['stage2_boss']['inTeleportY'], 'shop', True))
    PortalList['stage2_exit'].append(Portal(StageDataList['stage2_exit']['inTeleportX'], StageDataList['stage2_exit']['inTeleportY'], 'stage2_boss', True))
    PortalList['stage2_exit'].append(Portal(StageDataList['stage2_exit']['outTeleportX'], StageDataList['stage2_exit']['outTeleportY'], 'stage2_exit', False))
    PortalList['stage2_exit'].append(Portal(StageDataList['stage2_exit']['inTeleportX'] + 100, StageDataList['stage2_exit']['inTeleportY'], 'shop', True))
    PortalList['shop'].append(Portal(StageDataList['shop']['inTeleportX'], StageDataList['shop']['inTeleportY'], 'shop', True))
    PortalState['stage1_1'] = 'sleep'
    PortalState['stage1_2'] = 'sleep'
    PortalState['shop'] = 'create'
    PortalState['stage2_boss'] = 'sleep'
    PortalState['stage2_exit'] = 'sleep'
    ShopItemList.append(PistolItem(1106, 920))
    ShopItemList.append(RifleItem(1221, 920))
    ShopItemList.append(SniperItem(1338, 920))
    ShopItemList.append(HealthItem(1470, 930))
    bgmList['stage1_1'] = load_music('Resource/Sound/bgm_stage1.mp3')
    bgmList['stage1_1'].set_volume(64)
    bgmList['stage1_2'] = load_music('Resource/Sound/bgm_stage2.mp3')
    bgmList['stage1_2'].set_volume(64)
    bgmList['stage2_boss'] = load_music('Resource/Sound/bgm_stage3.mp3')
    bgmList['stage2_boss'].set_volume(64)
    bgmList['stage2_exit'] = load_music('Resource/Sound/bgm_stage4.mp3')
    bgmList['stage2_exit'].set_volume(64)
    bgmList['shop'] = load_music('Resource/Sound/bgm_shop.mp3')
    bgmList['shop'].set_volume(64)
    bgmList[curStage].repeat_play()

def Render():
    global curStage, MonsterList, PortalList, StageDataList, ShopItemList, fireframe, fireframeTimer

    DrawManager.StageGraphicList[curStage].Draw()

    for row in range(len(StageDataList[curStage]['data'])):
        for col in range(len(StageDataList[curStage]['data'][row])):
            data = int(GetMapDate(row, col))
            if 1 < data and data <= 300:
                cx, cy, w, h = GetTileData(row, col)
                if data < 100: DrawManager.BackObjectGraphicList['dangerBox'].Draw(cx, cy)
                elif data < 200: DrawManager.BackObjectGraphicList['notGoodBox'].Draw(cx, cy)
                else: DrawManager.BackObjectGraphicList['goodBox'].Draw(cx, cy)
            elif 300 < data and data <= 600:
                cx, cy, w, h = GetTileData(row, col)
                if data < 400: DrawManager.BackObjectGraphicList['dangerRock'].Draw(cx, cy)
                elif data < 500: DrawManager.BackObjectGraphicList['notGoodRock'].Draw(cx, cy)
                else: DrawManager.BackObjectGraphicList['goodRock'].Draw(cx, cy)


    for i in PortalList[curStage] :
        i.render()
    for i in MonsterList[curStage] :
        i.Render()

    if curStage == 'shop':
        for i in ShopItemList:
            i.render()
    if curStage == 'stage2_exit':
        DrawManager.EffectGraphicList['fire'].Draw(100 + Camera.x, 0 + Camera.y, fireframe )
        DrawManager.EffectGraphicList['fire'].Draw(80 + Camera.x, 100 + Camera.y, (fireframe+2)%15 )
        DrawManager.EffectGraphicList['fire'].Draw(110 + Camera.x, 200 + Camera.y, (fireframe+4)%15 )
        DrawManager.EffectGraphicList['fire'].Draw( 70 + Camera.x, -100 + Camera.y, (fireframe+8)%15 )
        DrawManager.EffectGraphicList['fire'].Draw( 120 + Camera.x, 300 + Camera.y, (fireframe+10)%15 )
        DrawManager.EffectGraphicList['fire'].Draw( 120 + Camera.x, -200 + Camera.y, (fireframe+12)%15 )
        DrawManager.EffectGraphicList['fire'].Draw( 90 + Camera.x, 250 + Camera.y, (fireframe+14)%15 )
        DrawManager.EffectGraphicList['fire'].Draw( 120 + Camera.x, 350 + Camera.y, (fireframe+1)%15 )




def Update(frameTime):
    global curStage, MonsterList, PortalList, PortalState, PortalEffect, pos, fireframeTimer, fireframe
    for i in MonsterList[curStage] :
        i.Update(frameTime)
    for i in MonsterList[curStage] :
        if not i.alive:
            MonsterList[curStage].remove(i)
    if len(MonsterList[curStage]) == 0 and PortalState[curStage] == 'sleep':
        PortalState[curStage] = 'createState'
        PortalEffect = EffectManager.CallEffect('genPortal', PortalList[curStage][1], False)
    if PortalEffect != None and PortalEffect.end == True :
        PortalEffect = None
        PortalList[curStage][1].active = True
    pos.x = Camera.x + Camera.w/2
    pos.y = Camera.y
    if curStage == 'stage2_exit':
        Camera.offsetX += 5
        Camera.Move(5, 0)
        fireframeTimer += frameTime
        if(fireframeTimer >= DrawManager.frame_Interval):
            increaseRate = int(fireframeTimer / DrawManager.frame_Interval)
            fireframe = (fireframe + increaseRate) % 15
            fireframeTimer = 0


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

def BulletMapCollisionCheck(bullet, shiftX, shiftY):
    global StageDataList, curStage
    row = int((StageDataList[curStage]['tileHeight']*StageDataList[curStage]['height'] - (bullet.y + shiftY)) / StageDataList[curStage]['tileHeight'])
    rightCol = int((bullet.x + (bullet.wCollisionBox/2) + shiftX) / StageDataList[curStage]['tileWidth'])
    leftCol = int((bullet.x - (bullet.wCollisionBox/2) + shiftX) / StageDataList[curStage]['tileWidth'])
    if GetMapDate(row, rightCol) != '0' :
        data = int(GetMapDate(row, rightCol))
        if 1 < data and data <= 300:
            data -= bullet.hit
            print(data)
            cx, cy, w, h = GetTileData(row, rightCol)
            if data < 100: EffectManager.CallEffect('dangerBox_hit', None, False, True, cx, cy)
            elif data < 200: EffectManager.CallEffect('notGoodBox_hit', None, False, True, cx, cy)
            else: EffectManager.CallEffect('goodBox_hit', None, False, True, cx, cy)
            if data <= 1:
                data = 0
                EffectManager.CallEffect('box_break', None, False, True, cx, cy)
                SoundManager.CallEffectSound('debris')
            value = str('%d' %data)
            StageDataList[curStage]['data'][row][rightCol] = value
        elif 300 < data and data <= 600:
            data -= bullet.hit
            cx, cy, w, h = GetTileData(row, rightCol)
            if data < 400: EffectManager.CallEffect('dangerRock_hit', None, False, True, cx, cy)
            elif data < 500: EffectManager.CallEffect('notGoodRock_hit', None, False, True, cx, cy)
            else: EffectManager.CallEffect('goodRock_hit', None, False, True, cx, cy)
            if data <= 300:
                data = 0
                EffectManager.CallEffect('rock_break', None, False, True, cx, cy)
                SoundManager.CallEffectSound('debris')
            value = str('%d' %data)
            StageDataList[curStage]['data'][row][rightCol] = value
        return True
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