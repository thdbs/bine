from sdl2 import *


class KeyManager:
    handle = None

    def __init__(self):
        self.keyMap = {}
        self.keyMap[SDLK_w] = False

    def KeyUp(self, key):
        self.keyMap[key] = False

    def KeyDown(self, key):
        self.keyMap[key] = True

    def IsKeyDown(self, key):
        if(self.keyMap[key] == True):
            return(True)
        return(False)

    def Instance(self):
        if(KeyManager.handle == None ):
            KeyManager.handle = KeyManager()
        return(KeyManager.handle)
