from pico2d import *
import random
# User Hero
class Main():

    RUN, ATK1, ATK2 = 3, 2, 1

    def __init__(self):

        self.load_time = 0
        self.x = 0
        self.y = 90
        self.state = self.RUN
        self.ani = 6
        self.frame = 0
        self.frame = (self.frame + 1) % self.ani
        self.h_knight_image = load_image("knight_sheet.png")

    def update(self):
        if(self.state == 3):
            self.ani = 6
            self.frame = (self.frame + 1) % self.ani
        elif(self.state == 2):
            self.ani = 4
            self.frame = (self.frame + 1) % self.ani
        elif(self.state == 1):
            self.ani = 5
            self.frame = (self.frame + 1) % self.ani

    def draw(self):
        self.h_knight_image.clip_draw(self.frame * 100, self.ani * 100, 100, 100, self.x ,self.y)



def handle_events():
        global running
        global x
        global key_down_right
        global key_down_left
        global key_down_up
        global key_down_down
        global key_down_upright

        events = get_events()
        for event in events:
            if event.type == SDL_QUIT:
                running = False
            elif event.type == SDL_KEYDOWN:
                if event.key == SDLK_RIGHT:
                    key_down_right = True
                    Main().state = Main().RUN

                elif event.key == SDLK_LEFT:
                    key_down_left = True
                    Main().state = Main().RUN

                elif event.key == SDLK_UP:
                    key_down_up = True
                    Main().state = Main().RUN

                elif event.key == SDLK_DOWN:
                    key_down_down = True
                    Main().state = Main().RUN

                elif event.key == SDLK_a:
                    Main().state = Main().ATK1

                elif event.key == SDLK_s:
                    Main().state = Main().ATK2

                elif event.key == SDLK_ESCAPE:
                    running = False

            elif event.type == SDL_KEYUP:
                if event.key == SDLK_RIGHT:
                    key_down_right = False

                elif event.key == SDLK_LEFT:
                    key_down_left = False

                elif event.key == SDLK_UP:
                    key_down_up = False

                elif event.key == SDLK_DOWN:
                    key_down_down = False

                elif event.key == SDLK_a:
                    Main().state = Main().RUN

                elif event.key == SDLK_s:
                    Main().state = Main().RUN


open_canvas()
grass = load_image('grass.png')

key_down_up = False
key_down_down = False
key_down_right = False
key_down_left = False
running = True




while (running):
    clear_canvas()
    grass.draw(400, 30)
    Main().draw()
    update_canvas()
    Main().update()

    handle_events()
    delay(0.07)


    if key_down_left == True:
        Main().x -= 5
    if key_down_right == True:
        Main().x += 5
    if key_down_down == True:
        Main().y -= 5
    if key_down_up == True:
        Main().y += 5

close_canvas()
