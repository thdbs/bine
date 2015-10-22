__author__ = '성소윤'
from CharacterState import *
from Character import *
from Weapon import *

class Player(Character):
    PlayerStateMap = {}

    def __init__(self, x, y, width, height):
        Character.__init__(self, x, y, width, height)
        #init State
        Player.PlayerStateMap["RightIdle"] = PlayerRightIdleState()
        Player.PlayerStateMap["RightRun"] = PlayerRightRunState()
        Player.PlayerStateMap["LeftRun"] = PlayerLeftRunState()
        Player.PlayerStateMap["Up"] = PlayerUpState()
        Player.PlayerStateMap["Down"] = PlayerDownState()

        self.state = Player.PlayerStateMap["RightIdle"]

        #Weapen Init
        self.weapon = ShotGun()

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