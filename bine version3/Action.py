__author__ = '성소윤'


import Character
import DrawManager
from math import *
import StageManager

actionList = {}
maxSpeed = 80    #동기화 문제고려해서 수정

def GenAction():
    global actionList
    actionList['move'] = Move()
    actionList['increaseFrame'] = IncreaseFrame()
    actionList['increaseFrameOnce'] = IncreaseFrameOnce()
    actionList['observation'] = Observation()
    actionList['Trace'] = Trace()

def GetDistance(x1, y1, x2, y2):
    return sqrt((x2 - x1)*(x2 - x1) + (y2 - y1)*(y2 - y1))

def Nomalization(x, y) :
    len = sqrt(x*x + y*y)
    return x/len, y/len

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

class IncreaseFrameOnce(Action):
    def update(self, character, frameTime):
        character.frameTimer += frameTime
        if(character.frameTimer >= DrawManager.frame_Interval):
            increaseRate = int(character.frameTimer / DrawManager.frame_Interval)
            character.frameTimer = 0
            sprName = character.name + '_' + character.stateName
            character.frame = (character.frame + increaseRate)
            if character.frame > DrawManager.CharacterGraphicList[sprName].frame :
                return True
            return False


class Observation(Action):
    def update(self, character, target):
        distance = GetDistance(character.x, character.y, target.x, target. y)
        if( distance < character.detectionRange):
            if(distance < character.attackRange):
                return "attack"
            return "move"
        return None


class Trace(Action):
    def update(self, character, tartget):
        vx = [-1, 0, 1, -1, 1, -1, 0, 1]
        vy = [-1, -1, -1, 0, 0, 1, 1, 1]
        mRow, mCol = StageManager.GetMyPoistion(character.x, character.y)
        tRow, tCol = StageManager.GetMyPoistion(tartget.x, tartget.y)
        minvx, minvy = None, None
        minH = 111111111111111
        for i in range(8):
            d = GetDistance(mCol + vx[i], mRow + vy[i], tCol, tRow)
            if (StageManager.GetMapDate(mRow + vy[i], mCol + vx[i]) == '0') and ( d < minH ):
                minvx, minvy = vx[i], vy[i]
                minH = d
        if minvx == None or minvy == None : return
        if minvx* minvy == 0 :
            character.dirx = minvx
            character.diry = -minvy
        else :
            cx, cy, w, h = StageManager.GetTileData(mRow, mCol)
            dirX = (cx + (w/2.0)*minvx) - character.x
            dirY = (cy + (h/2.0)*(-minvy)) - character.y
            dirX, dirY = Nomalization(dirX, dirY)
            if dirX == 0 and dirY ==0 :
                dirX , dirY = minvx, -minvy
            character.dirx, character.diry = dirX, dirY
        character.vx = character.dirx*character.WALK_SPEED_PPS
        character.vy = character.diry*character.WALK_SPEED_PPS
        if character.dirx > 0 : character.side = True
        else : character.side = False
