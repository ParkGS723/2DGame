import pico2d
import math
import json
import random
import game_framework

import Main_Scene

from pico2d import *

class Hero_Adell:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 3.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    adell_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self, x = 0):
        self.x, self.y = x, 340 #object_data['Hero_Adell']['y'] #0, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.atk_time = 0.0
        self.atk = 10 #object_data['Hero_Adell']['atk']
        self.health = 50 #object_data['Hero_Adell']['health']
        self.dir = 2.5
        self.col = 0
        self.state = self.WALK
        if Hero_Adell.adell_image == None:
            Hero_Adell.adell_image = load_image('Hero/Adell_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Adell.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Adell.FRAMES_PER_ACTION * Hero_Adell.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
            self.dir = 2.5
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
            self.dir = 0.0
            if self.frame == 1:
                self.col = 0

        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0.0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 2.5
            self.x = 100
            self.state = self.WALK

    def die(self, hero, frame_time):
        self.atk_time += frame_time
        if hero.frame == 0:
            if self.atk_time > 0.07:
                self.atk_time = 0
                self.health -= self.atk
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
    FRAMES_PER_ACTION = 6
    archer_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self, x = 0):
        self.x, self.y = x, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 2
        self.atk_time = 0.0
        self.atk = 10
        self.col = 0
        self.health = 50
        self.state = self.ATK
        if Hero_Archer.archer_image == None:
            Hero_Archer.archer_image = load_image('Hero/Archer_sheet.png')

    def update(self, frame_time):
        distance = Hero_Archer.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Archer.FRAMES_PER_ACTION * Hero_Archer.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
            self.dir = 2
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
            self.dir = 0
            if self.frame == 1:
                self.col = 0
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 2
            self.x = 100
            self.state = self.WALK

    def die(self, hero, frame_time):
        self.atk_time += frame_time

        if hero.frame == 0:
            if self.atk_time > 0.05:
                self.atk_time = 0
                self.health -= self.atk
                if self.health <= 0:
                    return True
        return False

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
    FRAMES_PER_ACTION = 6
    asuka_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self, x = 0):
        self.x, self.y = x, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 2.0
        self.atk_time = 0.0
        self.atk = 10
        self.col = 0
        self.health = 50
        self.state = self.WALK
        if Hero_Asuka.asuka_image == None:
            Hero_Asuka.asuka_image = load_image('Hero/Asuka_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Asuka.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Asuka.FRAMES_PER_ACTION * Hero_Asuka.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
            self.dir = 2.0
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
            self.dir = 0.0
            if self.frame == 1:
                self.col = 0
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 2.0
            self.x = 100
            self.state = self.WALK

    def die(self, hero, frame_time):
        self.atk_time += frame_time

        if hero.frame == 0:
            if self.atk_time > 0.05:
                self.atk_time = 0
                self.health -= self.atk
                if self.health <= 0:
                    return True
        return False

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
    FRAMES_PER_ACTION = 6
    axel_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self, x = 0):
        self.x, self.y = x, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 2.0
        self.atk_time = 0.0
        self.atk = 10
        self.col = 0
        self.health = 50
        self.state = self.WALK
        if Hero_Axel.axel_image == None:
            Hero_Axel.axel_image = load_image('Hero/Axel_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Axel.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Axel.FRAMES_PER_ACTION * Hero_Axel.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
            self.dir = 2.0
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
            self.dir = 0
            if self.frame == 1:
                self.col = 0
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 2.0
            self.x = 100
            self.state = self.WALK

    def die(self, hero, frame_time):
        self.atk_time += frame_time

        if hero.frame == 0:
            if self.atk_time > 0.05:
                self.atk_time = 0
                self.health -= self.atk
                if self.health <= 0:
                    return True
        return False

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
    FRAMES_PER_ACTION = 6
    gunner_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self, x = 0):
        self.x, self.y = x, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 2.0
        self.atk_time = 0.0
        self.atk = 10
        self.col = 0
        self.health = 50
        self.state = self.WALK
        if Hero_Gunner.gunner_image == None:
            Hero_Gunner.gunner_image = load_image('Hero/Gunner_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Gunner.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Gunner.FRAMES_PER_ACTION * Hero_Gunner.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
            self.dir = 2.0
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
            self.dir = 0.0
            if self.frame == 1:
                self.col = 0
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 2.0
            self.x = 100
            self.state = self.WALK

    def die(self, hero, frame_time):
        self.atk_time += frame_time

        if hero.frame == 0:
            if self.atk_time > 0.05:
                self.atk_time = 0
                self.health -= self.atk
                if self.health <= 0:
                    return True
        return False

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
    FRAMES_PER_ACTION = 6
    fenrich_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self, x = 0):
        self.x, self.y = x, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 2.0
        self.atk_time = 0.0
        self.atk = 10
        self.col = 0
        self.health = 50
        self.state = self.WALK
        if Hero_Fenrich.fenrich_image == None:
            Hero_Fenrich.fenrich_image = load_image('Hero/Fenrich_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Fenrich.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Fenrich.FRAMES_PER_ACTION * Hero_Fenrich.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
            self.dir = 2.0
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
            self.dir = 0.0
            if self.frame == 1:
                self.col = 0
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0.0
            self.x = random.randint(1100, 1103)
            self.state = self.ATK
        elif self.x < 100:
            self.dir = 2.0
            self.x = 100
            self.state = self.WALK

    def die(self, hero, frame_time):
        self.atk_time += frame_time

        if hero.frame == 0:
            if self.atk_time > 0.05:
                self.atk_time = 0
                self.health -= self.atk
                if self.health <= 0:
                    return True
        return False

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
    FRAMES_PER_ACTION = 6
    ninja_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self, x = 0):
        self.x, self.y = x, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 2.0
        self.atk_time = 0.0
        self.atk = 10
        self.col = 0
        self.health = 50
        self.state = self.WALK
        if Hero_Ninja.ninja_image == None:
            Hero_Ninja.ninja_image = load_image('Hero/Ninja_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Ninja.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Ninja.FRAMES_PER_ACTION * Hero_Ninja.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
            self.dir = 2.0
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
            self.dir = 0.0
            if self.frame == 1:
                self.col = 0
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
                self.health -= self.atk
                if self.health <= 0:
                    return True
        return False

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
    FRAMES_PER_ACTION = 6
    pram_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self, x = 0):
        self.x, self.y = x, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 2.0
        self.atk_time = 0.0
        self.atk = 10
        self.col = 0
        self.health = 50
        self.state = self.WALK
        if Hero_Pram.pram_image == None:
            Hero_Pram.pram_image = load_image('Hero/Pram_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Pram.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Pram.FRAMES_PER_ACTION * Hero_Pram.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
            self.dir = 2.0
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
            self.dir = 0.0
            if self.frame == 1:
                self.col = 0
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
                self.health -= self.atk
                if self.health <= 0:
                    return True
        return False

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
    FRAMES_PER_ACTION = 6
    professor_image = None
    WALK, ATK, MTK, DIE = 3,2,1,0

    def __init__(self, x = 0):
        self.x, self.y = x, 340
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 2.0
        self.atk_time = 0.0
        self.atk = 10
        self.col = 0
        self.health = 50
        self.state = self.WALK
        if Hero_Prof.professor_image == None:
            Hero_Prof.professor_image = load_image('Hero/Professor_Sheet.png')

    def update(self, frame_time):
        distance = Hero_Prof.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Prof.FRAMES_PER_ACTION * Hero_Prof.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
            self.dir = 2.0
        elif self.state == self.ATK:
            self.frame = int(self.total_frames) % 4
            self.dir = 0.0
            if self.frame == 1:
                self.col = 0
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
            if self.atk_time > 0.07:
                self.atk_time = 0
                self.health -= self.atk
                if self.health <= 0:
                    return True
        return False

    def draw(self):
        self.professor_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 40, self.y - 85, self.x + 40, self.y + 65

