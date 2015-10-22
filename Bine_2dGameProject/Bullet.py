__author__ = '성소윤'

from math import *
import Camera
from Graphic import *
import Stage

class Bullet:
    def __init__(self, x, y, rad, speedRate, width, height):
        self.x = x
        self.y = y
        self.radian = rad

        self.speed = 10
        self.speedRate = speedRate

        self.alive = True

        self.width =width
        self.height = height

    def Update(self):
        self.x += cos(self.radian)*self.speed
        self.y += sin(self.radian)*self.speed
        self.speed += self.speedRate

        self.CheckAlive()

    def Render(self):
        pass

    def CheckAlive(self):
        x = self.x- Camera.xPos
        y = self.y- Camera.yPos

        if x - self.width/2 > Camera.width or x + self.width/2 < 0 or y - self.height/2 > Camera.height or y + self.height/2 < 0 \
                or Stage.GetMapDate(int((128*17 - self.y )/128), int(self.x/128)) is not '0':
            self.alive = False


class ShotGunBullet(Bullet):
    def __init__(self, x, y, rad, speedRate, width, height):
        Bullet.__init__(self, x, y, rad, speedRate, width, height)

    def Render(self):
        global BulletGraphicMap
        x = self.x- Camera.xPos
        y = self.y- Camera.yPos
        BulletGraphicMap['ShotGun'].draw(x, y)

