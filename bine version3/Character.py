__author__ = '성소윤'

import PlayerState
import Action
import EffectManager
from Arms import *
import SoundManager


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
        self.alive = True
        self.death = False
        if random.randint(0, 100) < 50 : self.side = True
        else : self.side = False

    def Update(self, frameTime):
        self.state.update(self, frameTime)

    def Render(self):
        self.state.render(self)
        if self.hit :
            pass


    def ChangeState(self, state, stateName):
        self.state = state
        self.stateName = stateName
        self.frame, self.frameTimer = 0, 0


    def CollisionCheck_Bullet(self, bullet):
        if not self.death:
            if self.x - self.wCollisionBox/2 < bullet.x + bullet.wCollisionBox/2 and self.x + self.wCollisionBox/2 > bullet.x - bullet.wCollisionBox/2 and \
                   self.y < bullet.y + bullet.hCollisionBox/2 and self.y + self.hCollisionBox > bullet.y - bullet.hCollisionBox/2 and self.ally != bullet.ally:
                if self.shield >0:
                    self.shield -= bullet.hit
                    self.shield = max(self.shield, 0)
                    EffectManager.CallEffect('shield', self, False)
                else:
                    self.health -= bullet.hit
                    self.health = max(self.health, 0)
                    str = self.name + '_hit'
                    EffectManager.CallEffect( str, self, True)
                    self.hit = True
                    if self.health <= 0 :
                        self.ChangeState(PlayerState.stateList['death'], 'death')
                        self.death = True
                        if self.name != 'Jimmy' : self.GenCoin()
                bullet.alive = False
                if bullet.name == 'boss':
                    EffectManager.CallEffect('explode', self, False )
                    if not Camera.effect : Camera.effect = True
                return(True)
        return(False)
    
    def CollisionCheck_Character(self, character):
        if self.x - self.wCollisionBox/2 < character.x + character.wCollisionBox/2 and self.x + self.wCollisionBox/2 > character.x - character.wCollisionBox/2 and \
            self.y < character.y + character.hCollisionBox and self.y + self.hCollisionBox > character.y :
            if character.stateName == 'melee':
                if self.shield > 0:
                    self.shield -= character.attack
                    self.shield = max(self.shield, 0)
                    EffectManager.CallEffect('shield', self, False)
                else:
                    self.health -= character.attack
                    self.health = max(self.health, 0)
                    str = self.name + '_hit'
                    EffectManager.CallEffect( str, self, True)
                    self.hit = True
                    if self.health <= 0 :
                        self.ChangeState(PlayerState.stateList['death'], 'death')
                        self.death = True
                        if self.name != 'Jimmy' : self.GenCoin()
            if self.stateName == 'melee':
                if character.shield > 0:
                    character.shield -= self.attack
                    character.shield = max(character.shield, 0)
                    EffectManager.CallEffect('shield', character, False)
                else:
                    character.health -= self.attack
                    character.health = max(character.health, 0)
                    str = character.name + '_hit'
                    EffectManager.CallEffect( str, character, True)
                    if character.health <= 0 :
                        character.ChangeState(PlayerState.stateList['death'], 'death')
                        character.death = True
                        if character.name != 'Jimmy' : character.GenCoin()
            return(True)
        return(False)

    def CollisionCheck(self, obj):
        if self.x - self.wCollisionBox/2 < obj.x + obj.wCollisionBox/2 and self.x + self.wCollisionBox/2 > obj.x - obj.wCollisionBox/2 and \
            self.y < obj.y + obj.hCollisionBox and self.y + self.hCollisionBox > obj.y :
            return True
        return False


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
    attack = None
    ally = True
    shieldTime = None
    maxPistol = None
    maxRifle = None
    maxSniper = None
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
            Jimmy.attack = character_data['Jimmy']['attack']
            Jimmy.shieldTime = character_data['Jimmy']['shieldTimer']
            Jimmy.maxPistol = character_data['Jimmy']['maxPistol']
            Jimmy.maxRifle = character_data['Jimmy']['maxRifle']
            Jimmy.maxSniper = character_data['Jimmy']['maxSniper']
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
        self.shieldTimer = 0
        self.genShield = False
        self.coin = 0
        self.reloadEffect = None
        self.bullet = {
            "Pistol" : { "reloaded" : Jimmy.maxPistol, "storage" :  character_data['Jimmy']['pistol'], "max" : Jimmy.maxPistol },
            "Rifle" : { "reloaded" : Jimmy.maxRifle, "storage" :  character_data['Jimmy']['rifle'], "max" : Jimmy.maxRifle },
            "Sniper" : { "reloaded" : Jimmy.maxSniper, "storage" :  character_data['Jimmy']['sniper'], "max" : Jimmy.maxSniper }
        }
        self.reloading = False

    def Update(self, frameTime):
        self.PrcessInput()
        if self.reloading and self.reloadEffect.end :
            self.reloadEffect = None
            self.reloading = False
            need = self.bullet[self.ArmsNameList[self.curArm]]['max']- self.bullet[self.ArmsNameList[self.curArm]]['reloaded']
            #print(self.bullet[self.ArmsNameList[self.curArm]]['max'], need)
            need = min(need, self.bullet[self.ArmsNameList[self.curArm]]['storage'])
            self.bullet[self.ArmsNameList[self.curArm]]['reloaded'] += need
            self.bullet[self.ArmsNameList[self.curArm]]['storage'] -= need

        Character.Update(self, frameTime)
        if self.shot and not self.reloading and not self.death and self.bullet[self.ArmsNameList[self.curArm]]['reloaded'] > 0 :
            self.ArmsList[self.ArmsNameList[self.curArm]].Shoot(self,InputManager.mouseX + Camera.x - self.x, InputManager.mouseY + Camera.y - self.y - self.hCollisionBox/2 )
            if not Camera.effect : Camera.effect = True
            if self.curArm != 'Sniper' :  SoundManager.CallEffectSound('pistol')
            else :  SoundManager.CallEffectSound('sniper')
            self.bullet[self.ArmsNameList[self.curArm]]['reloaded'] -= 1
            if self.bullet[self.ArmsNameList[self.curArm]]['reloaded'] == 0 and self.bullet[self.ArmsNameList[self.curArm]]['storage'] > 0 :
                self.reloadEffect = EffectManager.CallEffect('reloading_long', InputManager.mPos, False)
                SoundManager.CallEffectSound('reload')
                self.reloading = True

        if StageManager.curStage == 'stage2_exit':
            if self.x - Camera.x <= 200  and not self.death:
                self.ChangeState(PlayerState.stateList['death'], 'death')
                self.death = True


        self.shieldTimer += frameTime
        if self.shieldTimer > self.shieldTime :
            self.shieldTimer = 0
            if self.shield < self.maxShield :
                self.genShield = True
                EffectManager.CallEffect('shield', self, False)

        if self.genShield :
            self.shield += 1
            self.shield = min(self.shield, self.maxShield)
            if (self.shield == self.maxShield) : self.genShield = False

    def Render(self):
        if not self.hit : Character.Render(self)
        if not self.activeAttack and not self.death : self.ArmsList[self.ArmsNameList[self.curArm]].Render(self, InputManager.mouseX + Camera.x - self.x, InputManager.mouseY + Camera.y - self.y - self.hCollisionBox/2, InputManager.mouseX + Camera.x,InputManager.mouseY + Camera.y )
        elif self.activeAttack and not self.death : self.ArmsList[self.ArmsNameList[self.curArm]].Render(self, self.vx , self.vy - 100, self.x, self.y + self.hCollisionBox/2 )
        StageManager.MiniMapRender(self.x, self.y, 255, 50, 50)

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
            if (InputManager.GetKeyState(SDLK_f)) and not self.death :
                dirx = InputManager.mouseX + Camera.x - self.x
                diry = InputManager.mouseY + Camera.y - self.y - self.hCollisionBox/2
                dirx, diry = Action.Nomalization(dirx, diry)
                self.vx = dirx * Jimmy.WALK_SPEED_PPS
                self.vy = diry * Jimmy.WALK_SPEED_PPS
                self.ChangeState(PlayerState.stateList['Jimmy_melee'], 'melee')
            if (InputManager.GetKeyState(SDLK_e)) and not self.death :
                for i in StageManager.PortalList[StageManager.curStage]:
                    if i.Teleport(self): break
                if StageManager.curStage == 'shop':
                    for i in StageManager.ShopItemList:
                        i.CollisionCheck(self)
                InputManager.KeyUp(SDLK_e)
            if InputManager.GetKeyState(SDLK_r) and not self.death :
                if self.bullet[self.ArmsNameList[self.curArm]]['storage'] > 0 and self.bullet[self.ArmsNameList[self.curArm]]['reloaded'] < self.bullet[self.ArmsNameList[self.curArm]]['max']\
                        and not self.reloading:
                    self.reloadEffect = EffectManager.CallEffect('reloading', InputManager.mPos, False)
                    SoundManager.CallEffectSound('reload')
                    self.reloading = True
        if InputManager.GetKeyState(SDLK_q) :
            self.curArm = (self.curArm + 1) % 3
            InputManager.KeyUp(SDLK_q)
            SoundManager.CallEffectSound('weapon_switch')
        if InputManager.LButton : self.shot = True
        else : self.shot = False