__author__ = '성소윤'
from pico2d import *

PlayerGraphicMap = {}
WeaponGraphicMap = {}
BulletGraphicMap = {}

class Animation:
    def __init__(self, image, width, height):
        self.image = image
        self.width = width
        self.height = height

    def Draw(self, x, y, frame ):
        self.image.clip_draw( frame*self.width,0, self.width, self.height, x, y )


def InitMainStateGraphic(): #Call By mainState
    global PlayerGraphicMap, WeaponGraphicMap, BulletGraphicMap
    #Player Sprite Load
    PrIdle = load_image('Resource/Player/spr_jimmy_idle_right.png')
    PlayerGraphicMap["RightIde"] = Animation(PrIdle, 114, 94)
    PlIdle = load_image('Resource/Player/spr_jimmy_idle_left.jpg')
    PlayerGraphicMap["LeftIdle"] = Animation(PlIdle, 114, 94)
    PrRun = load_image('Resource/Player/spr_jimmy_sprint_right.png')
    PlayerGraphicMap["RightRun"] = Animation(PrRun, 114, 94)
    PlRun = load_image('Resource/Player/spr_jimmy_sprint_left.jpg')
    PlayerGraphicMap["LeftRun"] = Animation(PlRun, 114, 94)

    #WeaponImageLoad
    rShotGun = load_image('Resource/Weapon/spr_shotgun_heavy_right.png')
    WeaponGraphicMap["ShotGunRight"] = rShotGun
    lShotGun = load_image('Resource/Weapon/spr_shotgun_heavy_left.png')
    WeaponGraphicMap["ShotGunLeft"] = lShotGun

    #BulletImageLoad
    shotGunBullet = load_image('Resource/Weapon/spr_shotgun_bullet.png')
    BulletGraphicMap["ShotGun"] = shotGunBullet


