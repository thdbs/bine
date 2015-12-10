import Graphic
import Manager
from Player import *
from pico2d import *


class CharacterState:
    def __init__(self):
        pass
    def Update(self):
        pass
    def ProcessInput(self):
        pass
    def ChangeState(self, character, state):
        character.ChangeState(state)

class PlayerRightRunState(CharacterState):
    def __init__(self):
        pass

    def Update(self, player):
        player.x += 1

    def ProcessInput(self, player):
        keyState = Manager.KeyManager.Instance()
        if (not keyState.IsKeyDown(SDLK_w)):
            CharacterState.ChangeState(player,PlayerRightIdleState.Instance() )

class PlayerRightIdleState(CharacterState):
    handle = None

    def __init__(self):
        pass
    def Instance(self):
        if(PlayerRightIdleState.handle == None):
            PlayerRightIdleState.handle = PlayerRightIdleState()
        return(PlayerRightIdleState.handle)