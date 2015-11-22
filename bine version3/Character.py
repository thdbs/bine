__author__ = '성소윤'

import State
import json
from pico2d import *
import InputManager

character_data = None

def GenCharaterData():
    global character_data
    if(Character == None):
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

    def Update(self, frameTime):
        self.state.update(self, frameTime)
        if not self.hit :
            Character.CheckHit(self)

    def Render(self):
        self.state.render(self)
        if self.hit :


    def ChangeState(self, state, stateName):
        self.state = state
        self.stateName = stateName
        self.frame, self.frameTimer = 0, 0

    def CheckHit(self):


class Jimmy(Character):
    created = False
    name = None
    maxHealth = None
    maxShield = None
    wCollisionBox, hCollisionBox  = None, None
    WALK_SPEED_PPS = None
    DASH_SPEED_PPS = None
    dashTime = None
    def __init__(self, x, y):
        if not Jimmy.created:
            Jimmy.created = True
            Jimmy.name = character_data['Jimmy']['name']
            Jimmy.maxHealth = character_data['Jimmy']['maxHealth']
            Jimmy.maxShield = character_data['Jimmy']['maxSheild']
            Jimmy.wCollisionBox, Jimmy.hCollisionBox  = character_data['Jimmy']['collisionBoxWidth'], character_data['Jimmy']['collisionBoxWidth']
            Jimmy.WALK_SPEED_PPS = character_data['Jimmy']['walkSpeedPPS']
            Jimmy.DASH_SPEED_PPS = character_data['Jimmy']['dashSpeedPPS']
            Jimmy.dashTime = character_data['Jimmy']['dashTime']
        Character.__init__(x, y, Jimmy.maxHealth, Jimmy.maxShield)
        self.state = State.stateList['Jimmy_idle']
        self.dash = False
        self.dashTimer = 0

    def PrcessInput(self):
        if (InputManager.KekUp('w') and InputManager.KeyUp('s'))\
                or (InputManager.KekDown('w') and InputManager.KeyDow('s')):
            self.vy = 0
        elif InputManager.KeyDown('w'):
            self.vy = Jimmy.WALK_SPEED_PPS
        elif InputManager.KeyDown('s'):
            self.vy = -Jimmy.WALK_SPEED_PPS
        if (InputManager.KekUp('a') and InputManager.KeyUp('d'))\
                or (InputManager.KekDown('a') and InputManager.KeyDow('d')):
            self.vx = 0
        elif InputManager.KeyDown('a'):
            self.vx = -Jimmy.WALK_SPEED_PPS
        elif InputManager.KeyDown('d'):
            self.vx = Jimmy.WALK_SPEED_PPS
        if(InputManager.KeyDown('shift') and (not self.dash)
           and (self.vx != 0 or self.vy != 0)):
            self.dash = True
            self.vx = self.vx * Jimmy.DASH_SPEED_PPS
            self.vy = self.vy * Jimmy.DASH_SPEED_PPS
