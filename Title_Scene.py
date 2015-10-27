import game_framework
from pico2d import *


import Main_Scene


name = "TitleScene"
Title_bkg = None

def enter():
    global Title_bkg
    Title_bkg = load_image('UI/GameTitle.jpg')

def exit():
    global Title_bkg
    del(Title_bkg)


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
                game_framework.change_state(Main_Scene)



def update(frame_time):
    pass


def draw(frame_time):
    global Title_bkg
    clear_canvas()
    Title_bkg.draw(640, 360)
    update_canvas()



