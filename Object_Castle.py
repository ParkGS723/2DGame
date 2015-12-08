import pico2d
import math
import json
import random
import game_framework

import Main_Scene

from pico2d import *

class User_Castle:
    castle_image = None
    defeat = False
    hp_image = None
    hp_red_image = None
    def __init__(self):
        self.x, self.y = 100, 355
        self.user_hp = 20
        self.user_hpbar = 20
        if User_Castle.hp_image == None:
            User_Castle.hp_image = load_image('UI/UI_HPBar.png')
        if User_Castle.hp_red_image == None:
            User_Castle.hp_red_image = load_image('UI/UI_HPBar_red.png')
        if User_Castle.castle_image == None:
            User_Castle.castle_image = load_image('Map/MyCastle.png')

    def update(self, frame_time):
        #print(self.user_hp)
        if self.user_hp == 0:
            self.defeat = True


    def draw(self):
        self.castle_image.draw(100, 355)
        self.hp_image.clip_draw(0, 0, 170, 54, self.x, self.y - 105)
        self.hp_red_image.clip_draw(0, 0, int(113 * (self.user_hpbar / 20)), 28, self.x - 37 + int(113 * (self.user_hpbar / 20 ) / 2), self.y - 105)
        # self.image_life_bar_in.clip_draw(0, 0, int(240 * (self.life / 100)) , 40, 255 + int  ( 240 * (self.life / 100) / 2), 500)
            #(0, self.frame * 10, 66, 500 - int(self.hpbar), 30, 300 - int(self.hpbar / 2))
    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 100, self.x + 40, self.y + 80

class Enemy_Castle:
    castle_image = None
    defeat = False
    hp_image = None
    hp_red_image = None
    def __init__(self):
        self.x, self.y = 1200, 355
        self.enemy_hp = 20
        self.enemy_hpbar = 20
        if Enemy_Castle.hp_image == None:
            Enemy_Castle.hp_image = load_image('UI/UI_HPBar.png')
        if Enemy_Castle.hp_red_image == None:
            Enemy_Castle.hp_red_image = load_image('UI/UI_HPBar_red.png')
        if Enemy_Castle.castle_image == None:
            Enemy_Castle.castle_image = load_image('Map/EnemyCastle.png')

    def update(self, frame_time):
        if self.enemy_hp == 0:
            self.defeat = True


    def draw(self):
        self.castle_image.draw(1200, 355)
        self.hp_image.clip_draw(0, 0, 170, 54, self.x - 20, self.y - 105)
        self.hp_red_image.clip_draw(0, 0, int(113 * (self.enemy_hpbar / 20)), 28, self.x - 57 + int(113 * (self.enemy_hpbar / 20) / 2), self.y - 105)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 100, self.x + 40, self.y + 80
