import game_framework
from pico2d import *


import Title_Scene

name = "StartScene"
credit_w_image = None

logo_time = 0.0

def enter():
    global credit_image, credit_w_image

    open_canvas(1280, 720)
    if credit_w_image == None:
        credit_w_image = load_image('Logo/Logo_kpu_credit_W.jpg')
        credit_image = load_image('Logo/Logo_kpu_credit.png')


def exit():
    global credit_image, credit_w_image
    del(credit_w_image)
    del(credit_image)
    close_canvas()

def update(frame_time):
    global name
    global logo_time
    logo_time += frame_time
    if (logo_time > 4.0):
        logo_time = 0
        game_framework.push_state(Title_Scene)


def draw(frame_time):
    clear_canvas()
    credit_w_image.draw(640, 360)
    if logo_time < 2:
        credit_image.opacify(logo_time * 0.5)
    else:
        credit_image.opacify(2 - (logo_time * 0.5))
    credit_image.draw(640, 360)
    update_canvas()

def handle_events(frame_time):
    events = get_events()


def pause(): pass
def resume(): pass




