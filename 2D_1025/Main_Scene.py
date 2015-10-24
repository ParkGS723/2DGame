import random
import json
import os
import game_framework
import Title_Scene
from pico2d import *

button_x, button_y = 0, 0
name = "MainScene"
u_Magician = None
h_Knight = None
font = None
gameUI = None
timer = False
chk_time = 0.0
class User_Magician:

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6

    u_image = None
    IDLE, ATTACK  = 3, 1

    def __init__(self):
        self.x, self.y = 95, 560
        self.frame = 0
        self.life_time = 0.0
        self.total_frames = 0.0
        self.state = self.IDLE
        if User_Magician.u_image == None:
            User_Magician.u_image = load_image('Hero/User_Magician.png')

    def update(self, frame_time):
        self.life_time += frame_time
        self.total_frames += User_Magician.FRAMES_PER_ACTION * User_Magician.ACTION_PER_TIME * frame_time
        if self.state == self.IDLE:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATTACK:
            self.frame = int(self.total_frames) % 4

    def draw(self):
        self.u_image.clip_draw(self.frame*118, self.state*100, 120, 120, self.x, self.y)

class Hero_Knight:
    PIXEL_PER_METER = (10.0 / 0.3)           # 10 pixel 30 cm
    RUN_SPEED_KMPH = 5.0                    # Km / Hour
    RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
    RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
    RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 0.5 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    h_image = None
    WALK, ATTACK, DAMAGE, DIE = 3,2,1,0

    def __init__(self):
        self.x, self.y = 0, 300
        self.frame = random.randint(0, 2)
        self.life_time = 0.0
        self.total_frames = 0.0
        self.dir = 1
        self.state = self.WALK
        if Hero_Knight.h_image == None:
            Hero_Knight.h_image = load_image('Hero/Knight_sheet.png')

    def update(self, frame_time):
        self.life_time += frame_time
        distance = Hero_Knight.RUN_SPEED_PPS * frame_time
        self.total_frames += Hero_Knight.FRAMES_PER_ACTION * Hero_Knight.ACTION_PER_TIME * frame_time
        if self.state == self.WALK:
            self.frame = int(self.total_frames) % 6
        elif self.state == self.ATTACK:
            self.frame = int(self.total_frames) % 4
        self.x += (self.dir * distance)

        if self.x > 1100:
            self.dir = 0
            self.x = random.randint(1100, 1103)
            self.state = self.ATTACK
            #print("Change Time: %f, Total Frames: %d" % (self.life_time, self.total_frames))
        elif self.x < 100:
            self.dir = 1
            self.x = 100
            self.state = self.WALK
            #print("Change Time: %f, Total Frames: %d" % (self.life_time, self.total_frames))


    def draw(self):
        self.h_image.clip_draw(self.frame*100, self.state*100, 110, 100, self.x, self.y)


def enter():
    global h_Knight, font
    global u_Magician
    global stage_background, gameUI, myCastle, enemyCastle, cloud
    global team1

    team1 = []
    u_Magician = User_Magician()

    h_Knight = Hero_Knight()
    gameUI = load_image('UI/GameUI.png')
    stage_background = load_image('Map/Stage2_bkg.png')
    myCastle = load_image('Map/MyCastle.png')
    enemyCastle = load_image('Map/EnemyCastle.png')
    cloud = load_image('Map/cloud.png')
    font = load_font('ENCR10B.TTF')
    game_framework.reset_time()

def exit():
    global u_Magician, h_Knight, font, myCastle, enemyCastle, stage_background, cloud, gameUI
    del(u_Magician)
    del(h_Knight)
    del(font)
    del(myCastle)
    del(enemyCastle)
    del(stage_background)
    del(cloud)
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
    global button_x, button_y, u_Magician
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
                u_Magician = User_Magician()
                u_Magician.state = u_Magician.ATTACK
                timer = False




def update(frame_time):
    global timer, chk_time
    h_Knight.update(frame_time)
    u_Magician.update(frame_time)
    if timer == False:
        chk_time += frame_time
    if chk_time > 1.0:
        timer = True
        chk_time = 0.0
        u_Magician.state = u_Magician.IDLE

def draw(frame_time):
    clear_canvas()
    stage_background.draw(400, 445)
    gameUI.draw(640, 50)
    myCastle.draw(100, 355)
    cloud.draw(90, 500)
    enemyCastle.draw(1200, 355)
    u_Magician.draw()
    for h_Knight in team1:
        h_Knight.update(frame_time)
        h_Knight.draw()
    update_canvas()





