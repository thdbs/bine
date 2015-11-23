__author__ = '성소윤'

import json
from pico2d import *
import InputManager
import random
import PlayerState
from Arms import *
import Action

character_data = {}


def GenCharaterData():
    global character_data
    with open('characterData.json') as f:
        character_data = json.load(f)


class Character:
    def __init__(self, x, y, max_health, max_shield):
        self.x, self.y = x, y
        self.vx, self.vy = 0, 0
        self.health = max_health
        self.shield = max_shield
        self.frame, self.frameTimer = 0, 0
        self.stateName = 'idle'
        self.hit = False
        if random.randint(0, 100) < 50 : self.side = True
        else : self.side = False

    def Update(self, frameTime):
        self.state.update(self, frameTime)
        if not self.hit :
            Character.CheckHit(self)

    def Render(self):
        self.state.render(self)
        if self.hit :
            pass


    def ChangeState(self, state, stateName):
        self.state = state
        self.stateName = stateName
        self.frame, self.frameTimer = 0, 0

    def CheckHit(self):
        pass


class Jimmy(Character):
    created = False
    name = None
    maxHealth = None
    maxShield = None
    wCollisionBox, hCollisionBox  = None, None
    WALK_SPEED_PPS = None
    DASH_SPEED_PPS = None
    dashTime = None
    meleeTime = None
    def __init__(self, x, y):
        if not Jimmy.created:
            Jimmy.created = True
            Jimmy.name = character_data['Jimmy']['name']
            Jimmy.maxHealth = character_data['Jimmy']['maxHealth']
            Jimmy.maxShield = character_data['Jimmy']['maxShield']
            Jimmy.wCollisionBox, Jimmy.hCollisionBox  = character_data['Jimmy']['collisionBoxWidth'], character_data['Jimmy']['collisionBoxWidth']
            Jimmy.WALK_SPEED_PPS = character_data['Jimmy']['walkSpeedPPS']
            Jimmy.DASH_SPEED_PPS = character_data['Jimmy']['dashSpeedPPS']
            Jimmy.dashTime = character_data['Jimmy']['dashTime']
            Jimmy.meleeTime = character_data['Jimmy']['meleeTime']
        Character.__init__(self, x, y, Jimmy.maxHealth, Jimmy.maxShield)
        self.state = PlayerState.stateList["Jimmy_idle"]
        self.dash = False
        self.dashTimer = 0
        self.ArmsNameList = ['Pistol', 'Rifle', 'Sniper']
        self.curArm = 1
        self.ArmsList = {}
        self.ArmsList['Sniper'] = SniperGun('Jimmy')
        self.ArmsList['Rifle'] = Rifle('Jimmy')
        self.ArmsList['Pistol'] = Pistol('Jimmy')
        self.shot = False
        self.meleeTimer = 0
        self.activeAttack = False

    def Update(self, frameTime):
        self.PrcessInput()
        Character.Update(self, frameTime)
        if self.shot :
            self.ArmsList[self.ArmsNameList[self.curArm]].Shoot(self,InputManager.mouseX + Camera.x - self.x, InputManager.mouseY + Camera.y - self.y - self.hCollisionBox/2 )

    def Render(self):
        Character.Render(self)
        if not self.activeAttack : self.ArmsList[self.ArmsNameList[self.curArm]].Render(self, InputManager.mouseX + Camera.x - self.x, InputManager.mouseY + Camera.y - self.y - self.hCollisionBox/2, InputManager.mouseX + Camera.x,InputManager.mouseY + Camera.y )
        else : self.ArmsList[self.ArmsNameList[self.curArm]].Render(self, self.vx , self.vy - 100, self.x, self.y + self.hCollisionBox/2 )

    def PrcessInput(self):
        if not self.dash and not self.activeAttack :
            if (InputManager.GetKeyState(SDLK_w) == InputManager.GetKeyState(SDLK_s)) :
                self.vy = 0
            elif InputManager.GetKeyState(SDLK_w):
                self.vy = Jimmy.WALK_SPEED_PPS
            elif InputManager.GetKeyState(SDLK_s):
                self.vy = -Jimmy.WALK_SPEED_PPS
            if (InputManager.GetKeyState(SDLK_a) == InputManager.GetKeyState(SDLK_d)) :
                self.vx = 0
            elif InputManager.GetKeyState(SDLK_a):
                self.vx = -Jimmy.WALK_SPEED_PPS
            elif InputManager.GetKeyState(SDLK_d):
                self.vx = Jimmy.WALK_SPEED_PPS
            if((InputManager.GetKeyState(SDLK_LSHIFT) or InputManager.GetKeyState(SDLK_RSHIFT)) and (self.vx != 0 or self.vy != 0)):
                self.dash = True
                self.vx = self.vx * Jimmy.DASH_SPEED_PPS
                self.vy = self.vy * Jimmy.DASH_SPEED_PPS
            if (InputManager.GetKeyState(SDLK_f)) :
                dirx = InputManager.mouseX + Camera.x - self.x
                diry = InputManager.mouseY + Camera.y - self.y - self.hCollisionBox/2
                dirx, diry = Action.Nomalization(dirx, diry)
                self.vx = dirx * Jimmy.WALK_SPEED_PPS
                self.vy = diry * Jimmy.WALK_SPEED_PPS
                self.ChangeState(PlayerState.stateList['Jimmy_melee'], 'melee')
        if InputManager.GetKeyState(SDLK_q) : self.curArm = (self.curArm + 1) %3
        if InputManager.LButton : self.shot = True
        else : self.shot = False