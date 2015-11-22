__author__ = '성소윤'

import StageManager
import Character
import DrawManager

actionList = None
maxSpeed = 6 #revise 동기화 문제고려

def GetAction(action):
    global actionList, maxSpeed
    #action 생성

    return actionList[action]

class Action:
    def Update(self):
        pass


class Move(Action):
    def Update(self, character, frameTime):
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
    def Update(self, character, frameTime):
        character.frmaeTimer += frameTime
        if(character.frmaeTimer >= DrawManager.frameInterval):
            increaseRate = character.frmaeTimer / DrawManger.frameInterval
            character.frmaeTimer = 0
            sprName = character.name + '_' + character.stateName
            character.frame = (character.frame + increaseRate) % DrawManager.sprList['sprName']


