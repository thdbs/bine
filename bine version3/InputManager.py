__author__ = '성소윤'
from StageManager import Pos
import Camera

keyMap = {}
LButton = False
RButton = False
mouseX, mouseY = 640, 360
mPos = Pos(mouseY + Camera.x, mouseY + Camera.y)


def GetKeyState(key):
    if key in keyMap.keys() and keyMap[key] == True:
        return(True)
    return(False)

def KeyDown(key):
    keyMap[key] = True

def KeyUp(key):
    keyMap[key] = False