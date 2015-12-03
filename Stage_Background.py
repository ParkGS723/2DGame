import pico2d
import math
import json
import random
import game_framework

import Main_Scene

from pico2d import *

class BackGround:
    def __init__(self):
        self.x, self.y = 400, 445
        self.image = load_image('Map/Stage_bkg.png')
        self.bgm = load_music('Sound/game_bgm.mp3')
        self.bgm.set_volume(60)
        self.bgm.repeat_play()

    def draw(self):
        self.image.clip_draw(0, 0, 2000, 550, self.x, self.y)

class BackGround2:
    def __init__(self):
        self.x, self.y = 400, 445
        self.image = load_image('Map/Stage2_bkg.png')

    def draw(self):
        self.image.clip_draw(0, 0, 2000, 550, self.x, self.y)

class BackGround3:
    def __init__(self):
        self.x, self.y = 400, 445
        self.image = load_image('Map/Stage3_bkg.png')

    def draw(self):
        self.image.clip_draw(0, 0, 2000, 550, self.x, self.y)

class BackGround4:
    def __init__(self):
        self.x, self.y = 400, 445
        self.image = load_image('Map/Stage4_bkg.png')

    def draw(self):
        self.image.clip_draw(0, 0, 2000, 550, self.x, self.y)

class BackGround5:
    def __init__(self):
        self.x, self.y = 400, 445
        self.image = load_image('Map/Stage5_bkg.png')

    def draw(self):
        self.image.clip_draw(0, 0, 2000, 550, self.x, self.y)