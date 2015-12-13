__author__ = '성소윤'
from pico2d import *

SoundList = {}

def GenData():
    SoundList['pistol'] = load_wav('Resource/Sound/sfx_pistol.wav')
    SoundList['pistol'].set_volume(64)
    SoundList['sniper'] = load_wav('Resource/Sound/sfx_sniper.wav')
    SoundList['sniper'].set_volume(64)
    SoundList['coin'] = load_wav('Resource/Sound/sfx_coin1.wav')
    SoundList['coin'].set_volume(64)
    SoundList['walk'] = load_wav('Resource/Sound/sfx_walk2.wav')
    SoundList['walk'].set_volume(64)
    SoundList['dash'] = load_wav('Resource/Sound/sfx_dash1.wav')
    SoundList['dash'].set_volume(32)
    SoundList['buy'] = load_wav('Resource/Sound/sfx_buy.wav')
    SoundList['buy'].set_volume(64)
    SoundList['debris'] = load_wav('Resource/Sound/sfx_debris3.wav')
    SoundList['debris'].set_volume(64)
    SoundList['explosion'] = load_wav('Resource/Sound/sfx_grenade_explosion.wav')
    SoundList['explosion'].set_volume(64)
    SoundList['reload'] = load_wav('Resource/Sound/sfx_reload_loop.wav')
    SoundList['reload'].set_volume(32)
    SoundList['weapon_switch'] = load_wav('Resource/Sound/sfx_weapon_switch.wav')
    SoundList['weapon_switch'].set_volume(64)


def CallEffectSound(sound_name):
    SoundList[sound_name].play()