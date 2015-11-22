__author__ = '성소윤'

import  json
from math import *
import DrawManager
import StageManager

BulletData = {}
BulletList = []

def GenBulletData() :
    global BulletData
    with open('BulletData.json') as f:
        BulletData = json.load(f)

def Rener():
    global  BulletList
    for i in BulletList :
        i.Render()

def CheckAliveBullet():
    global  BulletList
    for i in BulletList :
        if not i.alive:
            BulletList.remove(i)

def Update(frameTime):
    global  BulletList
    for i in BulletList :
        i.Update(frameTime)
    CheckAliveBullet()

def AddBullet(bullet):
    global BulletList
    BulletList.append(bullet)

class Bullet:
    def __init__(self, x, y, rad, side):
        self.x = x
        self.y = y
        self.radian = rad
        self.travel = 0
        self.alive = True
        self.side = side

    def Update(self,frameTime):
        x, y = self.x, self.y
        self.x += cos(self.radian)*self.speed*frameTime
        self.y += sin(self.radian)*self.speed*frameTime
        self.speed += self.speedRate*frameTime
        self.travel += sqrt((self.x-x)*(self.x -x) + (self.y - y)*(self.y - y))
        print(self.travel)
        self.CheckAlive()

    def Render(self):
        DrawManager.BulletGraphicList[self.name].Draw(self.x, self.y, self.side,self.radian)

    def CheckAlive(self):
        if self.travel >= self.maximumRange or StageManager.MapCollisionCheck(self,0 ,0) :
            self.alive = False

class PistolBullet(Bullet):
    created = False
    name = None
    wCollisionBox, hCollisionBox = None, None
    speed = None
    speedRate = None
    maximumRange = None

    def __init__(self, x, y, rad, side):
        Bullet.__init__(self, x, y, rad, side)
        if not PistolBullet.created :
            PistolBullet.created = True
            PistolBullet.name = 'pistol'
            PistolBullet.speed = BulletData['Pistol']['speed']
            PistolBullet.speedRate = BulletData['Pistol']['speedRates']
            PistolBullet.wCollisionBox = BulletData['Pistol']['collisionBoxWidth']
            PistolBullet.hCollisionBox = BulletData['Pistol']['collisionBoxHeight']
            PistolBullet.maximumRange = BulletData['Pistol']['maximumRange']


class RifleBullet(Bullet):
    created = False
    name = None
    wCollisionBox, hCollisionBox = None, None
    speed = None
    speedRate = None
    maximumRange = None

    def __init__(self, x, y, rad, side):
        Bullet.__init__(self, x, y, rad, side)
        if not RifleBullet.created :
            RifleBullet.created = True
            RifleBullet.name = 'rifle'
            RifleBullet.speed = BulletData['Rifle']['speed']
            RifleBullet.speedRate = BulletData['Rifle']['speedRates']
            RifleBullet.wCollisionBox = BulletData['Rifle']['collisionBoxWidth']
            RifleBullet.hCollisionBox = BulletData['Rifle']['collisionBoxHeight']
            RifleBullet.maximumRange = BulletData['Rifle']['maximumRange']

class SniperBullet(Bullet):
    created = False
    name = None
    wCollisionBox, hCollisionBox = None, None
    speed = None
    speedRate = None
    maximumRange = None

    def __init__(self, x, y, rad, side):
        Bullet.__init__(self, x, y, rad, side)
        if not SniperBullet.created :
            SniperBullet.created = True
            SniperBullet.name = 'sniper'
            SniperBullet.speed = BulletData['Sniper']['speed']
            SniperBullet.speedRate = BulletData['Sniper']['speedRates']
            SniperBullet.wCollisionBox = BulletData['Sniper']['collisionBoxWidth']
            SniperBullet.hCollisionBox = BulletData['Sniper']['collisionBoxHeight']
            SniperBullet.maximumRange = BulletData['Sniper']['maximumRange']


class BossBullet(Bullet):
    created = False
    name = None
    wCollisionBox, hCollisionBox = None, None
    speed = None
    speedRate = None
    maximumRange = None

    def __init__(self, x, y, rad, side):
        Bullet.__init__(self, x, y, rad, side)
        if not BossBullet.created :
            BossBullet.created = True
            BossBullet.name = 'boss'
            BossBullet.speed = BulletData['Boss']['speed']
            BossBullet.speedRate = BulletData['Boss']['speedRates']
            BossBullet.wCollisionBox = BulletData['Boss']['collisionBoxWidth']
            BossBullet.hCollisionBox = BulletData['Boss']['collisionBoxHeight']
            BossBullet.maximumRange = BulletData['Boss']['maximumRange']