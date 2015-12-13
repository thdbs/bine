__author__ = '성소윤'

import Character
import PlayerState
import Action
import DrawManager
import SoundManager
import Bullet

def GenData():
    Character.GenCharaterData()
    PlayerState.GenStateList()
    Action.GenAction()
    DrawManager.GenGraphicList()
    Bullet.GenBulletData()
    SoundManager.GenData()