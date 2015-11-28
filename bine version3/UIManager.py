__author__ = '성소윤'

from pico2d import *
import MainState
import game_framework
import DrawManager
import InputManager
import Camera
import StageManager
from StageManager import ShopItemList


def Render():
    if MainState.jimmy.health > 140 :DrawManager.UIGraphicList['jimmy_good'].Draw(50, 675 )
    elif MainState.jimmy.health > 70 :DrawManager.UIGraphicList['jimmy_danger'].Draw(50, 675 )
    else :DrawManager.UIGraphicList['jimmy_bad'].Draw(70, 660 )
    DrawManager.UIGraphicList['hp_bar_back'].Draw(70 + 15 + 10 + 140, 677 )
    DrawManager.UIGraphicList['hp_bar'].Draw(70 + 15 + 8 + MainState.jimmy.health/2, 680 , MainState.jimmy.health)
    DrawManager.UIGraphicList['shield_bar_back'].Draw(70 + 10 + 90, 658 )
    DrawManager.UIGraphicList['shield_bar'].Draw(70 + 8 + (MainState.jimmy.shield*3)/2, 660 , MainState.jimmy.shield*3)
    DrawManager.UIGraphicList['coin_bar'].Draw(10 + 71, 600)
    game_framework.font.draw(70 + 15 + 10 + 5, 685, 'hp                                 %d' % MainState.jimmy.health, (255, 255, 255))
    game_framework.font.draw(70 + 10 + 5, 660, 'shield          %d' % MainState.jimmy.shield, (255, 255, 255))
    game_framework.font.draw(50 + 50, 600, '%d' % MainState.jimmy.coin, (255, 255, 255))
    player = MainState.jimmy
    if not player.reloading : DrawManager.UIGraphicList['cursor'].Draw(InputManager.mouseX + Camera.x, InputManager.mouseY + Camera.y)
    DrawManager.UIGraphicList[player.ArmsNameList[player.curArm] + '_back'].Draw(42, 98)
    DrawManager.UIGraphicList[player.ArmsNameList[player.curArm]].Draw(40, 100)
    game_framework.font.draw(80, 100, '%d / %d' % (player.bullet[player.ArmsNameList[player.curArm]]["reloaded"], player.bullet[player.ArmsNameList[player.curArm]]["storage"]) , (200, 200, 200))
    if StageManager.curStage == 'shop' :
        game_framework.font.draw(10, 170, '%d / %d' % (player.bullet['Pistol']["reloaded"], player.bullet['Pistol']["storage"]) , (150, 255, 150))
        game_framework.font.draw(10, 150, '%d / %d' % (player.bullet['Rifle']["reloaded"], player.bullet['Rifle']["storage"]) , (150, 150, 255))
        game_framework.font.draw(10, 130, '%d / %d' % (player.bullet['Sniper']["reloaded"], player.bullet['Sniper']["storage"]) , (255, 150, 150))
        game_framework.font.draw(ShopItemList[0].x - Camera.x , ShopItemList[0].y - Camera.y + 90, '%d' % ShopItemList[0].coin , (255, 255, 255))
        game_framework.font.draw(ShopItemList[1].x - Camera.x , ShopItemList[1].y - Camera.y + 90, '%d' % ShopItemList[1].coin , (255, 255, 255))
        game_framework.font.draw(ShopItemList[2].x - Camera.x , ShopItemList[2].y - Camera.y + 90, '%d' % ShopItemList[2].coin , (255, 255, 255))
        game_framework.font.draw(ShopItemList[3].x - Camera.x , ShopItemList[3].y - Camera.y + 110, '%d' % ShopItemList[3].coin , (255, 255, 255))
    DrawManager.UIGraphicList[StageManager.curStage].Draw(StageManager.miniMapX + DrawManager.UIGraphicList[StageManager.curStage].width/2, StageManager.miniMapY + DrawManager.UIGraphicList[StageManager.curStage].height/2)