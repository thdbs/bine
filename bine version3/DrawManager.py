__author__ = '성소윤'
import Camera
from pico2d import *
import json

GraphicData = {}
CharacterGraphicList = {}
StageGraphicList = {}
GunGraphicList = {}
BackObjectGraphicList = {}
BulletGraphicList = {}

class Graphic:
    def Draw(self, x, y):
        pass

class Animation(Graphic):
    def __init__(self, image, width, height, frame, isSide = False, LeftImage = None):
        self.image = image
        self.width = width
        self.height = height
        self.frame = frame
        self.isSide = isSide
        if isSide :
            self.left_image = LeftImage

    def Draw(self, x, y, frame = 0, side = None ):
        drawPointX = x - Camera.x
        drawPointY = y - Camera.y + self.height/2.0
        if Camera.In(drawPointX, drawPointY, self.width, self.height) :
            if self.isSide :
                if side == True :
                    self.image.clip_draw( frame*self.width, 0, self.width, self.height, drawPointX, drawPointY )
                else :
                    self.left_image.clip_draw( frame*self.width, 0, self.width, self.height, drawPointX, drawPointY )
            else :
                self.image.clip_draw( frame*self.width, 0, self.width, self.height, drawPointX, drawPointY )

class StageImage(Graphic):
    def __init__(self, image):
        self.image = image

    def Draw(self):
        self.image.clip_draw( int(Camera.x),int(Camera.y), int(Camera.w), int(Camera.h), int(Camera.w / 2), int(Camera.h / 2) )

class RotateImage(Graphic):
    def __init__(self, LeftImage, RightImage, width, height) :
        self.left_image = LeftImage
        self.right_image = RightImage
        self.width = width
        self.height = height


    def Draw(self, x, y, side, rad):
        drawPointX = x - Camera.x
        drawPointY = y - Camera.y + self.height / 2.0
        if Camera.In(drawPointX, drawPointY, self.width, self.height) :
            if side == True :
                self.right_image.rotate_image(rad, drawPointX, drawPointY)
            else :
                self.right_image.rotate_image(rad, drawPointX, drawPointY)


def GenGraphicList() :
    global CharacterGraphicList, StageGraphicList, GunGraphicList, BackObjectGraphicList, BulletGraphicList

    global GraphicData
    with open('GraphicData.json') as f:
        GraphicData = json.load(f)

    #Character Sprite Load
    Jimmy_right = load_image('Resource/Sprites/Jimmy/spr_jimmy_idle_right.png')
    Jimmy_left = load_image('Resource/Sprites/Jimmy/spr_jimmy_idle_left.png')
    CharacterGraphicList['Jimmy_idle'] = \
        Animation(Jimmy_right, GraphicData["Jimmy"]["idle"]["width"],GraphicData["Jimmy"]["idle"]["height"]
                  ,GraphicData["Jimmy"]["idle"]["frame"], True, Jimmy_left)
    Jimmy_right = load_image('Resource/Sprites/Jimmy/spr_jimmy_sprint_right.png')
    Jimmy_left = load_image('Resource/Sprites/Jimmy/spr_jimmy_sprint_left.png')
    CharacterGraphicList['Jimmy_walk'] = \
        Animation(Jimmy_right, GraphicData["Jimmy"]["walk"]["width"],GraphicData["Jimmy"]["walk"]["height"]
                  ,GraphicData["Jimmy"]["walk"]["frame"], True, Jimmy_left)
    Jimmy_right = load_image('Resource/Sprites/Jimmy/spr_jimmy_dash_right.png')
    Jimmy_left = load_image('Resource/Sprites/Jimmy/spr_jimmy_dash_left.png')
    CharacterGraphicList['Jimmy_dash'] = \
        Animation(Jimmy_right, GraphicData["Jimmy"]["dash"]["width"],GraphicData["Jimmy"]["dash"]["height"]
                  ,GraphicData["Jimmy"]["dash"]["frame"], True, Jimmy_left)
    Jimmy_right = load_image('Resource/Sprites/Jimmy/spr_jimmy_melee_right.png')
    Jimmy_left = load_image('Resource/Sprites/Jimmy/spr_jimmy_melee_left.png')
    CharacterGraphicList['Jimmy_melee'] = \
        Animation(Jimmy_right, GraphicData["Jimmy"]["melee"]["width"],GraphicData["Jimmy"]["melee"]["height"]
                  ,GraphicData["Jimmy"]["melee"]["frame"], True, Jimmy_left)
    Jimmy_right = load_image('Resource/Sprites/Jimmy/spr_jimmy_hit_right.png')
    Jimmy_left = load_image('Resource/Sprites/Jimmy/spr_jimmy_hit_left.png')
    CharacterGraphicList['Jimmy_hit'] = \
        Animation(Jimmy_right, GraphicData["Jimmy"]["hit"]["width"],GraphicData["Jimmy"]["hit"]["height"]
                  , GraphicData["Jimmy"]["hit"]["frame"], True, Jimmy_left)
    Jimmy_right = load_image('Resource/Sprites/Jimmy/spr_jimmy_idle_death.png')
    Jimmy_left = load_image('Resource/Sprites/Jimmy/spr_jimmy_idle_death.png')
    CharacterGraphicList['Jimmy_death'] = \
        Animation(Jimmy_right, GraphicData["Jimmy"]["death"]["width"],GraphicData["Jimmy"]["death"]["height"]
                  , GraphicData["Jimmy"]["death"]["frame"], True, Jimmy_left)
    Jimmy_right = load_image('Resource/Sprites/Jimmy/spr_jimmy_teleport_right.png')
    Jimmy_left = load_image('Resource/Sprites/Jimmy/spr_jimmy_teleport_left.png')
    CharacterGraphicList['Jimmy_teleport'] = \
        Animation(Jimmy_right, GraphicData["Jimmy"]["teleport"]["width"],GraphicData["Jimmy"]["teleport"]["height"]
                  ,GraphicData["Jimmy"]["teleport"]["frame"], True, Jimmy_left)

    Turtle_right = load_image('Resource/Sprites/Monster/Turtle/spr_turtle2_idle_right.png')
    Turtle_left =load_image('Resource/Sprites/Monster/Turtle/spr_turtle2_idle_left.png')
    CharacterGraphicList['Turtle_idle'] = \
        Animation(Turtle_right, GraphicData["Turtle"]["idle"]["width"],GraphicData["Turtle"]["idle"]["height"]
                  ,GraphicData["Turtle"]["idle"]["frame"], True, Turtle_left)
    Turtle_right = load_image('Resource/Sprites/Monster/Turtle/spr_turtle2_walk_right.png')
    Turtle_left =load_image('Resource/Sprites/Monster/Turtle/spr_turtle2_walk_left.png')
    CharacterGraphicList['Turtle_walk'] = \
        Animation(Turtle_right, GraphicData["Turtle"]["walk"]["width"],GraphicData["Turtle"]["walk"]["height"]
                  ,GraphicData["Turtle"]["walk"]["frame"], True, Turtle_left)
    Turtle_right = load_image('Resource/Sprites/Monster/Turtle/spr_turtle2_hit_right.png')
    Turtle_left =load_image('Resource/Sprites/Monster/Turtle/spr_turtle2_hit_left.png')
    CharacterGraphicList['Turtle_hit'] = \
        Animation(Turtle_right, GraphicData["Turtle"]["hit"]["width"],GraphicData["Turtle"]["hit"]["height"]
                  ,GraphicData["Turtle"]["hit"]["frame"], True, Turtle_left)
    Turtle_right = load_image('Resource/Sprites/Monster/Turtle/spr_turtle2_death_right.png')
    Turtle_left =load_image('Resource/Sprites/Monster/Turtle/spr_turtle2_death_left.png')
    CharacterGraphicList['Turtle_death'] = \
        Animation(Turtle_right, GraphicData["Turtle"]["death"]["width"],GraphicData["Turtle"]["death"]["height"]
                  ,GraphicData["Turtle"]["death"]["frame"], True, Turtle_left)
