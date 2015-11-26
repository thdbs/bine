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

def Render():
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
    def __init__(self, x, y, rad, side, ally):
        self.x = x
        self.y = y
        self.radian = rad
        self.travel = 0
        self.alive = True
        self.side = side
        self.ally = ally

    def Update(self,frameTime):
        x, y = self.x, self.y
        self.x += cos(self.radian)*self.speed*frameTime
        self.y += sin(self.radian)*self.speed*frameTime
        self.speed += self.speedRate*frameTime
        self.travel += sqrt((self.x-x)*(self.x -x) + (self.y - y)*(self.y - y))
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
    hit = None

    def __init__(self, x, y, rad, side, ally):
        Bullet.__init__(self, x, y, rad, side, ally)
        if not PistolBullet.created :
            PistolBullet.created = True
            PistolBullet.name = 'pistol'
            PistolBullet.speed = BulletData['Pistol']['speed']
            PistolBullet.speedRate = BulletData['Pistol']['speedRates']
            PistolBullet.wCollisionBox = BulletData['Pistol']['collisionBoxWidth']
            PistolBullet.hCollisionBox = BulletData['Pistol']['collisionBoxHeight']
            PistolBullet.maximumRange = BulletData['Pistol']['maximumRange']
            PistolBullet.hit = BulletData['Pistol']['hit']


class RifleBullet(Bullet):
    created = False
    name = None
    wCollisionBox, hCollisionBox = None, None
    speed = None
    speedRate = None
    maximumRange = None
    hit = None

    def __init__(self, x, y, rad, side, ally):
        Bullet.__init__(self, x, y, rad, side, ally)
        if not RifleBullet.created :
            RifleBullet.created = True
            RifleBullet.name = 'rifle'
            RifleBullet.speed = BulletData['Rifle']['speed']
            RifleBullet.speedRate = BulletData['Rifle']['speedRates']
            RifleBullet.wCollisionBox = BulletData['Rifle']['collisionBoxWidth']
            RifleBullet.hCollisionBox = BulletData['Rifle']['collisionBoxHeight']
            RifleBullet.maximumRange = BulletData['Rifle']['maximumRange']
            RifleBullet.hit = BulletData['Rifle']['hit']

class SniperBullet(Bullet):
    created = False
    name = None
    wCollisionBox, hCollisionBox = None, None
    speed = None
    speedRate = None
    maximumRange = None
    hit = None

    def __init__(self, x, y, rad, side, ally):
        Bullet.__init__(self, x, y, rad, side, ally)
        if not SniperBullet.created :
            SniperBullet.created = True
            SniperBullet.name = 'sniper'
            SniperBullet.speed = BulletData['Sniper']['speed']
            SniperBullet.speedRate = BulletData['Sniper']['speedRates']
            SniperBullet.wCollisionBox = BulletData['Sniper']['collisionBoxWidth']
            SniperBullet.hCollisionBox = BulletData['Sniper']['collisionBoxHeight']
            SniperBullet.maximumRange = BulletData['Sniper']['maximumRange']
            SniperBullet.hit = BulletData['Sniper']['hit']


class BossBullet(Bullet):
    created = False
    name = None
    wCollisionBox, hCollisionBox = None, None
    speed = None
    speedRate = None
    maximumRange = None
    hit = None

    def __init__(self, x, y, rad, side, ally):
        Bullet.__init__(self, x, y, rad, side, ally)
        if not BossBullet.created :
            BossBullet.created = True
            BossBullet.name = 'boss'
            BossBullet.speed = BulletData['Boss']['speed']
            BossBullet.speedRate = BulletData['Boss']['speedRates']
            BossBullet.wCollisionBox = BulletData['Boss']['collisionBoxWidth']
            BossBullet.hCollisionBox = BulletData['Boss']['collisionBoxHeight']
            BossBullet.maximumRange = BulletData['Boss']['maximumRange']
            BossBullet.hit = BulletData['Boss']['hit']