__author__ = '성소윤'
import Camera
from pico2d import *
import json

GraphicList = {}
GraphicData = {}
CharacterGraphicList = {}
StageGraphicList = {}
ArmsGraphicList = {}
BackObjectGraphicList = {}
BulletGraphicList = {}
frame_Interval = 0.1

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
        drawPointX = int(x - Camera.x)
        drawPointY = int(y - Camera.y + self.height/2)
        if Camera.In(drawPointX, drawPointY, self.width, self.height) :
            if self.isSide :
                if side == True :
                    self.image.clip_draw(frame*self.width, 0, self.width, self.height, drawPointX, drawPointY )
                else :
                    self.left_image.clip_draw(frame*self.width, 0, self.width, self.height, drawPointX, drawPointY )
            else :
                self.image.clip_draw(frame*self.width, 0, self.width, self.height, drawPointX, drawPointY )

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
        drawPointY = y - Camera.y
        if Camera.In(drawPointX, drawPointY, self.width, self.height) :
            if side == True :
                self.right_image.rotate_draw(rad, drawPointX, drawPointY)
            else :
                self.left_image.rotate_draw(rad, drawPointX, drawPointY)


def GenGraphicList() :
    global CharacterGraphicList, StageGraphicList, ArmsGraphicList, BackObjectGraphicList, BulletGraphicList
    global GraphicList

    global GraphicData
    with open('GraphicData.json') as f:
        GraphicData = json.load(f)

    #Character Sprite Load
    Jimmy_right = load_image('Resource/Sprites/Jimmy/spr_jimmy_idle_right.png')
    Jimmy_left = load_image('Resource/Sprites/Jimmy/spr_jimmy_idle_left.jpg')
    CharacterGraphicList['Jimmy_idle'] = \
        Animation(Jimmy_right, GraphicData["Jimmy"]["idle"]["width"],GraphicData["Jimmy"]["idle"]["height"]
                  ,GraphicData["Jimmy"]["idle"]["frame"], True, Jimmy_left)
    Jimmy_right = load_image('Resource/Sprites/Jimmy/spr_jimmy_sprint_right.png')
    Jimmy_left = load_image('Resource/Sprites/Jimmy/spr_jimmy_sprint_left.jpg')
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
    Jimmy_right = load_image('Resource/Sprites/Jimmy/spr_jimmy_death_right.png')
    Jimmy_left = load_image('Resource/Sprites/Jimmy/spr_jimmy_death_left.png')
    CharacterGraphicList['Jimmy_death'] = \
        Animation(Jimmy_right, GraphicData["Jimmy"]["death"]["width"],GraphicData["Jimmy"]["death"]["height"]
                  , GraphicData["Jimmy"]["death"]["frame"], True, Jimmy_left)
    Jimmy_right = load_image('Resource/Sprites/Jimmy/spr_jimmy_teleport_in.png')
    CharacterGraphicList['Jimmy_teleport'] = \
        Animation(Jimmy_right, GraphicData["Jimmy"]["teleport"]["width"],GraphicData["Jimmy"]["teleport"]["height"]
                  ,GraphicData["Jimmy"]["teleport"]["frame"])

    Turtle_right = load_image('Resource/Sprites/Monster/Turtle/spr_turtle2_idle_right.jpg')
    Turtle_left = load_image('Resource/Sprites/Monster/Turtle/spr_turtle2_idle_left.jpg')
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
    Turtle_left = load_image('Resource/Sprites/Monster/Turtle/spr_turtle2_death_left.png')
    CharacterGraphicList['Turtle_death'] = \
        Animation(Turtle_right, GraphicData["Turtle"]["death"]["width"],GraphicData["Turtle"]["death"]["height"]
                  ,GraphicData["Turtle"]["death"]["frame"], True, Turtle_left)

    #Stage Image Load
    stage = load_image('Resource/Sprites/Stage/stage1_room1.png')
    StageGraphicList['stage1_1'] = StageImage(stage)
    stage = load_image('Resource/Sprites/Stage/stage1_room2.png')
    StageGraphicList['stage1_2'] = StageImage(stage)
    stage = load_image('Resource/Sprites/Stage/stage2_boss.png')
    StageGraphicList['stage2_boss'] = StageImage(stage)
    stage = load_image('Resource/Sprites/Stage/stage2_exit.png')
    StageGraphicList['stage2_exit'] = StageImage(stage)
    stage = load_image('Resource/Sprites/Stage/shop.png')
    StageGraphicList['shop'] = StageImage(stage)

    #Gun Image Load
    gun_right = load_image('Resource/Sprites/Weapon/spr_jimmy_pistol_right.png')
    gun_left = load_image('Resource/Sprites/Weapon/spr_jimmy_pistol_left.png')
    ArmsGraphicList['Jimmy_pistol'] = RotateImage(gun_left, gun_right, GraphicData['Arms']['jimmy_pistol']['width'],
                                                 GraphicData['Arms']['jimmy_pistol']['height'])
    gun_right = load_image('Resource/Sprites/Weapon/spr_jimmy_rifle_right.png')
    gun_left = load_image('Resource/Sprites/Weapon/spr_jimmy_rifle_left.png')
    ArmsGraphicList['Jimmy_rifle'] = RotateImage(gun_left, gun_right, GraphicData['Arms']['jimmy_rifle']['width'],
                                                 GraphicData['Arms']['jimmy_rifle']['height'])
    gun_right = load_image('Resource/Sprites/Weapon/spr_jimmy_sniper_right.png')
    gun_left = load_image('Resource/Sprites/Weapon/spr_jimmy_sniper_left.png')
    ArmsGraphicList['Jimmy_sniper'] = RotateImage(gun_left, gun_right, GraphicData['Arms']['jimmy_sniper']['width'],
                                                 GraphicData['Arms']['jimmy_sniper']['height'])
    gun_right = load_image('Resource/Sprites/Weapon/spr_monster_pistol_right.png')
    gun_left = load_image('Resource/Sprites/Weapon/spr_monster_pistol_left.png')
    ArmsGraphicList['Monster_pistol'] = RotateImage(gun_left, gun_right, GraphicData['Arms']['monster_pistol']['width'],
                                                 GraphicData['Arms']['monster_pistol']['height'])
    gun_right = load_image('Resource/Sprites/Weapon/spr_monster_rifle_right.png')
    gun_left = load_image('Resource/Sprites/Weapon/spr_monster_rifle_left.png')
    ArmsGraphicList['Monster_rifle'] = RotateImage(gun_left, gun_right, GraphicData['Arms']['monster_rifle']['width'],
                                                 GraphicData['Arms']['monster_rifle']['height'])
    gun_right = load_image('Resource/Sprites/Weapon/spr_monster_sniper_right.png')
    gun_left = load_image('Resource/Sprites/Weapon/spr_monster_sniper_left.png')
    ArmsGraphicList['Monster_sniper'] = RotateImage(gun_left, gun_right, GraphicData['Arms']['monster_sniper']['width'],
                                                 GraphicData['Arms']['monster_sniper']['height'])
    gun_right = load_image('Resource/Sprites/Weapon/spr_boss_gun_right.png')
    gun_left = load_image('Resource/Sprites/Weapon/spr_boss_gun_left.png')
    ArmsGraphicList['Boss_gun'] = RotateImage(gun_left, gun_right, GraphicData['Arms']['boss_gun']['width'],
                                                 GraphicData['Arms']['boss_gun']['height'])

    #Bullet Image Ldad
    bullet_right = load_image('Resource/Sprites/Weapon/spr_pistol_bullet.png')
    bullet_left = load_image('Resource/Sprites/Weapon/spr_pistol_bullet.png')
    BulletGraphicList['pistol'] = RotateImage(bullet_left, bullet_right, GraphicData['Bullet']['pistol']['width'],
                                                 GraphicData['Bullet']['pistol']['height'])
    bullet_right = load_image('Resource/Sprites/Weapon/spr_rifle_bullet.png')
    bullet_left = load_image('Resource/Sprites/Weapon/spr_rifle_bullet.png')
    BulletGraphicList['rifle'] = RotateImage(bullet_left, bullet_right, GraphicData['Bullet']['rifle']['width'],
                                                 GraphicData['Bullet']['rifle']['height'])
    bullet_right = load_image('Resource/Sprites/Weapon/spr_sniper_bullet_right.png')
    bullet_left = load_image('Resource/Sprites/Weapon/spr_sniper_bullet_left.png')
    BulletGraphicList['sniper'] = RotateImage(bullet_left, bullet_right, GraphicData['Bullet']['sniper']['width'],
                                                 GraphicData['Bullet']['sniper']['height'])
    bullet_right = load_image('Resource/Sprites/Weapon/spr_boss_gun_bullet_right.png')
    bullet_left = load_image('Resource/Sprites/Weapon/spr_boss_gun_bullet_left.png')
    BulletGraphicList['boss'] = RotateImage(bullet_left, bullet_right, GraphicData['Bullet']['boss']['width'],
                                                 GraphicData['Bullet']['boss']['height'])