__author__ = '성소윤'

from Graphic import *
import InputManager
import Camera


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
        if not player.MapCollisonCheck( 3, 0):
            player.x += 3
            Camera.Update(3, 0)
        player.Timer += 1
        if player.Timer >= 6:
            player.Timer = 0
            player.frame = ( player.frame + 1 ) % 6

    def Render(self, player):
        global PlayerGraphicMap
        if InputManager.mouseX >= 640:
            PlayerGraphicMap["RightRun"].Draw(player.x - Camera.xPos , player.y -Camera.yPos + 47, player.frame)
        else:
            PlayerGraphicMap["LeftRun"].Draw(player.x - Camera.xPos , player.y -Camera.yPos + 47, player.frame)

    def ProcessInput(self, player):
       if not InputManager.GetKeyState(SDLK_d):
           player.frame = 0
           CharacterState.ChangeState(self, player, player.PlayerStateMap["RightIdle"])


class PlayerLeftRunState(CharacterState):
    def __init__(self):
        pass

    def Update(self, player):
        if not player.MapCollisonCheck( -3, 0):
            player.x -= 3
            Camera.Update(-3, 0)
        player.Timer += 1
        if player.Timer >= 6:
            player.Timer = 0
            player.frame = ( player.frame + 1 ) % 6

    def Render(self, player):
        global PlayerGraphicMap
        if InputManager.mouseX >= 640:
            PlayerGraphicMap["RightRun"].Draw(player.x - Camera.xPos , player.y -Camera.yPos + 47, player.frame)
        else:
            PlayerGraphicMap["LeftRun"].Draw(player.x - Camera.xPos , player.y -Camera.yPos + 47, player.frame)

    def ProcessInput(self, player):
       if not InputManager.GetKeyState(SDLK_a):
           player.frame = 0
           CharacterState.ChangeState(self, player, player.PlayerStateMap["RightIdle"])


class PlayerUpState(CharacterState):
    def __init__(self):
        pass

    def Update(self, player):
        if not player.MapCollisonCheck( 0, 3):
            player.y += 3
            Camera.Update(0, 3)
        player.Timer += 1
        if player.Timer >= 6:
            player.Timer = 0
            player.frame = ( player.frame + 1 ) % 6

    def Render(self, player):
        global PlayerGraphicMap
        if InputManager.mouseX >= 640:
            PlayerGraphicMap["RightRun"].Draw(player.x - Camera.xPos , player.y -Camera.yPos + 47, player.frame)
        else:
            PlayerGraphicMap["LeftRun"].Draw(player.x - Camera.xPos , player.y -Camera.yPos + 47, player.frame)

    def ProcessInput(self, player):
       if not InputManager.GetKeyState(SDLK_w):
           player.frame = 0
           CharacterState.ChangeState(self, player, player.PlayerStateMap["RightIdle"])

class PlayerDownState(CharacterState):
    def __init__(self):
        pass

    def Update(self, player):
        if not player.MapCollisonCheck( 0, -3):
            player.y -= 3
            Camera.Update(0, -3)
        player.Timer += 1
        if player.Timer >= 6:
            player.Timer = 0
            player.frame = ( player.frame + 1 ) % 6

    def Render(self, player):
        global PlayerGraphicMap
        if InputManager.mouseX >= 640:
            PlayerGraphicMap["RightRun"].Draw(player.x - Camera.xPos , player.y -Camera.yPos + 47, player.frame)
        else:
            PlayerGraphicMap["LeftRun"].Draw(player.x - Camera.xPos , player.y -Camera.yPos + 47, player.frame)

    def ProcessInput(self, player):
       if not InputManager.GetKeyState(SDLK_s):
           player.frame = 0
           CharacterState.ChangeState(self, player, player.PlayerStateMap["RightIdle"])


class PlayerRightIdleState(CharacterState):

    def __init__(self):
        pass

    def Update(self, player):
        player.Timer += 1
        if player.Timer >= 6:
            player.Timer = 0
            player.frame = ( player.frame + 1 ) % 12

    def Render(self, player):
        global PlayerGraphicMap
        if InputManager.mouseX >= 640:
            PlayerGraphicMap["RightIde"].Draw(player.x- Camera.xPos, player.y- Camera.yPos + 47, player.frame)
        else:
            PlayerGraphicMap["LeftIdle"].Draw(player.x- Camera.xPos, player.y- Camera.yPos + 47, player.frame)


    def ProcessInput(self, player):
        if InputManager.GetKeyState(SDLK_d):
            player.frame = 0
            CharacterState.ChangeState(self, player, player.PlayerStateMap["RightRun"])
        elif InputManager.GetKeyState(SDLK_a):
            player.frame = 0
            CharacterState.ChangeState(self, player, player.PlayerStateMap["LeftRun"])
        elif InputManager.GetKeyState(SDLK_w):
            player.frame = 0
            CharacterState.ChangeState(self, player, player.PlayerStateMap["Up"])
        elif InputManager.GetKeyState(SDLK_s):
            player.frame = 0
            CharacterState.ChangeState(self, player, player.PlayerStateMap["Down"])

class TurtleMonsterIdleState(CharacterState):

    def __init__(self):
        pass

    def Update(self, monster):
        monster.Timer += 1
        if monster.Timer >= 6:
            monster.Timer = 0
            monster.frame = ( monster.frame + 1 ) % 12

    def Render(self, monster):
        global TurtleMonsterGraphicMap
        if monster.target.x > monster.x :
            TurtleMonsterGraphicMap["RightIdle"].Draw(monster.x- Camera.xPos, monster.y- Camera.yPos + 47, monster.frame)
        else:
            TurtleMonsterGraphicMap["LeftIdle"].Draw(monster.x- Camera.xPos, monster.y- Camera.yPos + 47, monster.frame)

class TurtleMonsterAttackState(CharacterState):
    pass;