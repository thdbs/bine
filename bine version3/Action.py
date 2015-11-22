__author__ = '성소윤'

import StageManager
import Character
import DrawManager

actionList = {}
maxSpeed = 80    #revise 동기화 문제고려해서

def GenAction():
    global actionList
    actionList['move'] = Move()
    actionList['increaseFrame'] = IncreaseFrame()

class Action:
    def Update(self):
        pass


class Move(Action):
    def update(self, character, frameTime):
        global maxSpeed
        shiftX = character.vx*frameTime
        shiftY = character.vy*frameTime
        if not StageManager.MapCollisionCheck(character, shiftX, shiftY):
            character.x += shiftX
            character.y += shiftY
        else :
            shiftX = shiftX / maxSpeed
            shiftY = shiftY / maxSpeed
            while(not StageManager.MapCollisionCheck(character, shiftX, shiftY)):
                character.x += shiftX
                character.y += shiftY


class IncreaseFrame(Action):
    def update(self, character, frameTime):
        character.frameTimer += frameTime
        if(character.frameTimer >= DrawManager.frame_Interval):
            increaseRate = int(character.frameTimer / DrawManager.frame_Interval)
            character.frameTimer = 0
            sprName = character.name + '_' + character.stateName
            character.frame = (character.frame + increaseRate) % DrawManager.CharacterGraphicList[sprName].frame


