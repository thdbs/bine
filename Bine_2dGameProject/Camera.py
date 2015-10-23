__author__ = '성소윤'
import Stage
width, height = 1280, 720
xPos, yPos = 797 - width/2, 935 - height/2

def Update(xShift, yShift):
    global xPos, yPos
    xPos += xShift
    yPos += yShift
