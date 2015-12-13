__author__ = '성소윤'

from math import *
import DrawManager
import Action
import SoundManager

coinList = []

def Init():
    global coinList
    coinList = []

def AddCoin(x, y):
    coinList.append(Coin(x, y))

def Render():
    global coinList
    for i in coinList:
        i.render()

def Update(frameTime, player):
    global coinList
    for i in coinList: i.update(frameTime, player)
    for i in coinList :
        if i.eaten : coinList.remove(i)

class Coin:
    hCollisionBox = 20
    wCollisionBox = 20

    def __init__(self, x, y):
        self.x = x
        self.y = y
        self.drop = True
        self.frame = 0
        self.frameTimer = 0
        self.eaten = False
        self.dirX, self.dirY = 0, 0

    def render(self):
        if self.drop : DrawManager.ItemGraphicList['coin_drop'].Draw(self.x, self.y, self.frame)
        else : DrawManager.ItemGraphicList['coin'].Draw(self.x, self.y, self.frame)

    def update(self, frameTime, player):
        if self.drop:
            if Action.actionList['increaseFrameOncePrime'].update(self, frameTime, 'Item', 'coin_drop'):
                self.drop = False
                self.frame = 0
                self.frameTimer = 0
        else:
            Action.actionList['increaseFramePrime'].update(self, frameTime, 'Item', 'coin')
            len = sqrt((self.x - player.x)*(self.x - player.x) +
                       ((self.y + self.hCollisionBox/2) - (player.y + player.hCollisionBox/2))*((self.y + self.hCollisionBox/2) - (player.y + player.hCollisionBox/2)))
            if len < 150.0 :
                self.dirX = (player.x - self.x)/len
                self.dirY = ((player.y + player.hCollisionBox/2) - (self.y + self.hCollisionBox/2))/len
            self.x += self.dirX*5
            self.y += self.dirY*5
            if player.CollisionCheck(self) :
                self.eaten = True
                SoundManager.CallEffectSound('coin')
                player.coin += 1