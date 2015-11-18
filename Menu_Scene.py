import game_framework
from pico2d import *


import Main_Scene

mx, my = 0, 0
name = "MenuScene"
Title_bkg = None

def enter():
    global MainMenu_bkg, Menu_0, Menu_0_over, Menu_1, Menu_1_over, Menu_2, Menu_2_over, Menu_3, Menu_3_over
    MainMenu_bkg = load_image('UI/MainMenu.png')
    Menu_0 = load_image('UI/Menu_0.png')
    Menu_0_over = load_image('UI/Menu_0(over).png')
    Menu_1 = load_image('UI/Menu_1.png')
    Menu_1_over = load_image('UI/Menu_1(over).png')
    Menu_2 = load_image('UI/Menu_2.png')
    Menu_2_over = load_image('UI/Menu_2(over).png')
    Menu_3 = load_image('UI/Menu_3.png')
    Menu_3_over = load_image('UI/Menu_3(over).png')

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
                if 515 < mx < 765 and 165 < my < 335:
                    game_framework.change_state(Main_Scene)
               # if 195 < mx < 445 and 515 < my < 690:

               # if 510 < mx < 765 and 515 < my < 690:

                #if 830 < mx < 1090 and 515 < my < 690:


def update(frame_time):
    pass

def draw(frame_time):
    global mx, my
    global MainMenu_bkg, Menu_0, Menu_0_over, Menu_1, Menu_1_over, Menu_2, Menu_2_over, Menu_3, Menu_3_over
    clear_canvas()
    MainMenu_bkg.draw(640, 360)
    if 195 < mx < 445 and 515 < my < 690:
        Menu_0_over.draw(320, 600)
    else:
        Menu_0.draw(320, 600)

    if 510 < mx < 765 and 515 < my < 690:
        Menu_1_over.draw(640, 600)
    else:
        Menu_1.draw(640, 600)

    if 830 < mx < 1090 and 515 < my < 690:
        Menu_2_over.draw(960, 600)
    else:
        Menu_2.draw(960, 600)

    if 510 < mx < 765 and 160 < my < 340:
        Menu_3_over.draw(640, 250)
    else:
        Menu_3.draw(640, 250)

    update_canvas()



