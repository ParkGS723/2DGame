import random


import game_framework
import Title_Scene
from pico2d import *

import json
import os

button_x, button_y = 0, 0
name = "MainScene"
background = None
font = None
gameUI = None
timer = False
chk_time = 0.0
gold = 0

class User_Valvatorez:

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    user_image = None
    IDLE, ATK, MTK, DIE   = 3, 2, 1, 0

    def __init__(self):
        self.x, self.y = 85, 565
        self.frame = 0
        self.total_frames = 0.0
        self.state = self.IDLE
        if User_Valvatorez.user_image == None:
            User_Valvatorez.user_image = load_image('Hero/Valvatorez_Sheet.png')

    def update(self, frame_time):
        self.total_frames += User_Valvatorez.FRAMES_PER_ACTION * User_Valvatorez.ACTION_PER_TIME * frame_time
        if self.state == self.IDLE:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4

    def draw(self):
        self.user_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 70, self.x + 50, self.y + 70

class Monster_Skleton:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    m_image = None
    WALK, ATTACK, DAMAGE, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 1200, 300
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = -0.8
        self.state = self.WALK
        if Monster_Skleton.m_image == None:
            Monster_Skleton.m_image = load_image('Monster/Skeleton_sheet.png')

    def update(self, frame_time):
        distance = Monster_Skleton.RUN_SPEED_PPS * frame_time
        self.total_frames += Monster_Skleton.FRAMES_PER_ACTION * Monster_Skleton.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATTACK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1200:
            self.dir = -0.8
            self.x = random.randint(1100, 1103)
            self.state = self.WALK
        elif self.x < 100:
            self.dir = 0
            self.x = 100
            self.state = self.ATTACK

    def draw(self):
        self.m_image.clip_draw(self.frame*100, self.state*100, 110, 100, self.x, self.y)

class Magic_Meteor:
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 2.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    magic_image = None

    def __init__(self):
        self.x, self.y = 0, 800
        self.frame = 0
        self.total_frames = 0.0
        self.state = 0
        if Magic_Meteor.magic_image == None:
            Magic_Meteor.magic_image = load_image('Magic/Magic_Meteor.png')

    def update(self, frame_time):
        self.total_frames += Magic_Meteor.FRAMES_PER_ACTION * Magic_Meteor.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 16
        if(self.y > 300):
            self.y -= 0.2
        elif(self.y < 300):
            self.y = -100

    def draw(self):
        self.magic_image.clip_draw(self.frame*70, self.state*100, 60, 80, self.x, self.y)

class Hero_Adell:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1
    adell_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 0, 340 #object_data['Hero_Adell']['y'] #0, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.atk_time = 0.0
        self.atk = 10 #object_data['Hero_Adell']['atk']
        self.health = 50 #object_data['Hero_Adell']['health']
        self.dir = 0.5
        self.state = self.WALK
        if Hero_Adell.adell_image == None:
            Hero_Adell.adell_image = load_image('Hero/Adell_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Adell.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Adell.FRAMES_PER_ACTION * Hero_Adell.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 0.5
            self.x = 100
            self.state = self.WALK

    def die(self, hero, frame_time):
        self.atk_time += frame_time

        if hero.frame == 0:
            if self.atk_time > 0.05:
                self.atk_time = 0
                self.health -= hero.atk
                if self.health <= 0:
                    return True
        return False

    def draw(self):
        self.adell_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 85, self.x + 40, self.y + 65

class Hero_Archer:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1
    archer_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 0, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0.5
        self.state = self.ATK
        if Hero_Archer.archer_image == None:
            Hero_Archer.archer_image = load_image('Hero/Archer_sheet.png')

    def update(self, frame_time):
        distance = Hero_Archer.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Archer.FRAMES_PER_ACTION * Hero_Archer.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 0.5
            self.x = 100
            self.state = self.WALK

    def draw(self):
        self.archer_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 85, self.x + 40, self.y + 65

class Hero_Asuka:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1
    asuka_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 0, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0.5
        self.state = self.WALK
        if Hero_Asuka.asuka_image == None:
            Hero_Asuka.asuka_image = load_image('Hero/Asuka_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Asuka.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Asuka.FRAMES_PER_ACTION * Hero_Asuka.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 0.5
            self.x = 100
            self.state = self.WALK

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 85, self.x + 40, self.y + 65

    def draw(self):
        self.asuka_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

class Hero_Axel:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1
    axel_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 0, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0.5
        self.state = self.WALK
        if Hero_Axel.axel_image == None:
            Hero_Axel.axel_image = load_image('Hero/Axel_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Axel.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Axel.FRAMES_PER_ACTION * Hero_Axel.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 0.5
            self.x = 100
            self.state = self.WALK

    def draw(self):
        self.axel_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 85, self.x + 40, self.y + 65

class Hero_Gunner:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1
    gunner_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 0, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0.5
        self.state = self.WALK
        if Hero_Gunner.gunner_image == None:
            Hero_Gunner.gunner_image = load_image('Hero/Gunner_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Gunner.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Gunner.FRAMES_PER_ACTION * Hero_Gunner.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 0.5
            self.x = 100
            self.state = self.WALK

    def draw(self):
        self.gunner_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 85, self.x + 40, self.y + 65

class Hero_Fenrich:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1
    fenrich_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 0, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0.5
        self.state = self.WALK
        if Hero_Fenrich.fenrich_image == None:
            Hero_Fenrich.fenrich_image = load_image('Hero/Fenrich_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Fenrich.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Fenrich.FRAMES_PER_ACTION * Hero_Fenrich.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 0.5
            self.x = 100
            self.state = self.WALK

    def draw(self):
        self.fenrich_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 85, self.x + 40, self.y + 65

class Hero_Ninja:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1
    ninja_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 0, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0.5
        self.state = self.WALK
        if Hero_Ninja.ninja_image == None:
            Hero_Ninja.ninja_image = load_image('Hero/Ninja_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Ninja.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Ninja.FRAMES_PER_ACTION * Hero_Ninja.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 0.5
            self.x = 100
            self.state = self.WALK

    def draw(self):
        self.ninja_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 85, self.x + 40, self.y + 65

class Hero_Pram:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1
    pram_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 0, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0.5
        self.state = self.WALK
        if Hero_Pram.pram_image == None:
            Hero_Pram.pram_image = load_image('Hero/Pram_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Pram.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Pram.FRAMES_PER_ACTION * Hero_Pram.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 0.5
            self.x = 100
            self.state = self.WALK

    def draw(self):
        self.pram_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 85, self.x + 40, self.y + 65

class Hero_Prof:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 1
    professor_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 0, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 0.5
        self.state = self.WALK
        if Hero_Prof.professor_image == None:
            Hero_Prof.professor_image = load_image('Hero/Professor_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Prof.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Prof.FRAMES_PER_ACTION * Hero_Prof.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 0.5
            self.x = 100
            self.state = self.WALK


    def draw(self):
        self.professor_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 85, self.x + 40, self.y + 65

class User_Castle:
    castle_image = None
    def __init__(self):
        if User_Castle.castle_image == None:
            User_Castle.castle_image = load_image('Map/MyCastle.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.castle_image.draw(100, 355)

class Enemy_Slime:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    slime_image = None
    WALK, ATK  = 3,2

    def __init__(self):
        self.x, self.y = 1200, 330#object_data['Enemy_Slime']['y']
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.atk_time = 0.0
        self.dir = -0.5
        self.atk = 2 #object_data['Enemy_Slime']['atk']
        self.health = 50 #object_data['Enemy_Slime']['heath']
        self.state = self.WALK
        if Enemy_Slime.slime_image == None:
            Enemy_Slime.slime_image = load_image('Monster/Slime_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Slime.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Slime.FRAMES_PER_ACTION * Enemy_Slime.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 5
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 5
        self.x += (self.dir * distance)

        if self.x < 200:
            self.dir = 0
            self.x = 200
            self.state = self.ATK
        elif self.x > 200:
            self.dir = -0.5
            self.state = self.WALK

    def die(self, enemy, frame_time):
        self.atk_time += frame_time
        if enemy.frame == 0:
            if self.atk_time > 0.1:
                self.atk_time = 0
                self.health -= enemy.atk
                if self.health <= 0:
                    return True
        return False


    def draw(self):
        self.slime_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 80, self.x + 40, self.y + 40

class Enemy_Zombie:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    zombie_image = None
    WALK, ATK  = 3,2

    def __init__(self):
        self.x, self.y = 1250, 330
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = -0.5
        self.state = self.WALK
        if Enemy_Zombie.zombie_image == None:
            Enemy_Zombie.zombie_image = load_image('Monster/Zombie_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Zombie.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Zombie.FRAMES_PER_ACTION * Enemy_Zombie.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 5
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x < 200:
            self.dir = 0
            self.x = 200
            self.state = self.ATK
        elif self.x > 200:
            self.dir = -0.5
            self.state = self.WALK

    def draw(self):
        self.zombie_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 80, self.x + 40, self.y + 40

class Enemy_Castle:
    castle_image = None
    def __init__(self):
        if Enemy_Castle.castle_image == None:
            Enemy_Castle.castle_image = load_image('Map/EnemyCastle.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.castle_image.draw(1200, 355)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 80, self.x + 40, self.y + 40

class Enemy_Golem:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    golem_image = None
    WALK, ATK  = 3,2

    def __init__(self):
        self.x, self.y = 1300, 320
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = -0.5
        self.state = self.WALK
        if Enemy_Golem.golem_image == None:
            Enemy_Golem.golem_image = load_image('Monster/WoodGolem_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Zombie.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Zombie.FRAMES_PER_ACTION * Enemy_Zombie.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 5
        self.x += (self.dir * distance)

        if self.x < 200:
            self.dir = 0
            self.x = 200
            self.state = self.ATK
        elif self.x > 200:
            self.dir = -0.5
            self.state = self.WALK

    def draw(self):
        self.golem_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 80, self.x + 40, self.y + 40

class Enemy_Pringer:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    pringer_image = None
    WALK, ATK  = 3,2

    def __init__(self):
        self.x, self.y = 1100, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = -0.5
        self.state = self.WALK
        if Enemy_Pringer.pringer_image == None:
            Enemy_Pringer.pringer_image = load_image('Monster/Pringer_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Pringer.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Pringer.FRAMES_PER_ACTION * Enemy_Pringer.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 2
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 3
        self.x += (self.dir * distance)

        if self.x < 200:
            self.dir = 0
            self.x = 200
            self.state = self.ATK
        elif self.x > 200:
            self.dir = -0.5
            self.state = self.WALK

    def draw(self):
        self.pringer_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 80, self.x + 40, self.y + 15

class Enemy_Demon:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    demon_image = None
    WALK, ATK  = 3,2

    def __init__(self):
        self.x, self.y = 1000, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = -0.5
        self.state = self.WALK
        if Enemy_Demon.demon_image == None:
            Enemy_Demon.demon_image = load_image('Monster/Demon_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Demon.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Demon.FRAMES_PER_ACTION * Enemy_Demon.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 3
        self.x += (self.dir * distance)

        if self.x < 200:
            self.dir = 0
            self.x = 200
            self.state = self.ATK
        elif self.x > 200:
            self.dir = -0.5
            self.state = self.WALK

    def draw(self):
        self.demon_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 80, self.x + 40, self.y + 40

class Enemy_Succubus:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    succubus_image = None
    WALK, ATK  = 3,2

    def __init__(self):
        self.x, self.y = 1300, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = -0.5
        self.state = self.WALK
        if Enemy_Succubus.succubus_image == None:
            Enemy_Succubus.succubus_image = load_image('Monster/Succubus_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Succubus.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Succubus.FRAMES_PER_ACTION * Enemy_Succubus.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 5
        self.x += (self.dir * distance)

        if self.x < 200:
            self.dir = 0
            self.x = 200
            self.state = self.ATK
        elif self.x > 200:
            self.dir = -0.5
            self.state = self.WALK

    def draw(self):
        self.succubus_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 80, self.x + 40, self.y + 40


def enter():
    global hero_adell, hero_archer, hero_axel, hero_asuka, hero_fenrich, hero_gunner, hero_ninja, hero_pram, hero_prof
    global m_Skeleton, enemy_castle, enemy_slime, enemy_zombie, enemy_golem, enemy_pringer, enemy_demon, enemy_succubus
    global user_valva, user_castle
    global stage_background, gameUI, cloud, ui_button, gold, font
    global my_team
    global hero_group1, hero_group2
    global enemy_group1, enemy_group2
    global my_magic
    global magic_meteor

    #obj_data_txt = '                                   \
    #{                                                  \
    #    "Hero_Adell": {y":340, "atk":2, "health":50},  \
    #    "Enemy_Slime": {"y":330, "atk":2, "health":50} \
    #}                                                  \
    #'
    #object_data = json.load(obj_data_txt)
    gold = 10000
    hero_group1 = []
    hero_group2 = []
    enemy_group1 = []
    enemy_group2 = []
    my_team = []
    my_magic = []

    user_valva = User_Valvatorez()
    user_castle = User_Castle()
    hero_adell = Hero_Adell()
    hero_archer = Hero_Archer()
    hero_asuka = Hero_Asuka()
    hero_axel = Hero_Axel()
    hero_fenrich = Hero_Fenrich()
    hero_gunner = Hero_Gunner()
    hero_ninja = Hero_Ninja()
    hero_pram = Hero_Pram()
    hero_prof = Hero_Prof()

    magic_meteor = Magic_Meteor()

    enemy_castle = Enemy_Castle()
    enemy_slime = Enemy_Slime()
    enemy_zombie = Enemy_Zombie()
    enemy_golem = Enemy_Golem()
    enemy_pringer = Enemy_Pringer()
    enemy_demon = Enemy_Demon()
    enemy_succubus = Enemy_Succubus()

    m_Skeleton = Monster_Skleton()
    ui_button = load_image('UI/UI_Button.png')
    gameUI = load_image('UI/GameUI.png')
    stage_background = load_image('Map/Stage2_bkg.png')
    cloud = load_image('Map/cloud.png')
    font = load_font('ENCR10B.TTF')
    game_framework.reset_time()

def exit():
    global hero_adell, hero_archer, hero_axel, hero_asuka, hero_fenrich, hero_gunner, hero_ninja, hero_pram, hero_prof
    global user_valva, user_castle, magic_meteor
    global enemy_castle, enemy_zombie, enemy_golem, enemy_pringer, enemy_demon, enemy_succubus
    del(user_valva)
    del(user_castle)
    del(hero_adell)
    del(hero_archer)
    del(hero_asuka)
    del(hero_axel)
    del(hero_fenrich)
    del(hero_gunner)
    del(hero_ninja)
    del(hero_pram)
    del(hero_prof)
    del(magic_meteor)
    del(enemy_castle)
    del(enemy_zombie)
    del(enemy_golem)
    del(enemy_pringer)
    del(enemy_demon)
    del(enemy_succubus)

def pause():
    pass

def resume():
    pass

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def collide_enter(frame_time):
    for enemy_slime in enemy_group1:
        for hero_adell in my_team:
            if collide(hero_adell, enemy_slime):
                print("col")
                enemy_slime.dir = 0
                hero_adell.dir = 0
                hero_adell.state = hero_adell.ATK
                enemy_slime.state = enemy_slime.ATK

                if hero_adell.die(enemy_slime, frame_time) == True:
                    my_team.remove(hero_adell)
                    enemy_slime.dir = -0.5
                    enemy_slime.state = enemy_slime.WALK

                elif enemy_slime.die(hero_adell, frame_time) == True:
                    enemy_group1.remove(enemy_slime)
                    hero_adell.dir = 0.5
                    hero_adell.state = hero_adell.WALK


def button_click():
    global hero_adell, hero_archer, hero_asuka, hero_axel, hero_fenrich, hero_gunner, hero_ninja, hero_pram, hero_prof, gold
    global enemy_slime
    if 49 < button_x < 170 and 80 < button_y < 210:
        hero_adell = Hero_Adell()
        enemy_slime = Enemy_Slime()
        gold = gold - 100
        if len(my_team) < 10:
            my_team.append(hero_adell)

        if len(enemy_group1) < 10:
            enemy_group1.append(enemy_slime)

    if 179 < button_x < 310 and 85 < button_y < 210:
        hero_archer = Hero_Archer()
        gold = gold - 300
        if len(my_team) < 50:
            my_team.append(hero_archer)

    if 309 < button_x < 440 and 85 < button_y < 210:
        hero_asuka = Hero_Asuka()
        gold = gold - 500
        if len(my_team) < 50:
            my_team.append(hero_asuka)

    if 439 < button_x < 560 and 85 < button_y < 210:
        hero_axel = Hero_Axel()
        gold = gold - 1000
        if len(my_team) < 50:
            my_team.append(hero_axel)

    if 569 < button_x < 690 and 85 < button_y < 210:
        hero_gunner = Hero_Gunner()
        gold = gold - 1500
        if len(my_team) < 50:
            my_team.append(hero_gunner)

    if 699 < button_x < 820 and 85 < button_y < 210:
        hero_fenrich = Hero_Fenrich()
        gold = gold - 2000
        if len(my_team) < 50:
            my_team.append(hero_fenrich)

    if 829 < button_x < 950 and 85 < button_y < 210:
        hero_ninja = Hero_Ninja()
        gold = gold - 3000
        if len(my_team) < 50:
            my_team.append(hero_ninja)

    if 959 < button_x < 1080 and 85 < button_y < 210:
        hero_pram = Hero_Pram()
        gold = gold - 5000
        if len(my_team) < 50:
            my_team.append(hero_pram)

    if 1089 < button_x < 1209 and 85 < button_y < 210:
        hero_prof = Hero_Prof()
        gold = gold - 7000
        if len(my_team) < 50:
            my_team.append(hero_prof)

    if 100 < button_x < 700 and 300 < button_y < 768:
         m_meteor = Magic_Meteor()
         if len(my_magic) < 100:
             m_meteor.x = button_x
             my_magic.append(m_meteor)

def handle_events(frame_time):
    global button_x, button_y, user_valva
    events = get_events()
    global timer, chk_time
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            button_x, button_y = event.x, 720 - event.y
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(Title_Scene)
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            print(button_x, button_y)
            button_click()
            if 100 < button_x < 700 and 300 < button_y < 768:
                user_valva = User_Valvatorez()
                user_valva.state = user_valva.ATK
                timer = False

def update(frame_time):
    global timer, chk_time, gold

    user_valva.update(frame_time)
    magic_meteor.update(frame_time)
    m_Skeleton.update(frame_time)
    #enemy_zombie.update(frame_time)
    #enemy_golem.update(frame_time)
    #enemy_pringer.update(frame_time)
    #enemy_demon.update(frame_time)
    #enemy_succubus.update(frame_time)

    collide_enter(frame_time)
    gold += (frame_time * 100)
    if timer == False:
        chk_time += frame_time
    if chk_time > 1.0:
        timer = True
        chk_time = 0.0
        user_valva.state = user_valva.IDLE



def draw(frame_time):
    global gold
    score = 0
    clear_canvas()
    stage_background.draw(400, 445)
    gameUI.draw(640, 70)
    cloud.draw(90, 500)
    ui_button.draw(1230, 690)
    user_castle.draw()
    user_valva.draw()
    enemy_castle.draw()
    m_Skeleton.draw()

    for enemy_slime in enemy_group1:
        enemy_slime.update(frame_time)
        enemy_slime.draw()
        enemy_slime.draw_bb()

    #enemy_zombie.draw()
    #enemy_zombie.draw_bb()
    #enemy_golem.draw()
    #enemy_golem.draw_bb()
    #enemy_pringer.draw()
    #enemy_pringer.draw_bb()
    #enemy_demon.draw()
    #enemy_demon.draw_bb()
    #enemy_succubus.draw()
    #enemy_succubus.draw_bb()
    font.draw(360, 55, '%1.f' % score)
    font.draw(515, 55, '%1.f' % gold)
    for m_meteor in my_magic:
        m_meteor.update(frame_time)
        m_meteor.draw()

    for hero_adell in my_team:
        hero_adell.update(frame_time)
        hero_adell.draw()
        hero_adell.draw_bb()

    for hero_archer in my_team:
        hero_archer.update(frame_time)
        hero_archer.draw()
        hero_archer.draw_bb()

    for hero_asuka in my_team:
        hero_asuka.update(frame_time)
        hero_asuka.draw()
        hero_asuka.draw_bb()

    for hero_axel in my_team:
        hero_axel.update(frame_time)
        hero_axel.draw()

    for hero_fenrich in my_team:
        hero_fenrich.update(frame_time)
        hero_fenrich.draw()

    for hero_gunner in my_team:
        hero_gunner.update(frame_time)
        hero_gunner.draw()

    for hero_ninja in my_team:
        hero_ninja.update(frame_time)
        hero_ninja.draw()

    for hero_pram in my_team:
        hero_pram.update(frame_time)
        hero_pram.draw()

    for hero_prof in my_team:
        hero_prof.update(frame_time)
        hero_prof.draw()

    #충돌체크

    user_valva.draw_bb()
    update_canvas()





