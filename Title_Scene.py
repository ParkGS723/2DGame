import game_framework
from pico2d import *


import Menu_Scene

mx, my = 0, 0
name = "TitleScene"
Title_bkg = None

class TitleBackGround:
    def __init__(self):
        self.x, self.y = 640, 360
        self.image = load_image('UI/GameTitle.png')
        self.bgm = load_music('Sound/title_bgm.mp3')
        self.bgm.set_volume(60)
        self.bgm.repeat_play()

    def draw(self):
        self.image.clip_draw(0, 0, 1280, 720, self.x, self.y)


def enter():
    global Title_start, Title_start_over, title_bg
    title_bg = TitleBackGround()
    Title_start = load_image('UI/GameStart.png')
    Title_start_over = load_image('UI/GameStart(over).png')

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
    global mx, my, title_bg

    clear_canvas()
    title_bg.draw()

    if 550 < mx < 750 and 115 < my < 315:
        Title_start_over.draw(640, 360)
    else:
        Title_start.draw(640, 360)

    update_canvas()



