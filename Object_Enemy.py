import pico2d
import math
import json
import random
import game_framework

import Main_Scene

from pico2d import *

class Enemy_Slime:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 3
    slime_image = None
    WALK, ATTACK, MTK, DIE = 3, 2, 1, 0

    def __init__(self, x = 1100):
        enemy_data_file = open('Json/enemy_data.txt','r')
        enemy_data = json.load(enemy_data_file)
        enemy_data_file.close()
        self.x, self.y = x, enemy_data['Enemy_Slime']['y']
        self.atk = enemy_data['Enemy_Slime']['atk']
        self.hp = enemy_data['Enemy_Slime']['hp']
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.atk_time = 0.0
        self.dir = -1.0
        self.check = 0
        self.state = self.WALK
        if Enemy_Slime.slime_image == None:
            Enemy_Slime.slime_image = load_image('Monster/Slime_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Slime.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Slime.FRAMES_PER_ACTION * Enemy_Slime.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 5
            self.dir = -1.0
            self.x += (self.dir * distance)
        elif self.state == self.ATTACK:
            self.frame = int(self.total_frames) % 5
            self.dir = 0
            if self.frame == 4:
                self.check = 0

    def die(self, hero, frame_time):
        self.atk_time += frame_time

        if hero.frame == 0:
            if self.atk_time > 0.1:
                self.atk_time = 0
                self.hp -= hero.atk
                if self.hp <= 0:
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
    WALK, ATTACK, MTK, DIE = 3, 2, 1, 0

    def __init__(self, x = 1100):
        enemy_data_file = open('Json/enemy_data.txt','r')
        enemy_data = json.load(enemy_data_file)
        enemy_data_file.close()
        self.x, self.y = x, enemy_data['Enemy_Zombie']['y']
        self.atk = enemy_data['Enemy_Zombie']['atk']
        self.hp = enemy_data['Enemy_Zombie']['hp']
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.atk_time = 0.0
        self.dir = -0.5
        self.check = 0
        self.state = self.WALK
        if Enemy_Zombie.zombie_image == None:
            Enemy_Zombie.zombie_image = load_image('Monster/Zombie_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Zombie.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Zombie.FRAMES_PER_ACTION * Enemy_Zombie.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 5
            self.dir = -0.5
            self.x += (self.dir * distance)
        elif self.state == self.ATTACK:
            self.frame = int(self.total_frames) % 4
            self.dir = 0.0
            if self.frame == 3:
                self.check = 0

    def die(self, hero, frame_time):
        self.atk_time += frame_time
        if hero.frame == 0:
            if self.atk_time > 0.1:
                self.atk_time = 0
                self.hp -= hero.atk
                if self.hp <= 0:
                    return True
        return False

    def draw(self):
        self.zombie_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

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
    WALK, ATTACK, MTK, DIE = 3, 2, 1, 0

    def __init__(self, x = 1100):
        enemy_data_file = open('Json/enemy_data.txt','r')
        enemy_data = json.load(enemy_data_file)
        enemy_data_file.close()
        self.x, self.y = x, enemy_data['Enemy_Golem']['y']
        self.atk = enemy_data['Enemy_Golem']['atk']
        self.hp = enemy_data['Enemy_Golem']['hp']
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.atk_time = 0.0
        self.dir = -0.5
        self.check = 0
        self.state = self.WALK
        if Enemy_Golem.golem_image == None:
            Enemy_Golem.golem_image = load_image('Monster/WoodGolem_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Golem.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Golem.FRAMES_PER_ACTION * Enemy_Golem.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
            self.dir = -0.5
            self.x += (self.dir * distance)
        elif self.state == self.ATTACK:
            self.frame = int(self.total_frames) % 5
            self.dir = 0.0
            if self.frame == 4:
                self.check = 0

    def die(self, hero, frame_time):
        self.atk_time += frame_time
        if hero.frame == 0:
            if self.atk_time > 0.1:
                self.atk_time = 0
                self.hp -= hero.atk
                if self.hp <= 0:
                    return True
        return False

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
    WALK, ATTACK, MTK, DIE = 3, 2, 1, 0

    def __init__(self, x = 1100):
        enemy_data_file = open('Json/enemy_data.txt','r')
        enemy_data = json.load(enemy_data_file)
        enemy_data_file.close()
        self.x, self.y = x, enemy_data['Enemy_Pringer']['y']
        self.atk = enemy_data['Enemy_Pringer']['atk']
        self.hp = enemy_data['Enemy_Pringer']['hp']
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.atk_time = 0.0
        self.dir = -1.3
        self.check = 0
        self.state = self.WALK
        if Enemy_Pringer.pringer_image == None:
            Enemy_Pringer.pringer_image = load_image('Monster/Pringer_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Pringer.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Pringer.FRAMES_PER_ACTION * Enemy_Pringer.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 2
            self.dir = -1.3
            self.x += (self.dir * distance)
        elif self.state == self.ATTACK:
            self.frame = int(self.total_frames) % 3
            self.dir = 0.0
            if self.frame == 2:
                self.check = 0

    def die(self, hero, frame_time):
        self.atk_time += frame_time
        if hero.frame == 0:
            if self.atk_time > 0.1:
                self.atk_time = 0
                self.hp -= hero.atk
                if self.hp <= 0:
                    return True
        return False

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
    WALK, ATTACK, MTK, DIE = 3, 2, 1, 0

    def __init__(self, x = 1100):
        enemy_data_file = open('Json/enemy_data.txt','r')
        enemy_data = json.load(enemy_data_file)
        enemy_data_file.close()
        self.x, self.y = x, enemy_data['Enemy_Pringer']['y']
        self.atk = enemy_data['Enemy_Pringer']['atk']
        self.hp = enemy_data['Enemy_Pringer']['hp']
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.atk_time = 0.0
        self.dir = -0.5
        self.check = 0
        self.state = self.WALK
        if Enemy_Demon.demon_image == None:
            Enemy_Demon.demon_image = load_image('Monster/Demon_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Demon.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Demon.FRAMES_PER_ACTION * Enemy_Demon.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
            self.dir = -0.5
            self.x += (self.dir * distance)
        elif self.state == self.ATTACK:
            self.frame = int(self.total_frames) % 3
            self.dir = 0.0
            if self.frame == 2:
                self.check = 0

    def die(self, hero, frame_time):
        self.atk_time += frame_time
        if hero.frame == 0:
            if self.atk_time > 0.1:
                self.atk_time = 0
                self.hp -= hero.atk
                if self.hp <= 0:
                    return True
        return False

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
    WALK, ATTACK, MTK, DIE = 3, 2, 1, 0

    def __init__(self, x = 1100):
        enemy_data_file = open('Json/enemy_data.txt','r')
        enemy_data = json.load(enemy_data_file)
        enemy_data_file.close()
        self.x, self.y = x, enemy_data['Enemy_Succubus']['y']
        self.atk = enemy_data['Enemy_Succubus']['atk']
        self.hp = enemy_data['Enemy_Succubus']['hp']
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.atk_time = 0.0
        self.dir = -1.2
        self.check = 0
        self.state = self.WALK
        if Enemy_Succubus.succubus_image == None:
            Enemy_Succubus.succubus_image = load_image('Monster/Succubus_Sheet.png')

    def update(self, frame_time):
        distance = Enemy_Succubus.RUN_SPEED_PPS * frame_time
        self.total_frames += Enemy_Succubus.FRAMES_PER_ACTION * Enemy_Succubus.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 7
            self.dir = -1.2
            self.x += (self.dir * distance)
        elif self.state == self.ATTACK:
            self.frame = int(self.total_frames) % 5
            self.dir = 0.0
            if self.frame == 4:
                self.check = 0

    def die(self, hero, frame_time):
        self.atk_time += frame_time
        if hero.frame == 0:
            if self.atk_time > 0.1:
                self.atk_time = 0
                self.hp -= hero.atk
                if self.hp <= 0:
                    return True
        return False

    def draw(self):
        self.succubus_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 80, self.x + 40, self.y + 40