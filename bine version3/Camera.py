__author__ = '성소윤'

w = 1280
h = 720
x = 0
y = 0
effect = False
offsetX = 0
offsetY = 0
timer = 0

def Init():
    global x,y,effect,offsetX,offsetY,timer
    x = 0
    y = 0
    effect = False
    offsetX = 0
    offsetY = 0
    timer = 0


def In(drawPointX, drawPointY, width, height) :
    return True

def Move(xShift, yShift) :
    global x, y
    x += xShift
    y += yShift

def SetPos(xPos, yPos) :
    global x, y
    x = xPos - w/2 + offsetX
    y = yPos - h/2 + offsetY

def ShakeCamera():
    global  offsetX, offsetY, timer, effect
    if(effect):
        if timer == 0:
            offsetX += 5
            offsetY += 5
            Move(5, 5)
            timer += 1
            return
        if timer == 1 :
            offsetX -= 5
            offsetY -= 5
            Move(-5, -5)
            timer += 1
            return
        if timer == 2:
            offsetX += 5
            offsetY += 5
            Move(5, 5)
            timer += 1
            return
        if timer == 3 :
            offsetX -= 5
            offsetY -= 5
            Move(-5, -5)
            timer += 1
            return
        if timer == 4:
            effect = False
            timer = 0
            offsetX = 0
            offsetY = 0