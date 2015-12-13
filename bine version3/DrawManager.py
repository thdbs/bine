__author__ = '성소윤'
import Camera
from pico2d import *

GraphicList = {}
GraphicData = {}
CharacterGraphicList = {}
StageGraphicList = {}
ArmsGraphicList = {}
EffectGraphicList = {}
BackObjectGraphicList = {}
BulletGraphicList = {}
UIGraphicList = {}
ItemGraphicList = {}
frame_Interval = 0.1
frame_Interval_effect = 0.3

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
                self.image.clip_draw(int(frame*self.width), 0, int(self.width), self.height, drawPointX, drawPointY )

class AnimationCenter(Graphic):
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
        drawPointY = int(y - Camera.y)
        if Camera.In(drawPointX, drawPointY, self.width, self.height) :
            if self.isSide :
                if side == True :
                    self.image.clip_draw(frame*self.width, 0, self.width, self.height, drawPointX, drawPointY )
                else :
                    self.left_image.clip_draw(frame*self.width, 0, self.width, self.height, drawPointX, drawPointY )
            else :
                self.image.clip_draw(int(frame*self.width), 0, int(self.width), self.height, drawPointX, drawPointY )

class Animation_Stage(Graphic):
    def __init__(self, image, width, height, frame):
        self.image = image
        self.width = width
        self.height = height
        self.frame = frame

    def Draw(self, x, y, frame = 0, side = None ):
        drawPointX = int(x - Camera.x)
        drawPointY = int(y - Camera.y + 360)
        self.image.clip_draw(int(frame*self.width), 0, int(self.width), self.height, drawPointX, drawPointY, 1280, 720 )

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


class StatImage(Graphic):
    def __init__(self, image, width, height) :
        self.image = image
        self.width = width
        self.height = height


    def Draw(self, x, y, w = None):
        if w == None : w = self.width
        self.image.clip_draw(0, 0, w, self.height, x, y )

class StaticImage(Graphic):
    def __init__(self, image, width, height) :
        self.image = image
        self.width = width
        self.height = height


    def Draw(self, x, y):
        drawPointX = int(x - Camera.x)
        drawPointY = int(y - Camera.y + self.height/2)
        self.image.clip_draw(0, 0, self.width, self.height, drawPointX, drawPointY )

class StaticImageCenter(Graphic):
    def __init__(self, image, width, height) :
        self.image = image
        self.width = width
        self.height = height


    def Draw(self, x, y):
        drawPointX = int(x - Camera.x)
        drawPointY = int(y - Camera.y)
        self.image.clip_draw(0, 0, self.width, self.height, drawPointX, drawPointY )


def GenGraphicList() :
    global CharacterGraphicList, StageGraphicList, ArmsGraphicList, BackObjectGraphicList, BulletGraphicList, EffectGraphicList, UIGraphicList, ItemGraphicList
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
    
    DashDuck_right = load_image('Resource/Sprites/Monster/Dash_Duck/spr_duck_dash_right.png')
    DashDuck_left = load_image('Resource/Sprites/Monster/Dash_Duck/spr_duck_dash_left.png')
    CharacterGraphicList['DashDuck_dash'] = \
        Animation(DashDuck_right, GraphicData["DashDuck"]["dash"]["width"],GraphicData["DashDuck"]["dash"]["height"]
                  ,GraphicData["DashDuck"]["dash"]["frame"], True, DashDuck_left)
    DashDuck_right = load_image('Resource/Sprites/Monster/Dash_Duck/spr_duck_death_right.png')
    DashDuck_left = load_image('Resource/Sprites/Monster/Dash_Duck/spr_duck_death_left.png')
    CharacterGraphicList['DashDuck_death'] = \
        Animation(DashDuck_right, GraphicData["DashDuck"]["death"]["width"],GraphicData["DashDuck"]["death"]["height"]
                  ,GraphicData["DashDuck"]["death"]["frame"], True, DashDuck_left)
    DashDuck_right = load_image('Resource/Sprites/Monster/Dash_Duck/spr_duck_hit_right.png')
    DashDuck_left = load_image('Resource/Sprites/Monster/Dash_Duck/spr_duck_hit_left.png')
    CharacterGraphicList['DashDuck_hit'] = \
        Animation(DashDuck_right, GraphicData["DashDuck"]["hit"]["width"],GraphicData["DashDuck"]["hit"]["height"]
                  ,GraphicData["DashDuck"]["hit"]["frame"], True, DashDuck_left)
    DashDuck_right = load_image('Resource/Sprites/Monster/Dash_Duck/spr_duck_idle_right.png')
    DashDuck_left = load_image('Resource/Sprites/Monster/Dash_Duck/spr_duck_idle_left.png')
    CharacterGraphicList['DashDuck_idle'] = \
        Animation(DashDuck_right, GraphicData["DashDuck"]["idle"]["width"],GraphicData["DashDuck"]["idle"]["height"]
                  ,GraphicData["DashDuck"]["idle"]["frame"], True, DashDuck_left)
    DashDuck_right = load_image('Resource/Sprites/Monster/Dash_Duck/spr_duck_walk_right.png')
    DashDuck_left = load_image('Resource/Sprites/Monster/Dash_Duck/spr_duck_walk_left.png')
    CharacterGraphicList['DashDuck_walk'] = \
        Animation(DashDuck_right, GraphicData["DashDuck"]["walk"]["width"],GraphicData["DashDuck"]["walk"]["height"]
                  ,GraphicData["DashDuck"]["walk"]["frame"], True, DashDuck_left)
    
    SniperDuck_right = load_image('Resource/Sprites/Monster/Sniper_Duck/spr_duck3_death_right.png')
    SniperDuck_left = load_image('Resource/Sprites/Monster/Sniper_Duck/spr_duck3_death_left.png')
    CharacterGraphicList['SniperDuck_death'] = \
        Animation(SniperDuck_right, GraphicData["SniperDuck"]["death"]["width"],GraphicData["SniperDuck"]["death"]["height"]
                  ,GraphicData["SniperDuck"]["death"]["frame"], True, SniperDuck_left)
    SniperDuck_right = load_image('Resource/Sprites/Monster/Sniper_Duck/spr_duck3_hit_right.png')
    SniperDuck_left = load_image('Resource/Sprites/Monster/Sniper_Duck/spr_duck3_hit_left.png')
    CharacterGraphicList['SniperDuck_hit'] = \
        Animation(SniperDuck_right, GraphicData["SniperDuck"]["hit"]["width"],GraphicData["SniperDuck"]["hit"]["height"]
                  ,GraphicData["SniperDuck"]["hit"]["frame"], True, SniperDuck_left)
    SniperDuck_right = load_image('Resource/Sprites/Monster/Sniper_Duck/spr_duck3_idle_right.png')
    SniperDuck_left = load_image('Resource/Sprites/Monster/Sniper_Duck/spr_duck3_idle_left.png')
    CharacterGraphicList['SniperDuck_idle'] = \
        Animation(SniperDuck_right, GraphicData["SniperDuck"]["idle"]["width"],GraphicData["SniperDuck"]["idle"]["height"]
                  ,GraphicData["SniperDuck"]["idle"]["frame"], True, SniperDuck_left)
    SniperDuck_right = load_image('Resource/Sprites/Monster/Sniper_Duck/spr_duck3_walk_right.png')
    SniperDuck_left = load_image('Resource/Sprites/Monster/Sniper_Duck/spr_duck3_walk_left.png')
    CharacterGraphicList['SniperDuck_walk'] = \
        Animation(SniperDuck_right, GraphicData["SniperDuck"]["walk"]["width"],GraphicData["SniperDuck"]["walk"]["height"]
                  ,GraphicData["SniperDuck"]["walk"]["frame"], True, SniperDuck_left)
    
    Kaze_right = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_dash_right.png')
    Kaze_left = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_dash_left.png')
    CharacterGraphicList['Kaze_dash'] = \
        Animation(Kaze_right, GraphicData["Kaze"]["dash"]["width"],GraphicData["Kaze"]["dash"]["height"]
                  ,GraphicData["Kaze"]["dash"]["frame"], True, Kaze_left)
    Kaze_right = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_death_right.png')
    Kaze_left = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_death_left.png')
    CharacterGraphicList['Kaze_death'] = \
        Animation(Kaze_right, GraphicData["Kaze"]["death"]["width"],GraphicData["Kaze"]["death"]["height"]
                  ,GraphicData["Kaze"]["death"]["frame"], True, Kaze_left)
    Kaze_right = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_hit_right.png')
    Kaze_left = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_hit_left.png')
    CharacterGraphicList['Kaze_hit'] = \
        Animation(Kaze_right, GraphicData["Kaze"]["hit"]["width"],GraphicData["Kaze"]["hit"]["height"]
                  ,GraphicData["Kaze"]["hit"]["frame"], True, Kaze_left)
    Kaze_right = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_idle_right.png')
    Kaze_left = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_idle_left.png')
    CharacterGraphicList['Kaze_idle'] = \
        Animation(Kaze_right, GraphicData["Kaze"]["idle"]["width"],GraphicData["Kaze"]["idle"]["height"]
                  ,GraphicData["Kaze"]["idle"]["frame"], True, Kaze_left)
    Kaze_right = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_walk_right.png')
    Kaze_left = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_walk_left.png')
    CharacterGraphicList['Kaze_walk'] = \
        Animation(Kaze_right, GraphicData["Kaze"]["walk"]["width"],GraphicData["Kaze"]["walk"]["height"]
                  ,GraphicData["Kaze"]["walk"]["frame"], True, Kaze_left)
    Kaze_right = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_melee_right.png')
    Kaze_left = load_image('Resource/Sprites/Monster/Kaze/spr_kamikaze_melee_left.png')
    CharacterGraphicList['Kaze_melee'] = \
        Animation(Kaze_right, GraphicData["Kaze"]["melee"]["width"],GraphicData["Kaze"]["melee"]["height"]
                  ,GraphicData["Kaze"]["melee"]["frame"], True, Kaze_left)
    
    Boss_right = load_image('Resource/Sprites/Monster/Boss/spr_boss_death_right.png')
    Boss_left = load_image('Resource/Sprites/Monster/Boss/spr_boss_death_left.png')
    CharacterGraphicList['Boss_death'] = \
        Animation(Boss_right, GraphicData["Boss"]["death"]["width"],GraphicData["Boss"]["death"]["height"]
                  ,GraphicData["Boss"]["death"]["frame"], True, Boss_left)
    Boss_right = load_image('Resource/Sprites/Monster/Boss/spr_boss_hit_right.png')
    Boss_left = load_image('Resource/Sprites/Monster/Boss/spr_boss_hit_left.png')
    CharacterGraphicList['Boss_hit'] = \
        Animation(Boss_right, GraphicData["Boss"]["hit"]["width"],GraphicData["Boss"]["hit"]["height"]
                  ,GraphicData["Boss"]["hit"]["frame"], True, Boss_left)
    Boss_right = load_image('Resource/Sprites/Monster/Boss/spr_boss_idle_right.png')
    Boss_left = load_image('Resource/Sprites/Monster/Boss/spr_boss_idle_left.png')
    CharacterGraphicList['Boss_idle'] = \
        Animation(Boss_right, GraphicData["Boss"]["idle"]["width"],GraphicData["Boss"]["idle"]["height"]
                  ,GraphicData["Boss"]["idle"]["frame"], True, Boss_left)
    Boss_right = load_image('Resource/Sprites/Monster/Boss/spr_boss_walk_right.png')
    Boss_left = load_image('Resource/Sprites/Monster/Boss/spr_boss_walk_left.png')
    CharacterGraphicList['Boss_walk'] = \
        Animation(Boss_right, GraphicData["Boss"]["walk"]["width"],GraphicData["Boss"]["walk"]["height"]
                  ,GraphicData["Boss"]["walk"]["frame"], True, Boss_left)
    Boss_right = load_image('Resource/Sprites/Monster/Boss/spr_boss_egg_crack.png')
    CharacterGraphicList['Boss_eggCrack'] = \
        Animation(Boss_right, GraphicData["Boss"]["eggCrack"]["width"],GraphicData["Boss"]["eggCrack"]["height"]
                  ,GraphicData["Boss"]["eggCrack"]["frame"])
    Boss_right = load_image('Resource/Sprites/Monster/Boss/spr_boss_egg_start.png')
    CharacterGraphicList['Boss_eggStart'] = \
        Animation(Boss_right, GraphicData["Boss"]["eggStart"]["width"],GraphicData["Boss"]["eggStart"]["height"]
                  ,GraphicData["Boss"]["eggStart"]["frame"])

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
    ArmsGraphicList['Monster_boss'] = RotateImage(gun_left, gun_right, GraphicData['Arms']['boss_gun']['width'],
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

    #load Effect
    image = load_image('Resource/Sprites/Effect/spr_fire_pixel.png')
    EffectGraphicList['fire'] = \
        Animation(image, image.w/ GraphicData['Effect']['fire']['frame'] ,image.h, GraphicData['Effect']['fire']['frame'] )
    image = load_image('Resource/Sprites/Effect/spr_shield.png')
    EffectGraphicList['shield'] = Animation(image, image.w/ GraphicData['Effect']['shield']['frame'] ,image.h, GraphicData['Effect']['shield']['frame'] )
    image = load_image('Resource/Sprites/Effect/spr_shield_boss.png')
    EffectGraphicList['bossShield'] = Animation(image, image.w/ GraphicData['Effect']['bossShield']['frame'] ,image.h, GraphicData['Effect']['bossShield']['frame'] )
    image = load_image('Resource/Sprites/Effect/spr_teleporter_create.png')
    EffectGraphicList['genPortal'] = Animation(image, image.w/ GraphicData['Effect']['genPortal']['frame'] ,image.h, GraphicData['Effect']['genPortal']['frame'] )
    image = load_image('Resource/Sprites/Effect/spr_change_stage.png')
    EffectGraphicList['chStage'] = Animation_Stage(image, image.w/ GraphicData['Effect']['chStage']['frame'] ,image.h, GraphicData['Effect']['chStage']['frame'] )
    image = load_image('Resource/Sprites/Object/Box/spr_longbox_hit_0.png')
    EffectGraphicList['goodBox_hit'] = AnimationCenter(image, image.w ,image.h, 1 )
    image = load_image('Resource/Sprites/Object/Box/spr_longbox_hit_1.png')
    EffectGraphicList['notGoodBox_hit'] = AnimationCenter(image, image.w ,image.h, 1 )
    image = load_image('Resource/Sprites/Object/Box/spr_longbox_hit_2.png')
    EffectGraphicList['dangerBox_hit'] = AnimationCenter(image, image.w ,image.h, 1 )
    image = load_image('Resource/Sprites/Object/Box/spr_longbox_break.png')
    EffectGraphicList['box_break'] = AnimationCenter(image, image.w/33 ,image.h, 33 )
    image = load_image('Resource/Sprites/Object/Rock/spr_root4_hit_0.png')
    EffectGraphicList['goodRock_hit'] = AnimationCenter(image, image.w ,image.h, 1 )
    image = load_image('Resource/Sprites/Object/Rock/spr_root4_hit_1.png')
    EffectGraphicList['notGoodRock_hit'] = AnimationCenter(image, image.w ,image.h, 1 )
    image = load_image('Resource/Sprites/Object/Rock/spr_root4_hit_2.png')
    EffectGraphicList['dangerRock_hit'] = AnimationCenter(image, image.w ,image.h, 1 )
    image = load_image('Resource/Sprites/Object/Rock/spr_root4_break.png')
    EffectGraphicList['rock_break'] = AnimationCenter(image, image.w/24 ,image.h, 24 )
    image = load_image('Resource/Sprites/Effect/spr_crosshair_reload.png')
    EffectGraphicList['reloading'] = AnimationCenter(image, image.w/24 ,image.h, 24 )
    image = load_image('Resource/Sprites/Effect/spr_crosshair_reload_long.png')
    EffectGraphicList['reloading_long'] = AnimationCenter(image, image.w/48 ,image.h, 48 )

    image = load_image('Resource/Sprites/Item/spr_pickup_light.png')
    EffectGraphicList['pickup_pistol'] = Animation(image, image.w/16 ,image.h, 16 )
    image = load_image('Resource/Sprites/Item/spr_pickup_heavy_0-horz.png')
    EffectGraphicList['pickup_rifle'] = Animation(image, image.w/16 ,image.h, 16 )
    image = load_image('Resource/Sprites/Item/spr_pickup_medium.png')
    EffectGraphicList['pickup_sniper'] = Animation(image, image.w/16 ,image.h, 16 )
    image = load_image('Resource/Sprites/Item/spr_pickup_health_1.png')
    EffectGraphicList['pickup_health'] = Animation(image, image.w/1 ,image.h, 1 )
    image = load_image('Resource/Sprites/Effect/spr_grenade_exp.png')
    EffectGraphicList['explode'] = AnimationCenter(image, image.w/11 ,image.h, 11 )



    #load UI
    image = load_image('Resource/Sprites/Effect/hp_bar.png')
    UIGraphicList['hp_bar'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Effect/hp_bar_back.png')
    UIGraphicList['hp_bar_back'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Effect/shield_bar.png')
    UIGraphicList['shield_bar'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Effect/shield_bar_back.png')
    UIGraphicList['shield_bar_back'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Effect/coin_bar.png')
    UIGraphicList['coin_bar'] = StatImage(image, image.w, image.h)

    image = load_image('Resource/Sprites/Effect/spr_hud_face_jimmy_0.png')
    UIGraphicList['jimmy_good'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Effect/spr_hud_face_jimmy_1.png')
    UIGraphicList['jimmy_danger'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Effect/spr_hud_face_jimmy_2.png')
    UIGraphicList['jimmy_bad'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Effect/spr_crosshair_0.png')
    UIGraphicList['cursor'] = StaticImageCenter(image, image.w, image.h)
    image = load_image('Resource/Sprites/Weapon/spr_jimmy_pistol.png')
    UIGraphicList['Pistol'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Weapon/spr_jimmy_pistol_back.png')
    UIGraphicList['Pistol_back'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Weapon/spr_jimmy_rifle.png')
    UIGraphicList['Rifle'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Weapon/spr_jimmy_rifle_back.png')
    UIGraphicList['Rifle_back'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Weapon/spr_jimmy_sniper.png')
    UIGraphicList['Sniper'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Weapon/spr_jimmy_sniper_back.png')
    UIGraphicList['Sniper_back'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Stage/shop_mini.png')
    UIGraphicList['shop'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Stage/stage1_room1_mini.png')
    UIGraphicList['stage1_1'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Stage/stage1_room2_mini.png')
    UIGraphicList['stage1_2'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Stage/stage2_boss_mini.png')
    UIGraphicList['stage2_boss'] = StatImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Stage/stage2_exit_mini.png')
    UIGraphicList['stage2_exit'] = StatImage(image, image.w, image.h)

    #load Item
    image = load_image('Resource/Sprites/Item/spr_coin_drop.png')
    ItemGraphicList['coin_drop'] = Animation(image, image.w/ GraphicData['Item']['coin_drop']['frame'] ,image.h, GraphicData['Item']['coin_drop']['frame'] )
    image = load_image('Resource/Sprites/Item/spr_coin.png')
    ItemGraphicList['coin'] = Animation(image, image.w/ GraphicData['Item']['coin']['frame'] ,image.h, GraphicData['Item']['coin']['frame'] )
    image = load_image('Resource/Sprites/Object/spr_teleporter.png')
    ItemGraphicList['portal'] = StaticImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Object/spr_teleporter_shop.png')
    ItemGraphicList['shop_portal'] = StaticImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Item/spr_light.png')
    ItemGraphicList['pistol'] = StaticImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Item/spr_heavy.png')
    ItemGraphicList['rifle'] = StaticImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Item/spr_medium.png')
    ItemGraphicList['sniper'] = StaticImage(image, image.w, image.h)
    image = load_image('Resource/Sprites/Item/spr_pickup_health_0.png')
    ItemGraphicList['health'] = StaticImage(image, image.w, image.h)


    image = load_image('Resource/Sprites/Object/Box/spr_longbox_0.png')
    BackObjectGraphicList['goodBox'] = StaticImageCenter(image, image.w, image.h)
    image = load_image('Resource/Sprites/Object/Box/spr_longbox_1.png')
    BackObjectGraphicList['notGoodBox'] = StaticImageCenter(image, image.w, image.h)
    image = load_image('Resource/Sprites/Object/Box/spr_longbox_2.png')
    BackObjectGraphicList['dangerBox'] = StaticImageCenter(image, image.w, image.h)
    image = load_image('Resource/Sprites/Object/Rock/spr_root4_0.png')
    BackObjectGraphicList['goodRock'] = StaticImageCenter(image, image.w, image.h)
    image = load_image('Resource/Sprites/Object/Rock/spr_root4_1.png')
    BackObjectGraphicList['notGoodRock'] = StaticImageCenter(image, image.w, image.h)
    image = load_image('Resource/Sprites/Object/Rock/spr_root4_2.png')
    BackObjectGraphicList['dangerRock'] = StaticImageCenter(image, image.w, image.h)