import pico2d
import json
import random
import game_framework

import Main_Scene

from pico2d import *

class GameSound:
    bomb_sound = None
    goldup_sound = None
    meteor_sound = None
    tornado_sound = None
    hero1_sound = None
    hero2_sound = None
    hero3_sound = None
    hero4_sound = None
    hero5_sound = None
    hero6_sound = None
    hero7_sound = None
    hero8_sound = None
    hero9_sound = None
    victory_sound = None
    defeat_sound = None
    enemy_pass_sound = None
    hero_pass_sound = None
    def __init__(self):
        self.sound_check = None
        if GameSound.enemy_pass_sound == None:
            GameSound.enemy_pass_sound = load_wav('Sound/enemy_pass.wav')
            GameSound.enemy_pass_sound.set_volume(80)

        if GameSound.hero_pass_sound == None:
            GameSound.hero_pass_sound = load_wav('Sound/hero_pass.wav')
            GameSound.hero_pass_sound.set_volume(80)

        if GameSound.victory_sound == None:
            GameSound.victory_sound = load_wav('Sound/Stage_Victory.wav')
            GameSound.victory_sound.set_volume(100)

        if GameSound.defeat_sound == None:
            GameSound.defeat_sound = load_wav('Sound/Stage_Defeat.wav')
            GameSound.defeat_sound.set_volume(100)

        if GameSound.bomb_sound == None:
            GameSound.bomb_sound = load_wav('Sound/game_bomb.wav')
            GameSound.bomb_sound.set_volume(64)

        if GameSound.goldup_sound == None:
            GameSound.goldup_sound = load_wav('Sound/game_goldup.wav')
            GameSound.goldup_sound.set_volume(64)

        if GameSound.meteor_sound == None:
            GameSound.meteor_sound = load_wav('Sound/game_meteor.wav')
            GameSound.meteor_sound.set_volume(64)

        if GameSound.tornado_sound == None:
            GameSound.tornado_sound = load_wav('Sound/game_Tornado.wav')
            GameSound.tornado_sound.set_volume(64)

        if GameSound.hero1_sound == None:
            GameSound.hero1_sound = load_wav('Sound/game_hero1.wav')
            GameSound.hero1_sound.set_volume(64)

        if GameSound.hero2_sound == None:
            GameSound.hero2_sound = load_wav('Sound/game_hero2.wav')
            GameSound.hero2_sound.set_volume(64)

        if GameSound.hero3_sound == None:
            GameSound.hero3_sound = load_wav('Sound/game_hero3.wav')
            GameSound.hero3_sound.set_volume(64)

        if GameSound.hero4_sound == None:
            GameSound.hero4_sound = load_wav('Sound/game_hero4.wav')
            GameSound.hero4_sound.set_volume(64)

        if GameSound.hero5_sound == None:
            GameSound.hero5_sound = load_wav('Sound/game_hero5.wav')
            GameSound.hero5_sound.set_volume(64)

        if GameSound.hero6_sound == None:
            GameSound.hero6_sound = load_wav('Sound/game_hero6.wav')
            GameSound.hero6_sound.set_volume(64)

        if GameSound.hero7_sound == None:
            GameSound.hero7_sound = load_wav('Sound/game_hero7.wav')
            GameSound.hero7_sound.set_volume(64)

        if GameSound.hero8_sound == None:
            GameSound.hero8_sound = load_wav('Sound/game_hero8.wav')
            GameSound.hero8_sound.set_volume(64)

        if GameSound.hero9_sound == None:
            GameSound.hero9_sound = load_wav('Sound/game_hero9.wav')
            GameSound.hero9_sound.set_volume(64)

    def enemypass(self):
        self.enemy_pass_sound.play()

    def heropass(self):
        self.hero_pass_sound.play()

    def bomb(self):
        self.bomb_sound.play()

    def goldup(self):
        self.goldup_sound.play()

    def meteor(self):
        self.meteor_sound.play()

    def tornado(self):
        self.tornado_sound.play()

    def hero1(self):
        self.hero1_sound.play()

    def hero2(self):
        self.hero2_sound.play()

    def hero3(self):
        self.hero3_sound.play()

    def hero4(self):
        self.hero4_sound.play()

    def hero5(self):
        self.hero5_sound.play()

    def hero6(self):
        self.hero6_sound.play()

    def hero7(self):
        self.hero7_sound.play()

    def hero8(self):
        self.hero8_sound.play()

    def hero9(self):
        self.hero9_sound.play()

    def victory(self):
        if self.sound_check == True:
            self.victory_sound.play()


    def defeat(self):
        if self.sound_check == True:
            self.defeat_sound.play()