import random
import json
import os

import game_framework
import title_state

from pico2d import *


button_x, button_y = 0, 0
name = "MainState"

h_Knight = None
grass = None
font = None
backimage = None
gameUI = None


class Grass:
    def __init__(self):
        self.image = load_image('grass.png')

    def draw(self):
        self.image.draw(640, 240)



class Hero_Knight:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 10.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    image = None

    WALK, ATTACK, DAMAGE, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 0, 320
        self.frame = random.randint(0, 7)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1
        self.state = self.WALK
        if Hero_Knight.image == None:
            Hero_Knight.image = load_image('knight_sheet.png')


    def update(self, frame_time):
        self.life_time += frame_time
        distance = Hero_Knight.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Knight.FRAMES_PER_ACTION * Hero_Knight.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATTACK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1200:
            self.dir = 0
            self.x = random.randint(1200, 1203)
            self.state = self.ATTACK
            print("Change Time: %f, Total Frames: %d" % (self.life_time, self.total_frames))
        elif self.x < 0:
            self.dir = 1
            self.x = 0
            self.state = self.WALK
            print("Change Time: %f, Total Frames: %d" % (self.life_time, self.total_frames))


    def draw(self):
        self.image.clip_draw(self.frame*100, self.state*100, 110, 100, self.x, self.y)




def enter():
    global h_Knight, grass, font, backimage, gameUI, button
    global team1

    team1 = []
    grass = Grass()
    h_Knight = Hero_Knight()
    gameUI = load_image('GameUI.png')
    backimage = load_image('main_background.jpg')
    font = load_font('ENCR10B.TTF')
    game_framework.reset_time()

def exit():
    global h_Knight, grass, font, gameUI
    del(h_Knight)
    del(grass)
    del(font)
    del(gameUI)


def pause():
    pass

def resume():
    pass

def button_click():
    global h_Knight
    if 80 < button_x < 180 and 80 < button_y < 180:
        h_Knight = Hero_Knight()
        if len(team1) < 10:
            h_Knight.draw()
            team1.append(h_Knight)

def handle_events(frame_time):
    global button_x, button_y
    events = get_events()

    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            button_x, button_y = event.x, 720 - event.y
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
            game_framework.change_state(title_state)
        elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT):
            print(button_x, button_y)
            button_click()

def update(frame_time):
    h_Knight.update(frame_time)

def draw(frame_time):
    clear_canvas()
    backimage.draw(400, 500)
    grass.draw()
    gameUI.draw(640, 50)
    for h_Knight in team1:
        h_Knight.update(frame_time)
        h_Knight.draw()
    update_canvas()





