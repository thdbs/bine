__author__ = '성소윤'

import Action
import DrawManager
import SoundManager

class State:
    def enter(self, character):
        pass

    def update(self, character, frameTime):
        pass

    def render(self, character):
        pass

    def Exit(self, character):
        pass


class Walk(State):
    def enter(self, character):
        pass

    def update(self, character, frameTime):
        Action.actionList['move'].update(character, frameTime)
        Action.actionList['increaseFrame'].update(character, frameTime)

    def render(self, character):
        pass

    def Exit(self, character):
        pass


class Dash(State):
    def enter(self, character):
        pass

    def update(self, character, frameTime):
        Action.actionList['move'].update(character, frameTime)
        Action.actionList['increaseFrame'].update(character, frameTime)

    def render(self, character):
        pass

    def Exit(self, character):
        pass


class Melee(State):
    def enter(self, character):
        pass

    def update(self, character, frameTime):
        character.activeAttack = True
        Action.actionList['move'].update(character, frameTime)
        Action.actionList['increaseFrame'].update(character, frameTime)
        character.meleeTimer += frameTime
        if character.meleeTimer > character.meleeTime :
            character.meleeTimer = 0
            character.activeAttack = False

    def render(self, character):
        pass

    def Exit(self, character):
        pass


class Idle(Melee):
    def enter(self, character):
        pass

    def update(self, character, frameTime):
        Action.actionList['increaseFrame'].update(character, frameTime)

    def render(self, character):
        pass

    def Exit(self, character):
        pass


class Death(State):
    def enter(self, character):
        pass

    def update(self, character, frameTime):
        if Action.actionList['increaseFrameOnce'].update(character, frameTime) :
            character.alive = False

    def render(self, character):
        if character.alive:
            str = character.name + '_' + character.stateName
            DrawManager.CharacterGraphicList[str].Draw(character.x, character.y, character.frame, character.side )

    def Exit(self, character):
        pass


class Teleport(State):
    def enter(self, character):
        pass

    def update(self, character):
        pass

    def render(self, character):
        pass

    def Exit(self, character):
        pass