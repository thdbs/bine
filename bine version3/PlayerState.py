__author__ = '성소윤'

from State import *
import Action
import DrawManager
import InputManager
import Camera
from AIstate import *

stateList = {}
def GenStateList() :
    global stateList
    stateList['Jimmy_walk'] = PlayerWalk()
    stateList['Jimmy_idle'] = PlayerIdle()
    stateList['Jimmy_dash'] = PlayerDash()
    stateList['Jimmy_melee'] = PlayerMelee()
    stateList["A.I_idle"] = AiIdle()
    stateList["A.I_melee"] = AiMelee()
    stateList["A.I_walk_dash"] = AiWalkDash()
    stateList["A.I_walk"] = AiWalk()
    stateList["A.I_dash"] = AiDash()
    stateList["A.I_melee"] = AiMelee()


class PlayerIdle(Idle):
    def update(self, player, frameTime):
        if player.vx != 0 or player.vy != 0 :
            player.ChangeState(stateList['Jimmy_walk'], 'walk')
            player.Update(frameTime)
            return
        Idle.update(self, player, frameTime)

    def render(self, character):
        if InputManager.mouseX >= 640:
            character.side = True
        else :
            character.side = False
        DrawManager.CharacterGraphicList['Jimmy_idle'].Draw(character.x, character.y, character.frame, character.side )


class PlayerWalk(Walk):
    def update(self, player, frameTime):
        if player.vx == 0 and player.vy == 0 :
            player.ChangeState(stateList['Jimmy_idle'], 'idle')
            player.Update(frameTime)
            return
        if player.dash:
            player.ChangeState(stateList['Jimmy_dash'], 'dash')
            player.Update(frameTime)
            return
        Walk.update(self, player, frameTime)
        Camera.SetPos(player.x, player.y)

    def render(self, character):
        if InputManager.mouseX >= 640:
            character.side = True
        else :
            character.side = False
        DrawManager.CharacterGraphicList['Jimmy_walk'].Draw(character.x, character.y, character.frame, character.side )


class PlayerDash(Dash):
    def update(self, player, frameTime):
        Dash.update(self, player, frameTime)
        Camera.SetPos(player.x, player.y)
        player.dashTimer += frameTime
        if player.dashTimer > player.dashTime :
            player.dashTimer = 0
            player.dash = False
            player.vx, player.vy = player.vx / player.DASH_SPEED_PPS, player.vy / player.DASH_SPEED_PPS
            player.ChangeState(stateList['Jimmy_walk'], 'walk')

    def render(self, character):
        if InputManager.mouseX >= 640:
            character.side = True
        else :
            character.side = False
        DrawManager.CharacterGraphicList['Jimmy_dash'].Draw(character.x, character.y, character.frame, character.side )


class PlayerMelee(Melee):
    def update(self, player, frameTime):
        Melee.update(self,player, frameTime)
        Camera.SetPos(player.x, player.y)
        if not player.activeAttack  : player.vx , player.vy = 0, 0

    def render(self, character):
        DrawManager.CharacterGraphicList['Jimmy_melee'].Draw(character.x, character.y, character.frame, character.side)