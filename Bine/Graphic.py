from sdl2 import *
from pico2d import *

Stage1R1image = None
PrRunAni = None

class Animation:
    def __init__(self, image, width, height, maxFrame, tickTime):
        self.image = image
        self.width = width
        self.height = height
        self.frame = 0
        self.maxFrame = maxFrame

        self.ticKTime = tickTime
        self.Timer = 0

    def Draw(self, x, y):
        self.image.clip_draw(self.frame*self.width,0, self.width, self.height, x, y )

    def Update(self):
        ++self.Timer
        if self.Timer >= self.ticKTime:
            self.Timer = 0
            self.frame = ( self.frame + 1 ) % self.maxFrame


def SetGraphic():
    global PrRunAni
    global Stage1R1image
    #Player Sprite Load
    PrRun = load_image('Resource/Player/spr_jimmy_sprint_right.png')
    PrRunAni = Animation(PrRun, 114, 94, 6, 10)

    #Stage Image Load
    Stage1R1image = load_image('Resource/Stage/stage1_room1.png')