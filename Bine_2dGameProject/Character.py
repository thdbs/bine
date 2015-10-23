__author__ = '성소윤'

import Stage

class Character:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.frame = 0
        self.Timer = 0

        self.state = None

        self.ally = True

    def CollisionCheck(self, Object):
        if self.x - self.width/2 < Object.x + Object.width/2 and self.x + self.width/2 > Object.x - Object.width/2 and \
            self.y - self.height/2 < Object.y + Object.height/2 and self.y + self.height/2 > Object.y - Object.height/2 and \
                self.ally is not Object.ally :
            return(True)
        return(False)

    def MapCollisonCheck(self, xShift, yShift):
        if(xShift > 0):
            if Stage.GetMapDate(int((128*17 - (self.y + yShift))/128), int((self.x + self.width/2 + xShift)/128)) is not '0':
                return(True)
        elif(xShift < 0):
            if Stage.GetMapDate(int((128*17 -(self.y + yShift))/128),int((self.x - self.width/2 + xShift)/128)) is not '0':
                return(True)
        elif(yShift > 0):
            if Stage.GetMapDate(int((128*17 -(self.y + yShift + 3))/128), int((self.x + xShift)/128)) is not '0':
                return(True)
        elif(yShift < 0):
            if Stage.GetMapDate(int((128*17 -(self.y + yShift - 1))/128), int((self.x + xShift)/128)) is not '0':
                return(True)
        return(False)


