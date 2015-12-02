import pico2d
import math
import json
import random
import game_framework

import Main_Scene

from pico2d import *

class Magic_Meteor:
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 2.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    magic_image = None

    def __init__(self, y = 0):
        self.x, self.y = 0, y
        self.frame = 0
        self.total_frames = 0.0
        self.state = 0
        if Magic_Meteor.magic_image == None:
            Magic_Meteor.magic_image = load_image('Magic/Magic_Meteor.png')

    def update(self, frame_time):
        self.total_frames += Magic_Meteor.FRAMES_PER_ACTION * Magic_Meteor.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 16
        if (self.y > 300):
            self.y -= 150 * frame_time

    def draw(self):
        self.magic_image.clip_draw(self.frame*70, self.state*100, 60, 80, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 30, self.y - 30, self.x + 30, self.y + 30

class Magic_Tornado:
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 2.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    magic_image = None

    def __init__(self):
        self.x, self.y = 100, 370
        self.frame = 0
        self.total_frames = 0.0
        self.state = 0
        if Magic_Tornado.magic_image == None:
            Magic_Tornado.magic_image = load_image('Magic/Magic_Tornado.png')

    def update(self, frame_time):
        self.total_frames += Magic_Meteor.FRAMES_PER_ACTION * Magic_Meteor.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 10
        if (self.x < 1600):
            self.x += 150 * frame_time

    def draw(self):
        self.magic_image.clip_draw(self.frame*280, self.state*100, 240, 320, self.x, self.y)

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 100, self.y - 100, self.x + 60, self.y + 80

class Magic_Explosion:
    def __init__(self):
        self.x, self.y = 0, 0

    def update(self):
        pass

    def draw(self):
        pass

    def draw_bb(self):
        draw_rectangle(*self.get_bb())

    def get_bb(self):
        return self.x - 1280, self.y - 720, self.x + 1280, self.y + 720