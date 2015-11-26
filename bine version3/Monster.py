__author__ = '성소윤'

from Arms import *
import PlayerState
import random
import Character

class Monster(Character.Character):
    def Update(self, frameTime):
        Character.Character.Update(self, frameTime)
        if self.shot and self.attackTimer == 0  and not self.death:
            self.Arm.Shoot(self, self.target.x - self.x, (self.target.y + self.target.hCollisionBox/2) - (self.y + self.hCollisionBox/2) )
        self.attackTimer += frameTime
        if self.attackTimer > self.attackTime :
            self.attackTimer = 0

    def Render(self):
        Character.Character.Render(self)
        if not self.death : self.Arm.Render(self, self.target.x - self.x, (self.target.y + self.target.hCollisionBox/2) - (self.y + self.hCollisionBox/2), self.target.x, (self.target.y + self.target.hCollisionBox/2))



class Turtle(Monster):
    created = False
    name = None
    maxHealth = None
    maxShield = None
    wCollisionBox, hCollisionBox  = None, None
    WALK_SPEED_PPS = None
    detectionRange = None
    attackRange = None
    shooter = True
    availDash = False
    attackTime = None
    ally = False
    def __init__(self, x, y, target) :
        if not Turtle.created:
            Turtle.created = True
            Turtle.name = Character.character_data['Turtle']['name']
            Turtle.maxHealth = Character.character_data['Turtle']['maxHealth']
            Turtle.maxShield = Character.character_data['Turtle']['maxShield']
            Turtle.wCollisionBox, Turtle.hCollisionBox  = Character.character_data['Turtle']['collisionBoxWidth'], Character.character_data['Turtle']['collisionBoxWidth']
            Turtle.WALK_SPEED_PPS = Character.character_data['Turtle']['walkSpeedPPS']
            Turtle.detectionRange = Character.character_data['Turtle']['detectionRange']
            Turtle.attackRange = Character.character_data['Turtle']['attackRange']
            Turtle.attackTime = Character.character_data['Turtle']['attackTime']
        Character.Character.__init__(self, x, y, Turtle.maxHealth, Turtle.maxShield)
        self.target = target
        self.state = PlayerState.stateList["A.I_idle"]
        self.Arm = Pistol('Monster')
        self.shot = False
        self.dirx, self.diry = 0, 0
        self.vx, self.vy = Turtle.WALK_SPEED_PPS, Turtle.WALK_SPEED_PPS
        self.attackTimer = 0
        
class SniperDuck(Monster):
    created = False
    name = None
    maxHealth = None
    maxShield = None
    wCollisionBox, hCollisionBox  = None, None
    WALK_SPEED_PPS = None
    detectionRange = None
    attackRange = None
    shooter = True
    availDash = False
    attackTime = None
    ally = False
    def __init__(self, x, y, target):
        if not SniperDuck.created:
            SniperDuck.created = True
            SniperDuck.name = Character.character_data['SniperDuck']['name']
            SniperDuck.maxHealth = Character.character_data['SniperDuck']['maxHealth']
            SniperDuck.maxShield = Character.character_data['SniperDuck']['maxShield']
            SniperDuck.wCollisionBox, SniperDuck.hCollisionBox  = Character.character_data['SniperDuck']['collisionBoxWidth'], Character.character_data['SniperDuck']['collisionBoxWidth']
            SniperDuck.WALK_SPEED_PPS = Character.character_data['SniperDuck']['walkSpeedPPS']
            SniperDuck.detectionRange = Character.character_data['SniperDuck']['detectionRange']
            SniperDuck.attackRange = Character.character_data['SniperDuck']['attackRange']
            SniperDuck.attackTime = Character.character_data['SniperDuck']['attackTime']
        Character.Character.__init__(self, x, y, SniperDuck.maxHealth, SniperDuck.maxShield)
        self.target = target
        self.state = PlayerState.stateList["A.I_idle"]
        self.Arm = SniperGun('Monster')
        self.shot = False
        self.dirx, self.diry = 0, 0
        self.vx, self.vy = SniperDuck.WALK_SPEED_PPS, SniperDuck.WALK_SPEED_PPS
        self.attackTimer = 0
        
class Boss(Monster):
    created = False
    name = None
    maxHealth = None
    maxShield = None
    wCollisionBox, hCollisionBox  = None, None
    WALK_SPEED_PPS = None
    detectionRange = None
    attackRange = None
    shooter = True
    availDash = False
    attackTime = None
    ally = False
    def __init__(self, x, y, target):
        if not Boss.created:
            Boss.created = True
            Boss.name = Character.character_data['Boss']['name']
            Boss.maxHealth = Character.character_data['Boss']['maxHealth']
            Boss.maxShield = Character.character_data['Boss']['maxShield']
            Boss.wCollisionBox, Boss.hCollisionBox  = Character.character_data['Boss']['collisionBoxWidth'], Character.character_data['Boss']['collisionBoxWidth']
            Boss.WALK_SPEED_PPS = Character.character_data['Boss']['walkSpeedPPS']
            Boss.detectionRange = Character.character_data['Boss']['detectionRange']
            Boss.attackRange = Character.character_data['Boss']['attackRange']
            Boss.attackTime = Character.character_data['Boss']['attackTime']
        Character.Character.__init__(self, x, y, Boss.maxHealth, Boss.maxShield)
        self.target = target
        self.state = PlayerState.stateList["A.I_idle"]
        self.Arm = BossGun('Monster')
        self.shot = False
        self.dirx, self.diry = 0, 0
        self.vx, self.vy = Boss.WALK_SPEED_PPS, Boss.WALK_SPEED_PPS
        self.attackTimer = 0

        
        
class DashDuck(Monster):
    created = False
    name = None
    maxHealth = None
    maxShield = None
    wCollisionBox, hCollisionBox  = None, None
    WALK_SPEED_PPS = None
    DASH_SPEED_PPS = None
    dashTime = None
    detectionRange = None
    attackRange = None
    shooter = True
    availDash = True
    attackTime = None
    ally = False
    def __init__(self, x, y, target):
        if not DashDuck.created:
            DashDuck.created = True
            DashDuck.name = Character.character_data['DashDuck']['name']
            DashDuck.maxHealth = Character.character_data['DashDuck']['maxHealth']
            DashDuck.maxShield = Character.character_data['DashDuck']['maxShield']
            DashDuck.wCollisionBox, DashDuck.hCollisionBox  = Character.character_data['DashDuck']['collisionBoxWidth'], Character.character_data['DashDuck']['collisionBoxWidth']
            DashDuck.WALK_SPEED_PPS = Character.character_data['DashDuck']['walkSpeedPPS']
            DashDuck.DASH_SPEED_PPS = Character.character_data['DashDuck']['dashSpeedPPS']
            DashDuck.dashTime = Character.character_data['DashDuck']['dashTime']
            DashDuck.detectionRange = Character.character_data['DashDuck']['detectionRange']
            DashDuck.attackRange = Character.character_data['DashDuck']['attackRange']
            DashDuck.attackTime = Character.character_data['DashDuck']['attackTime']
        Character.Character.__init__(self, x, y, DashDuck.maxHealth, DashDuck.maxShield)
        self.target = target
        self.state = PlayerState.stateList["A.I_idle"]
        self.Arm = Rifle('Monster')
        self.shot = False
        self.dash = False
        self.dashTimer = 0
        self.dirx, self.diry = 0, 0
        self.attackTimer = 0
        self.backTime = random.randint(1, 3)
        self.backTimer = 0
        self.vx, self.vy = DashDuck.WALK_SPEED_PPS, DashDuck.WALK_SPEED_PPS

class Kaze(Monster):
    created = False
    name = None
    maxHealth = None
    maxShield = None
    wCollisionBox, hCollisionBox = None, None
    WALK_SPEED_PPS = None
    DASH_SPEED_PPS = None
    dashTime = None
    detectionRange = None
    attackRange = None
    shooter = False
    availDash = True
    attackTime = None
    attack = None
    ally = False
    def __init__(self, x, y, target):
        if not Kaze.created:
            Kaze.created = True
            Kaze.name = Character.character_data['Kaze']['name']
            Kaze.maxHealth = Character.character_data['Kaze']['maxHealth']
            Kaze.maxShield = Character.character_data['Kaze']['maxShield']
            Kaze.wCollisionBox, Kaze.hCollisionBox  = Character.character_data['Kaze']['collisionBoxWidth'], Character.character_data['Kaze']['collisionBoxWidth']
            Kaze.WALK_SPEED_PPS = Character.character_data['Kaze']['walkSpeedPPS']
            Kaze.DASH_SPEED_PPS = Character.character_data['Kaze']['dashSpeedPPS']
            Kaze.dashTime = Character.character_data['Kaze']['dashTime']
            Kaze.detectionRange = Character.character_data['Kaze']['detectionRange']
            Kaze.attackRange = Character.character_data['Kaze']['attackRange']
            Kaze.meleeTime = Character.character_data['Kaze']['meleeTime']
            Kaze.attackTime = Character.character_data['Kaze']['attackTime']
            Kaze.attack = Character.character_data['Kaze']['attack']
        Character.Character.__init__(self, x, y, Kaze.maxHealth, Kaze.maxShield)
        self.target = target
        self.state = PlayerState.stateList["A.I_idle"]
        self.dash = False
        self.dashTimer = 0
        self.dirx, self.diry = 0, 0
        self.backTime = random.randint(1, 3)
        self.backTimer = 0
        self.vx, self.vy = Kaze.WALK_SPEED_PPS, Kaze.WALK_SPEED_PPS
        self.meleeTimer = 0
        self.activeAttack = False
        self.attackTimer = 0
    def Update(self, frameTime):
        Character.Character.Update(self, frameTime)
        self.attackTimer += frameTime
        if self.attackTimer > self.attackTime :
            self.attackTimer = 0

    def Render(self):
        Character.Character.Render(self)
