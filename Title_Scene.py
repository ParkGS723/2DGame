import game_framework
from pico2d import *


import Menu_Scene

mx, my = 0, 0
name = "TitleScene"
Title_bkg = None

def enter():
    global Title_bkg, Title_start, Title_start_over
    Title_bkg = load_image('UI/GameTitle.jpg')
    Title_start = load_image('UI/Title_Play.png')
    Title_start_over = load_image('UI/Title_Play(over).png')


def exit():
    global Title_bkg
    del(Title_bkg)


def pause():
    pass

def resume():
    pass


def handle_events(frame_time):
    events = get_events()
    global mx, my
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            mx, my = event.x, 720 - event.y
        else:
            if (event.type, event.key) == (SDL_KEYDOWN, SDLK_ESCAPE):
                game_framework.quit()
            elif (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT ):
                print(mx, my)
                if 470 < mx < 800 and 185 < my < 315:
                    game_framework.change_state(Menu_Scene)

def update(frame_time):
    pass


def draw(frame_time):
    global mx, my
    global Title_bkg
    clear_canvas()
    Title_bkg.draw(640, 360)

    if 470 < mx < 800 and 185 < my < 315:
        Title_start_over.draw(640, 250)
    else:
        Title_start.draw(640, 250)

    update_canvas()



