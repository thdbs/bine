__author__ = '성소윤'

from pico2d import *
import Camera

StageDataMap = {}
StageImageMap = {}
nowStage = None

class Size:
    def __init__(self, right, bottom, width, height):
        self.right = right
        self.bottom = bottom
        self.width = width
        self.height = height

def LoadStageData():
    global StageDataMap
    arr11 = []
    f = open('Resource/Stage/stage1_room1.txt','r')
    lines = f.readlines()
    for line in lines:
        list = line.split()
        arr11.append(list)

    StageDataMap["Stage1Room1"] = arr11

    f.close()

def LoadStageImage():
    global StageImageMap
    Stage1R1image = load_image('Resource/Stage/stage1_room1.png')
    StageImageMap["Stage1Room1"] = Stage1R1image


def Draw():
    global StageImageMap, nowStage
    StageImageMap[nowStage].clip_draw( int(Camera.xPos),int(Camera.yPos), int(Camera.width), int(Camera.height), int(Camera.width/2), int(Camera.height/2) )

def SetNowStage(stage):
    global nowStage
    nowStage = stage

def GetMapDate(row, col):
    global StageDataMap,nowStage
    return(StageDataMap[nowStage][row][col])


def MapCollisionCheck(charcter, shiftX, shiftY):