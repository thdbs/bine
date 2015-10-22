__author__ = '성소윤'

from Bullet import *

BulletList = []

def Rener():
    global  BulletList
    for i in BulletList :
        i.Render()

def CheckFrameOutBullet():
    global  BulletList
    for i in BulletList :
        if not i.alive:
            BulletList.remove(i)

def Update():
    global  BulletList
    for i in BulletList :
        i.Update()
    CheckFrameOutBullet()

def AddBullet(bullet):
    global BulletList
    BulletList.append(bullet)
