__author__ = '성소윤'

import Action

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
        Action.actionList['increaseFrame'].update(character, frameTime)

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


class TelePort(State):
    def enter(self, character):
        pass

    def update(self, character):
        pass

    def render(self, character):
        pass

    def Exit(self, character):
        pass