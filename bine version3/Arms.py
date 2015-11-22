__author__ = '성소윤'

from Bullet import *
import DrawManager
from math import *
import random
import Camera
from pico2d import *
import InputManager

PistolPermitedError = 15
RiflePermitedError = 20
SniperPermitedError = 0

class Gun:
    def Shoot(self, owner):
        pass

    def Render(self, owner, dirX, dirY, targetX, targetY):
        rad = atan2(dirY, dirX)
        side = None
        if(dirX >=0 ) : side = True
        else :
            side = False
            rad += 3.14
        str = self.owner_name + '_' + self.name
        DrawManager.ArmsGraphicList[str].Draw(owner.x, owner.y + owner.hCollisionBox/2, side, rad)


class Pistol(Gun):
    name = None
    def __init__(self, owner_name):
        if Pistol.name == None : Pistol.name = 'pistol'
        self.owner_name = owner_name

    def Shoot(self, owner, dirX, dirY):
        owner.shot = False
        InputManager.LButton = False
        rad = atan2(dirY, dirX)
        side = None
        if(dirX >= 0 ) : side = True
        else : side = False
        AddBullet(PistolBullet(owner.x, owner.y + owner.hCollisionBox/2, rad + (random.randint(-PistolPermitedError,PistolPermitedError)/180.0)*3.14,side))


class Rifle(Gun):
    name = None
    def __init__(self, owner_name):
        if Rifle.name == None : Rifle.name = 'rifle'
        self.owner_name = owner_name

    def Shoot(self, owner, dirX, dirY):
        rad = atan2(dirY, dirX)
        side = None
        if(dirX >= 0 ) : side = True
        else : side = False
        AddBullet(RifleBullet(owner.x, owner.y + owner.hCollisionBox/2, rad + (random.randint(-RiflePermitedError,RiflePermitedError)/180.0)*3.14,side))


class SniperGun(Gun):
    name = None
    def __init__(self, owner_name):
        if SniperGun.name == None : SniperGun.name = 'sniper'
        self.owner_name = owner_name

    def Shoot(self, owner, dirX, dirY):
        owner.shot = False
        InputManager.LButton = False
        rad = atan2(dirY, dirX)
        side = None
        if(dirX >= 0 ) : side = True
        else : side = False
        AddBullet(SniperBullet(owner.x, owner.y + owner.hCollisionBox/2, rad + (random.randint(-SniperPermitedError,SniperPermitedError)/180.0)*3.14,side))

    def Render(self, owner, dirX, dirY, targetX, targetY):
        x1, y1 = int(owner.x - Camera.x), int(owner.y - Camera.y + owner.hCollisionBox/2)
        x2, y2 = int(targetX - Camera.x), int(targetY - Camera.y)
        draw_line(x1, y1, x2, y2)
        Gun.Render(self, owner, dirX, dirY, targetX, targetY)

class BossGun(Gun):
    pass