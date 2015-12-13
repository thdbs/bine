__author__ = '성소윤'
import DrawManager
import Action
import Camera

EffectList = []

def Render():
    global EffectList
    for i in EffectList:
        i.render()

def Update(frameTime):
    global EffectList
    for i in EffectList :
        if i.end:
            EffectList.remove(i)
    for i in EffectList:
        i.update(frameTime)
    Camera.ShakeCamera()

def CallEffect(grahpic_name, owner, isCharcter, isStatic  = False ,x = None, y = None):
    global EffectList
    if not isStatic:
        EffectList.append(Effect(grahpic_name, owner,isCharcter))
    else :
       EffectList.append(StaticEffect(grahpic_name, x, y))
    n = len(EffectList)
    return EffectList[n - 1]

class Effect:
    def __init__(self, graphic_name, owner, isCharcter):
        self.frame = 0
        self.graphic_name = graphic_name
        self.owner = owner
        self.end = False
        self.frameTimer = 0
        self.isCharacter = isCharcter

    def update(self, frameTime):
        if Action.actionList['increaseFrameOnce_effect'].update(self, frameTime) :
            self.end = True
            if self.isCharacter : self.owner.hit = False

    def render(self):
        if not self.end and not self.isCharacter : DrawManager.EffectGraphicList[self.graphic_name].Draw(self.owner.x, self.owner.y, self.frame )
        elif not self.end and self.isCharacter :
            DrawManager.CharacterGraphicList[self.graphic_name].Draw(self.owner.x, self.owner.y, self.frame, self.owner.side )
            self.owner.Render()

class StaticEffect:
    def __init__(self, graphic_name, x, y):
        self.x = x
        self.y = y
        self.frame = 0
        self.graphic_name = graphic_name
        self.end = False
        self.frameTimer = 0
        self.isCharacter = False


    def update(self, frameTime):
        if Action.actionList['increaseFrameOnce_effect'].update(self, frameTime) :
            self.end = True

    def render(self):
        if not self.end : DrawManager.EffectGraphicList[self.graphic_name].Draw(self.x, self.y, self.frame )