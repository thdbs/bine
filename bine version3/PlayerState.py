__author__ = '성소윤'

from State import *
from  pico2d import *
import  InputManager


class Idle(State):
    def enter(self, player):
        pass

    def update(self, player):
        if InputManager.GetKeyState(SDLK_d) or InputManager.GetKeyState(SDLK_a) or InputManager.GetKeyState(SDLK_w)\
                or InputManager.GetKeyState(SDLK_s):
            player.frame = 0
            player.ChangeState(player.PlayerStateMap["Run"])