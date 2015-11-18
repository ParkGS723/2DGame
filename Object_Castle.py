import pico2d
import math
import json
import random
import game_framework

import Main_Scene

from pico2d import *

class User_Castle:
    castle_image = None
    def __init__(self):
        if User_Castle.castle_image == None:
            User_Castle.castle_image = load_image('Map/MyCastle.png')

    def update(self, frame_time):
        pass

    def draw(self):
        self.castle_image.draw(100, 355)

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
