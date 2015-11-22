__author__ = '성소윤'

from State import *
import Action

class PlayerWalk(Walk):
    def update(self, player, frameTime):
        if player.vx == 0 and player.vy == 0 :
            player.ChangeState(.stateList['Jimmy_idle'], 'idle')
            player.Update()
            return
        if player.dash:
            player.ChangeState(.stateList['Jimmy_dash'], 'dash')
            player.Update()
            return
        Walk.update(self, player, frameTime)

    def