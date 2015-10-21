import Graphic

class PlayerState:
    def __init__(self, animation):
        self.animation = animation

    def Render(self, x, y):
        self.animation.Draw(x, y)

    def Update(self):
        self.animation.Update()

    def ProcessInput(self):
        pass


class PlayerRRunState(PlayerState):
