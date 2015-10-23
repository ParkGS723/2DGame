import game_framework
from pico2d import *


import title_state

name = "StartState"
image = None
logo_time = 0.0

def enter():
    global image
    open_canvas(1280, 720)
    image = load_image('kpu_credit.png')


def exit():
    global image
    del(image)
    close_canvas()

def update(frame_time):
    global name
    global logo_time

    if (logo_time > 2.0):
        logo_time = 0
        game_framework.push_state(title_state)
        #game_framework.quit()
    logo_time += frame_time

def draw(frame_time):
    global image
    clear_canvas()
    image.draw(400, 300)
    update_canvas()

def handle_events(frame_time):
    events = get_events()


def pause(): pass
def resume(): pass




