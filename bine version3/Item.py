__author__ = '성소윤'

import DrawManager
import StageManager
import EffectManager

class Portal:
    wCollisionBox = None
    hCollisionBox = None
    created = False
    def __init__(self, x, y, goTo, active):
        if not Portal.created:
            Portal.wCollisionBox = 90
            Portal.hCollisionBox = 30
        self.x = x
        self.y = y
        self.goTo = goTo
        self.active = active

    def render(self):
        if self.active:
            if self.goTo == 'shop' :
                DrawManager.ItemGraphicList['shop_portal'].Draw(self.x, self.y)
            else :
                DrawManager.ItemGraphicList['portal'].Draw(self.x, self.y)

    def Teleport(self, player):
        if self.active and player.CollisionCheck(self):
            StageManager.ChangeStage(player, self.goTo)
            return True
        return False

class Item:
    wCollisionBox = None
    hCollisionBox = None
    created = False
    def __init__(self, x, y ):
        if not Item.created:
            Item.created = True
            Item.wCollisionBox = 50
            Item.hCollisionBox = 74
        self.x = x
        self.y = y
        self.effect = None
        self.draw = True

class PistolItem(Item):
    def __init__(self, x, y ):
        Item.__init__(self, x, y)
        self.bullet = 30
        self.coin = 1

    def render(self):
        if self.effect != None and self.effect.end:
            self.draw = True
            self.effect = None
        if self.draw: DrawManager.ItemGraphicList['pistol'].Draw(self.x, self.y)

    def CollisionCheck(self, player):
        if self.effect == None:
            self.y -= Item.hCollisionBox/2
            if player.CollisionCheck(self):
                if player.coin >= self.coin:
                    player.coin -= self.coin
                    player.bullet['Pistol']["storage"] += self.bullet
                    self.effect = EffectManager.CallEffect('pickup_pistol', self, False )
                    self.draw = False
            self.y += Item.hCollisionBox/2

class RifleItem(Item):
    def __init__(self, x, y ):
        Item.__init__(self, x, y)
        self.bullet = 500
        self.coin = 2

    def render(self):
        if self.effect != None and self.effect.end:
            self.draw = True
            self.effect = None
        if self.draw: DrawManager.ItemGraphicList['rifle'].Draw(self.x, self.y)

    def CollisionCheck(self, player):
        self.y -= Item.hCollisionBox/2
        if player.CollisionCheck(self):
            if player.coin >= self.coin:
                player.coin -= self.coin
                player.bullet['Rifle']["storage"] += self.bullet
                self.effect = EffectManager.CallEffect('pickup_rifle', self, False )
                self.draw = False
        self.y += Item.hCollisionBox/2


class SniperItem(Item):
    def __init__(self, x, y ):
        Item.__init__(self, x, y)
        self.bullet = 20
        self.coin = 2

    def render(self):
        if self.effect != None and self.effect.end:
            self.draw = True
            self.effect = None
        if self.draw: DrawManager.ItemGraphicList['sniper'].Draw(self.x, self.y)

    def CollisionCheck(self, player):
        self.y -= Item.hCollisionBox/2
        if player.CollisionCheck(self):
            if player.coin >= self.coin:
                player.coin -= self.coin
                player.bullet['Sniper']["storage"] += self.bullet
                self.effect = EffectManager.CallEffect('pickup_sniper', self, False )
                self.draw = False
        self.y += Item.hCollisionBox/2


class HealthItem(Item):
    def __init__(self, x, y ):
        Item.__init__(self, x, y)
        self.health = 50
        self.coin = 1

    def render(self):
        if self.effect != None and self.effect.end:
            self.draw = True
            self.effect = None
        if self.draw: DrawManager.ItemGraphicList['health'].Draw(self.x, self.y)

    def CollisionCheck(self, player):
        self.y -= Item.hCollisionBox/2
        if player.CollisionCheck(self):
            if player.coin >= self.coin:
                player.coin -= self.coin
                player.health = min(self.health + player.health, player.maxHealth)
                self.effect = EffectManager.CallEffect('pickup_health', self, False )
                self.draw = False
        self.y += Item.hCollisionBox/2



