import pico2d
import math
import json
import random
import game_framework

import Main_Scene

from pico2d import *

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
        elif self.state == self.MTK:
            self.frame = int(self.total_frames) % 4
        elif self.state == self.DIE:
            self.frame = int(self.total_frames) % 1
    def draw(self):
        self.user_image.clip_draw(self.frame*120, self.state*180, 120, 180, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 50, self.y - 70, self.x + 50, self.y + 70