__author__ = '성소윤'
from CharacterState import *
from Character import *
from Weapon import *

class Monster(Character):
    def __init__(self, x, y, width, height, target):
        Character.__init__(self, x, y, width, height)
        self.ally = False
        self.target = target

    def Update(self):
        self.ProcessInput()
        self.state.Update(self)

    def Render(self):
        self.state.Render(self)
        self.weapon.Render(self.x, self.y)

    def ChangeState(self, state):
        self.state = state

    def ProcessInput(self):
        self.state.ProcessInput(self)
        if InputManager.LButton:
            self.weapon.Shot(self.x, self.y)
            InputManager.LButton = False

class TurtleMonster(Monster):
    MonsterStateMap = {}
    def __init__(self, x, y, width, height, target):
        Monster.__init__(self, x, y, width, height, target)
        #init State
        TurtleMonster.MonsterStateMap["Idle"] = TurtleMonsterIdleState()

        self.state = TurtleMonster.MonsterStateMap["Idle"]

        #Set Weapon

    def Update(self):
        self.state.Update(self)

    def Render(self):
        self.state.Render(self)

    def ChangeState(self, state):
        self.state = state
