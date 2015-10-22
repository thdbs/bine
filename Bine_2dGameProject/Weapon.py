__author__ = '성소윤'

from Graphic import *
from pico2d import *
import InputManager
import Camera
from math import *
import BulletManager
from Bullet import *

class Gun:
    def __init__(self):
        pass
    def Shot(self):
        pass
    def Render(self):
        pass

class ShotGun(Gun):
    def __init__(self):
        pass
    def Shot(self, x, y):
        rad = atan2(InputManager.mouseY-(y- Camera.yPos + 20), InputManager.mouseX - (x- Camera.xPos))
        bullet = ShotGunBullet(x + cos(rad)* 10, y +20 + sin(rad) * 10, rad, 0, 14, 14)
        BulletManager.AddBullet(bullet)

    def Render(self,x,y):
        global WeaponGraphicMap
        x = x- Camera.xPos
        y = y- Camera.yPos + 20
        if InputManager.mouseX >=640:
            rad = atan2(InputManager.mouseY-y, InputManager.mouseX - x)
            WeaponGraphicMap["ShotGunRight"].rotate_draw(rad, x , y)
        else:
            rad = atan2(InputManager.mouseY-y, InputManager.mouseX - x) - 3.14
            WeaponGraphicMap["ShotGunLeft"].rotate_draw(rad, x , y)
