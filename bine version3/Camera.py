__author__ = '성소윤'

w = 1280
h = 720
x = 0
y = 0

def In(drawPointX, drawPointY, width, height) :
    return True

def Move(xShift, yShift) :
    global x, y
    x += xShift
    y += yShift

def SetPos(xPos, yPos) :
    global x, y
    x = xPos - w/2
    y = yPos - h/2