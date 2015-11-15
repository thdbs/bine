__author__ = '성소윤'

keyMap = {}
LButton = False
RButton = False
mouseX, mouseY = 640, 360

def GetKeyState(key):
    if key in keyMap.keys() and keyMap[key] == True:
        return(True)
    return(False)

def KeyDown(key):
    keyMap[key] = True

def KeyUp(key):
    keyMap[key] = False