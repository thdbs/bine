__author__ = '성소윤'

import Action
import PlayerState

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
            str = 'A.I' + '_' + 'idle'
            character.ChangeState(PlayerState.stateList[str], 'idle')

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

    def update(self, character):
        pass

    def render(self, character):
        pass

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