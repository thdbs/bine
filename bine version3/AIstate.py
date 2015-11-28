__author__ = '성소윤'

from State import *
import random
import PlayerState

class AiIdle(Idle):
    def update(self, character, frameTime):
        if Action.actionList['observation'].update(character, character.target) == 'attack' :
            if character.shooter : character.shot = True
            else :
                character.ChangeState(PlayerState.stateList['A.I_melee'], 'melee')
                character.Update(frameTime)
                return
        elif Action.actionList['observation'].update(character, character.target) == 'move' :
            if character.availDash :
                character.ChangeState(PlayerState.stateList['A.I_walk_dash'], 'walk')
                character.Update(frameTime)
                return
            else :
                character.ChangeState(PlayerState.stateList['A.I_walk'], 'walk')
                character.Update(frameTime)
                return
        Idle.update(self, character, frameTime)

    def render(self, character):
        str = character.name  + '_' + character.stateName
        DrawManager.CharacterGraphicList[str].Draw(character.x, character.y, character.frame, character.side )

class AiWalk(Walk):
    def update(self, character, frameTime):
        if Action.actionList['observation'].update(character, character.target) == 'attack' :
            if character.shooter :
                character.shot = True
                character.ChangeState(PlayerState.stateList['A.I_idle'], 'idle')
                character.Update(frameTime)
            else :
                character.ChangeState(PlayerState.stateList['A.I_melee'], 'melee')
                character.Update(frameTime)
            return
        Action.actionList['Trace'].update(character, character.target)
        Walk.update(self, character, frameTime)

    def render(self, character):
        str = character.name  + '_' + character.stateName
        DrawManager.CharacterGraphicList[str].Draw(character.x, character.y, character.frame, character.side )

class AiWalkDash(Walk):
    def update(self, character, frameTime):
        if Action.actionList['observation'].update(character, character.target) == 'attack' :
            if character.shooter :
                character.shot = True
                character.ChangeState(PlayerState.stateList['A.I_idle'], 'idle')
                character.Update(frameTime)
            else :
                character.ChangeState(PlayerState.stateList['A.I_melee'], 'melee')
                character.Update(frameTime)
            return
        if character.backTimer >= character.backTimer :
            Action.actionList['Trace'].update(character, character.target)
            character.backTimer = 0
            character.backTime = random.randint(1, 3)
            character.vx = character.vx * character.DASH_SPEED_PPS
            character.vy = character.vy * character.DASH_SPEED_PPS
            character.ChangeState(PlayerState.stateList['A.I_dash'], 'dash')
            character.Update(frameTime)
            return
        Action.actionList['Trace'].update(character, character.target)
        Walk.update(self, character, frameTime)
        character.backTimer += frameTime

    def render(self, character):
        str = character.name  + '_' + character.stateName
        DrawManager.CharacterGraphicList[str].Draw(character.x, character.y, character.frame, character.side )

class AiDash(Dash):
    def update(self, character, frameTime):
        Dash.update(self, character, frameTime)
        character.dashTimer += frameTime
        if character.dashTimer > character.dashTime :
            character.dashTimer = 0
            character.vx, character.vy = character.vx / character.DASH_SPEED_PPS, character.vy / character.DASH_SPEED_PPS
            character.ChangeState(PlayerState.stateList['A.I_walk_dash'], 'walk')

    def render(self, character):
        str = character.name  + '_' + character.stateName
        DrawManager.CharacterGraphicList[str].Draw(character.x, character.y, character.frame, character.side )

class AiMelee(Melee):
    def update(self, character, frameTime):
        Melee.update(self, character, frameTime)
        if not character.activeAttack:
            str = 'A.I' + '_' + 'idle'
            character.ChangeState(PlayerState.stateList[str], 'idle')

    def render(self, character):
        str = character.name + '_' + character.stateName
        DrawManager.CharacterGraphicList[str].Draw(character.x, character.y, character.frame, character.side )

