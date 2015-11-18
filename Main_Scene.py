import random
import json
import os
import game_framework
import Title_Scene
import Object_Hero
import Object_Enemy
import Object_User
import Object_Castle

from pico2d import *


button_x, button_y = 0, 0
name = "MainScene"
background = None
font = None
gameUI = None
timer = False
chk_time = 0.0
load_time = 0.0
gold = 0

class Magic_Meteor:
    TIME_PER_ACTION = 0.5
    ACTION_PER_TIME = 2.0 / TIME_PER_ACTION
    FRAMES_PER_ACTION = 6
    magic_image = None

    def __init__(self):
        self.x, self.y = 0, 800
        self.frame = 0
        self.total_frames = 0.0
        self.state = 0
        if Magic_Meteor.magic_image == None:
            Magic_Meteor.magic_image = load_image('Magic/Magic_Meteor.png')

    def update(self, frame_time):
        self.total_frames += Magic_Meteor.FRAMES_PER_ACTION * Magic_Meteor.ACTION_PER_TIME * frame_time
        self.frame = int(self.total_frames) % 16
        if(self.y > 300):
            self.y -= 0.2

    def draw(self):
        self.magic_image.clip_draw(self.frame*70, self.state*100, 60, 80, self.x, self.y)

def enter():
    global hero_adell, hero_archer, hero_axel, hero_asuka, hero_fenrich, hero_gunner, hero_ninja, hero_pram, hero_prof
    global m_Skeleton, enemy_castle, enemy_slime, enemy_zombie, enemy_golem, enemy_pringer, enemy_demon, enemy_succubus
    global user_valva, user_castle
    global stage_background, gameUI, cloud, ui_button, gold, font
    global my_team
    global hero_group1, hero_group2, hero_group3, hero_group4, hero_group5, hero_group6, hero_group7, hero_group8, hero_group9
    global enemy_group1, enemy_group2, enemy_group3, enemy_group4, enemy_group5
    global my_magic
    global magic_meteor

    #obj_data_txt = '                                   \
    #{                                                  \
    #    "Hero_Adell": {y":340, "atk":2, "health":50},  \
    #    "Enemy_Slime": {"y":330, "atk":2, "health":50} \
    #}                                                  \
    #'
    #object_data = json.load(obj_data_txt)
    gold = 10000

    hero_group1 = []
    hero_group2 = []
    hero_group3 = []
    hero_group4 = []
    hero_group5 = []
    hero_group6 = []
    hero_group7 = []
    hero_group8 = []
    hero_group9 = []

    enemy_group1 = []
    enemy_group2 = []
    enemy_group3 = []
    enemy_group4 = []
    my_team = []
    my_magic = []

    user_valva = Object_User.User_Valvatorez()

    user_castle = Object_Castle.User_Castle()
    enemy_castle = Object_Castle.Enemy_Castle()

    hero_adell = Object_Hero.Hero_Adell()
    hero_archer = Object_Hero.Hero_Archer()
    hero_asuka = Object_Hero.Hero_Asuka()
    hero_axel = Object_Hero.Hero_Axel()
    hero_fenrich = Object_Hero.Hero_Fenrich()
    hero_gunner = Object_Hero.Hero_Gunner()
    hero_ninja = Object_Hero.Hero_Ninja()
    hero_pram = Object_Hero.Hero_Pram()
    hero_prof = Object_Hero.Hero_Prof()

    magic_meteor = Magic_Meteor()

    enemy_slime = Object_Enemy.Enemy_Slime()
    enemy_zombie = Object_Enemy.Enemy_Zombie()
    enemy_golem = Object_Enemy.Enemy_Golem()
    enemy_pringer = Object_Enemy.Enemy_Pringer()
    enemy_demon = Object_Enemy.Enemy_Demon()
    enemy_succubus = Object_Enemy.Enemy_Succubus()

    ui_button = load_image('UI/UI_Button.png')
    gameUI = load_image('UI/GameUI.png')
    stage_background = load_image('Map/Stage2_bkg.png')
    cloud = load_image('Map/cloud.png')
    font = load_font('ENCR10B.TTF')
    game_framework.reset_time()

def exit():
    global hero_adell, hero_archer, hero_axel, hero_asuka, hero_fenrich, hero_gunner, hero_ninja, hero_pram, hero_prof
    global user_valva, user_castle, magic_meteor
    global enemy_castle, enemy_zombie, enemy_golem, enemy_pringer, enemy_demon, enemy_succubus
    del(user_valva)
    del(user_castle)
    del(hero_adell)
    del(hero_archer)
    del(hero_asuka)
    del(hero_axel)
    del(hero_fenrich)
    del(hero_gunner)
    del(hero_ninja)
    del(hero_pram)
    del(hero_prof)
    del(magic_meteor)
    del(enemy_castle)
    del(enemy_zombie)
    del(enemy_golem)
    del(enemy_pringer)
    del(enemy_demon)
    del(enemy_succubus)

def pause():
    pass

def resume():
    pass

def EnemyLevel_System(frame_time):
    global load_time, summon_random
    load_time += frame_time
    if load_time > 0.7:
        summon_random = random.randint(0, 100)
        load_time = 0
    print(summon_random)
    if 0 < summon_random < 50 and len(enemy_group1) < 6:
        enemy_slime = Object_Enemy.Enemy_Slime(x = 1200)
        enemy_group1.append(enemy_slime)

    if 0 < summon_random < 25 and len(enemy_group2) < 4:
        enemy_zombie = Object_Enemy.Enemy_Zombie(x = 1250)
        enemy_group2.append(enemy_zombie)

    if 0 < summon_random < 15 and len(enemy_group3) < 2:
        enemy_golem = Object_Enemy.Enemy_Golem(x = 1250)
        enemy_group3.append(enemy_golem)

def object_state(frame_time):
    for hero_adell in hero_group1:
        if hero_adell.col > 0:
            hero_adell.state = 2
        elif hero_adell.col <= 0:
            hero_adell.state = 3

    for hero_archer in hero_group2:
        if hero_archer.col > 0:
            hero_archer.state = hero_archer.ATK
        elif hero_archer.col <= 0:
            hero_archer.state = hero_archer.WALK

    for hero_asuka in hero_group3:
        if hero_asuka.col > 0:
            hero_asuka.state = hero_asuka.ATK
        elif hero_asuka.col <= 0:
            hero_asuka.state = hero_asuka.WALK

    for hero_axel in hero_group4:
        if hero_axel.col > 0:
            hero_axel.state = hero_axel.ATK
        elif hero_axel.col <= 0:
            hero_axel.state = hero_axel.WALK

    for hero_gunner in hero_group5:
        if hero_gunner.col > 0:
            hero_gunner.state = hero_gunner.ATK
        elif hero_gunner.col <= 0:
            hero_gunner.state = hero_gunner.WALK

    for hero_fenrich in hero_group6:
        if hero_fenrich.col > 0:
            hero_fenrich.state = hero_fenrich.ATK
        elif hero_fenrich.col <= 0:
            hero_fenrich.state = hero_fenrich.WALK

    for hero_ninja in hero_group7:
        if hero_ninja.col > 0:
            hero_ninja.state = hero_ninja.ATK
        elif hero_ninja.col <= 0:
            hero_ninja.state = hero_ninja.WALK

    for hero_pram in hero_group8:
        if hero_pram.col > 0:
            hero_pram.state = hero_pram.ATK
        elif hero_pram.col <= 0:
            hero_pram.state = hero_pram.WALK

    for hero_prof in hero_group9:
        if hero_prof.col > 0:
            hero_prof.state = hero_prof.ATK
        elif hero_prof.col <= 0:
            hero_prof.state = hero_prof.WALK

    for enemy_slime in enemy_group1:
        if enemy_slime.col > 0:
            enemy_slime.state = enemy_slime.ATK
        elif enemy_slime.col <= 0:
            enemy_slime.state = enemy_slime.WALK

    for enemy_zombie in enemy_group2:
        if enemy_zombie.col > 0:
            enemy_zombie.state = enemy_zombie.ATK
        elif enemy_zombie.col <= 0:
            enemy_zombie.state = enemy_zombie.WALK

    for enemy_golem in enemy_group3:
        if enemy_golem.col > 0:
            enemy_golem.state = enemy_golem.ATK
        elif enemy_golem.col <= 0:
            enemy_golem.state = enemy_golem.WALK

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def collide_enter(frame_time):
    for enemy_slime in enemy_group1:
        for hero_adell in hero_group1:
            if collide(hero_adell, enemy_slime) == True:
                enemy_slime.col += 1
                hero_adell.col += 1

                if hero_adell.die(enemy_slime, frame_time) == True:
                    hero_group1.remove(hero_adell)
                    enemy_slime.col = 0

                elif enemy_slime.die(hero_adell, frame_time) == True:
                    enemy_group1.remove(enemy_slime)
                    hero_adell.col = 0

        for hero_archer in hero_group2:
            if collide(hero_archer, enemy_slime) == True:
                enemy_slime.col += 1
                hero_archer.col += 1

                if hero_archer.die(enemy_slime, frame_time) == True:
                    hero_group2.remove(hero_archer)
                    enemy_slime.col = 0

                elif enemy_slime.die(hero_archer, frame_time) == True:
                    enemy_group1.remove(enemy_slime)
                    hero_archer.col = 0

        for hero_asuka in hero_group3:
            if collide(hero_asuka, enemy_slime) == True:
                enemy_slime.col += 1
                hero_asuka.col += 1

                if hero_asuka.die(enemy_slime, frame_time) == True:
                    hero_group3.remove(hero_asuka)
                    enemy_slime.col = 0

                elif enemy_slime.die(hero_asuka, frame_time) == True:
                    enemy_group1.remove(enemy_slime)
                    hero_asuka.col = 0

        for hero_axel in hero_group4:
            if collide(hero_axel, enemy_slime) == True:
                enemy_slime.col += 1
                hero_axel.col += 1

                if hero_axel.die(enemy_slime, frame_time) == True:
                    hero_group4.remove(hero_axel)
                    enemy_slime.col = 0

                elif enemy_slime.die(hero_axel, frame_time) == True:
                    enemy_group1.remove(enemy_slime)
                    hero_axel.col = 0

        for hero_gunner in hero_group5:
            if collide(hero_gunner, enemy_slime) == True:
                enemy_slime.col += 1
                hero_gunner.col += 1

                if hero_gunner.die(enemy_slime, frame_time) == True:
                    hero_group5.remove(hero_gunner)
                    enemy_slime.col = 0

                elif enemy_slime.die(hero_gunner, frame_time) == True:
                    enemy_group1.remove(enemy_slime)
                    hero_gunner.col = 0

        for hero_fenrich in hero_group6:
            if collide(hero_fenrich, enemy_slime) == True:
                enemy_slime.col += 1
                hero_fenrich.col += 1

                if hero_fenrich.die(enemy_slime, frame_time) == True:
                    hero_group6.remove(hero_fenrich)
                    enemy_slime.col = 0

                elif enemy_slime.die(hero_fenrich, frame_time) == True:
                    enemy_group1.remove(enemy_slime)
                    hero_fenrich.col = 0

        for hero_ninja in hero_group7:
            if collide(hero_ninja, enemy_slime) == True:
                enemy_slime.col += 1
                hero_ninja.col += 1

                if hero_ninja.die(enemy_slime, frame_time) == True:
                    hero_group7.remove(hero_ninja)
                    enemy_slime.col = 0

                elif enemy_slime.die(hero_ninja, frame_time) == True:
                    enemy_group1.remove(enemy_slime)
                    hero_ninja.col = 0

        for hero_pram in hero_group8:
            if collide(hero_pram, enemy_slime) == True:
                enemy_slime.col += 1
                hero_pram.col += 1

                if hero_pram.die(enemy_slime, frame_time) == True:
                    hero_group8.remove(hero_pram)
                    enemy_slime.col = 0

                elif enemy_slime.die(hero_pram, frame_time) == True:
                    enemy_group1.remove(enemy_slime)
                    hero_pram.col = 0

        for hero_prof in hero_group9:
            if collide(hero_prof, enemy_slime) == True:
                enemy_slime.col += 1
                hero_prof.col += 1

                if hero_prof.die(enemy_slime, frame_time) == True:
                    hero_group9.remove(hero_prof)
                    enemy_slime.col = 0

                elif enemy_slime.die(hero_prof, frame_time) == True:
                    enemy_group1.remove(enemy_slime)
                    hero_prof.col = 0

    for enemy_zombie in enemy_group2:
        for hero_adell in hero_group1:
            if collide(hero_adell, enemy_zombie) == True:
                enemy_zombie.col += 1
                hero_adell.col += 1

                if hero_adell.die(enemy_zombie, frame_time) == True:
                    hero_group1.remove(hero_adell)
                    enemy_zombie.col = 0

                elif enemy_zombie.die(hero_adell, frame_time) == True:
                    enemy_group2.remove(enemy_zombie)
                    hero_adell.col = 0

        for hero_archer in hero_group2:
            if collide(hero_archer, enemy_zombie) == True:
                enemy_zombie.col += 1
                hero_archer.col += 1

                if hero_archer.die(enemy_zombie, frame_time) == True:
                    hero_group2.remove(hero_archer)
                    enemy_zombie.col = 0

                elif enemy_zombie.die(hero_archer, frame_time) == True:
                    enemy_group2.remove(enemy_zombie)
                    hero_archer.col = 0

        for hero_asuka in hero_group3:
            if collide(hero_asuka, enemy_zombie) == True:
                enemy_zombie.col += 1
                hero_asuka.col += 1

                if hero_asuka.die(enemy_zombie, frame_time) == True:
                    hero_group3.remove(hero_asuka)
                    enemy_zombie.col = 0

                elif enemy_zombie.die(hero_asuka, frame_time) == True:
                    enemy_group2.remove(enemy_zombie)
                    hero_asuka.col = 0

        for hero_axel in hero_group4:
            if collide(hero_axel, enemy_zombie) == True:
                enemy_zombie.col += 1
                hero_axel.col += 1

                if hero_axel.die(enemy_zombie, frame_time) == True:
                    hero_group4.remove(hero_axel)
                    enemy_zombie.col = 0

                elif enemy_zombie.die(hero_axel, frame_time) == True:
                    enemy_group2.remove(enemy_zombie)
                    hero_axel.col = 0

        for hero_gunner in hero_group5:
            if collide(hero_gunner, enemy_zombie) == True:
                enemy_zombie.col += 1
                hero_gunner.col += 1

                if hero_gunner.die(enemy_zombie, frame_time) == True:
                    hero_group5.remove(hero_gunner)
                    enemy_zombie.col = 0

                elif enemy_zombie.die(hero_gunner, frame_time) == True:
                    enemy_group2.remove(enemy_zombie)
                    hero_gunner.col = 0

        for hero_fenrich in hero_group6:
            if collide(hero_fenrich, enemy_zombie) == True:
                enemy_zombie.col += 1
                hero_fenrich.col += 1

                if hero_fenrich.die(enemy_zombie, frame_time) == True:
                    hero_group6.remove(hero_fenrich)
                    enemy_zombie.col = 0

                elif enemy_zombie.die(hero_fenrich, frame_time) == True:
                    enemy_group2.remove(enemy_zombie)
                    hero_fenrich.col = 0

        for hero_ninja in hero_group7:
            if collide(hero_ninja, enemy_zombie) == True:
                enemy_zombie.col += 1
                hero_ninja.col += 1

                if hero_ninja.die(enemy_zombie, frame_time) == True:
                    hero_group7.remove(hero_ninja)
                    enemy_zombie.col = 0

                elif enemy_zombie.die(hero_ninja, frame_time) == True:
                    enemy_group2.remove(enemy_zombie)
                    hero_ninja.col = 0

        for hero_pram in hero_group8:
            if collide(hero_pram, enemy_zombie) == True:
                enemy_zombie.col += 1
                hero_pram.col += 1

                if hero_pram.die(enemy_zombie, frame_time) == True:
                    hero_group8.remove(hero_pram)
                    enemy_zombie.col = 0

                elif enemy_zombie.die(hero_pram, frame_time) == True:
                    enemy_group2.remove(enemy_zombie)
                    hero_pram.col = 0

        for hero_prof in hero_group9:
            if collide(hero_prof, enemy_zombie) == True:
                enemy_zombie.col += 1
                hero_prof.col += 1

                if hero_prof.die(enemy_zombie, frame_time) == True:
                    hero_group9.remove(hero_prof)
                    enemy_zombie.col = 0

                elif enemy_zombie.die(hero_prof, frame_time) == True:
                    enemy_group2.remove(enemy_zombie)
                    hero_prof.col = 0

    for enemy_golem in enemy_group3:
        for hero_adell in hero_group1:
            if collide(hero_adell, enemy_golem) == True:
                enemy_golem.col += 1
                hero_adell.col += 1

                if hero_adell.die(enemy_golem, frame_time) == True:
                    hero_group1.remove(hero_adell)
                    enemy_golem.col = 0

                elif enemy_golem.die(hero_adell, frame_time) == True:
                    enemy_group3.remove(enemy_golem)
                    hero_adell.col = 0

        for hero_archer in hero_group2:
            if collide(hero_archer, enemy_golem) == True:
                enemy_golem.col += 1
                hero_archer.col += 1

                if hero_archer.die(enemy_golem, frame_time) == True:
                    hero_group2.remove(hero_archer)
                    enemy_golem.col = 0

                elif enemy_golem.die(hero_archer, frame_time) == True:
                    enemy_group3.remove(enemy_golem)
                    hero_archer.col = 0

        for hero_asuka in hero_group3:
            if collide(hero_asuka, enemy_golem) == True:
                enemy_golem.col += 1
                hero_asuka.col += 1

                if hero_asuka.die(enemy_golem, frame_time) == True:
                    hero_group3.remove(hero_asuka)
                    enemy_golem.col = 0

                elif enemy_golem.die(hero_asuka, frame_time) == True:
                    enemy_group3.remove(enemy_golem)
                    hero_asuka.col = 0

        for hero_axel in hero_group4:
            if collide(hero_axel, enemy_golem) == True:
                enemy_golem.col += 1
                hero_axel.col += 1

                if hero_axel.die(enemy_golem, frame_time) == True:
                    hero_group4.remove(hero_axel)
                    enemy_golem.col = 0

                elif enemy_golem.die(hero_axel, frame_time) == True:
                    enemy_group3.remove(enemy_golem)
                    hero_axel.col = 0

        for hero_gunner in hero_group5:
            if collide(hero_gunner, enemy_golem) == True:
                enemy_golem.col += 1
                hero_gunner.col += 1

                if hero_gunner.die(enemy_golem, frame_time) == True:
                    hero_group5.remove(hero_gunner)
                    enemy_golem.col = 0

                elif enemy_golem.die(hero_gunner, frame_time) == True:
                    enemy_group3.remove(enemy_golem)
                    hero_gunner.col = 0

        for hero_fenrich in hero_group6:
            if collide(hero_fenrich, enemy_golem) == True:
                enemy_golem.col += 1
                hero_fenrich.col += 1

                if hero_fenrich.die(enemy_golem, frame_time) == True:
                    hero_group6.remove(hero_fenrich)
                    enemy_golem.col = 0

                elif enemy_golem.die(hero_fenrich, frame_time) == True:
                    enemy_group3.remove(enemy_golem)
                    hero_fenrich.col = 0

        for hero_ninja in hero_group7:
            if collide(hero_ninja, enemy_golem) == True:
                enemy_golem.col += 1
                hero_ninja.col += 1

                if hero_ninja.die(enemy_golem, frame_time) == True:
                    hero_group7.remove(hero_ninja)
                    enemy_golem.col = 0

                elif enemy_golem.die(hero_ninja, frame_time) == True:
                    enemy_group3.remove(enemy_golem)
                    hero_ninja.col = 0

        for hero_pram in hero_group8:
            if collide(hero_pram, enemy_golem) == True:
                enemy_golem.col += 1
                hero_pram.col += 1

                if hero_pram.die(enemy_golem, frame_time) == True:
                    hero_group8.remove(hero_pram)
                    enemy_golem.col = 0

                elif enemy_golem.die(hero_pram, frame_time) == True:
                    enemy_group3.remove(enemy_golem)
                    hero_pram.col = 0

        for hero_prof in hero_group9:
            if collide(hero_prof, enemy_golem) == True:
                enemy_golem.col += 1
                hero_prof.col += 1

                if hero_prof.die(enemy_golem, frame_time) == True:
                    hero_group9.remove(hero_prof)
                    enemy_golem.col = 0

                elif enemy_golem.die(hero_prof, frame_time) == True:
                    enemy_group3.remove(enemy_golem)
                    hero_prof.col = 0
def button_click():
    global hero_adell, hero_archer, hero_asuka, hero_axel, hero_fenrich, hero_gunner, hero_ninja, hero_pram, hero_prof, gold

    if 49 < button_x < 170 and 80 < button_y < 210:
        hero_adell = Object_Hero.Hero_Adell(x = 0)
        gold = gold - 100
        if len(hero_group1) < 10:
            hero_adell.draw()
            hero_group1.append(hero_adell)

    if 179 < button_x < 310 and 85 < button_y < 210:
        hero_archer = Object_Hero.Hero_Archer(x = 0)
        gold = gold - 300
        if len(hero_group2) < 50:
            hero_group2.append(hero_archer)

    if 309 < button_x < 440 and 85 < button_y < 210:
        hero_asuka = Object_Hero.Hero_Asuka(x = 0)
        gold = gold - 500
        if len(hero_group3) < 50:
            hero_group3.append(hero_asuka)

    if 439 < button_x < 560 and 85 < button_y < 210:
        hero_axel = Object_Hero.Hero_Axel(x = 0)
        gold = gold - 1000
        if len(hero_group4) < 50:
            hero_group4.append(hero_axel)

    if 569 < button_x < 690 and 85 < button_y < 210:
        gold = gold - 1500
        hero_gunner = Object_Hero.Hero_Gunner(x = 0)
        if len(hero_group5) < 50:
            hero_group5.append(hero_gunner)

    if 699 < button_x < 820 and 85 < button_y < 210:
        gold = gold - 2000
        hero_fenrich = Object_Hero.Hero_Fenrich(x = 0)
        if len(hero_group6) < 50:
            hero_group6.append(hero_fenrich)

    if 829 < button_x < 950 and 85 < button_y < 210:
        gold = gold - 3000
        hero_ninja = Object_Hero.Hero_Ninja(x = 0)
        if len(hero_group7) < 50:
            hero_group7.append(hero_ninja)

    if 959 < button_x < 1080 and 85 < button_y < 210:
        gold = gold - 5000
        hero_pram = Object_Hero.Hero_Pram(x = 0)
        if len(hero_group8) < 50:
            hero_group8.append(hero_pram)

    if 1089 < button_x < 1209 and 85 < button_y < 210:
        gold = gold - 7000
        hero_prof = Object_Hero.Hero_Prof(x = 0)
        if len(hero_group9) < 50:
            hero_group9.append(hero_prof)

    if 100 < button_x < 700 and 300 < button_y < 768:
         m_meteor = Magic_Meteor()
         if len(my_magic) < 100:
             m_meteor.x = button_x
             my_magic.append(m_meteor)

def handle_events(frame_time):
    global button_x, button_y, user_valva
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
                user_valva.state = user_valva.ATK
                timer = False

def update(frame_time):
    global chk_time, load_time, gold, timer
    load_time += frame_time

    if load_time > 0.7:
        EnemyLevel_System(frame_time)
        load_time = 0

    user_valva.update(frame_time)
    magic_meteor.update(frame_time)
    object_state(frame_time)
    collide_enter(frame_time)
    gold += (frame_time * 100)
    if timer == False:
        chk_time += frame_time
    if chk_time > 1.0:
        timer = True
        chk_time = 0.0
        user_valva.state = user_valva.IDLE

def draw(frame_time):
    global gold
    score = 0
    clear_canvas()
    stage_background.draw(400, 445)
    gameUI.draw(640, 70)
    cloud.draw(90, 500)
    ui_button.draw(1230, 690)
    user_castle.draw()
    user_valva.draw()
    enemy_castle.draw()

    for enemy_slime in enemy_group1:
        enemy_slime.update(frame_time)
        enemy_slime.draw()
        enemy_slime.draw_bb()

    for enemy_zombie in enemy_group2:
        enemy_zombie.update(frame_time)
        enemy_zombie.draw()
        enemy_zombie.draw_bb()

    for enemy_golem in enemy_group3:
        enemy_golem.update(frame_time)
        enemy_golem.draw()
        enemy_golem.draw_bb()


    font.draw(360, 55, '%1.f' % score)
    font.draw(515, 55, '%1.f' % gold)
    for m_meteor in my_magic:
        m_meteor.update(frame_time)
        m_meteor.draw()

    for hero_adell in hero_group1:
        hero_adell.update(frame_time)
        hero_adell.draw()
        hero_adell.draw_bb()

    for hero_archer in hero_group2:
        hero_archer.update(frame_time)
        hero_archer.draw()
        hero_archer.draw_bb()

    for hero_asuka in hero_group3:
        hero_asuka.update(frame_time)
        hero_asuka.draw()
        hero_asuka.draw_bb()

    for hero_axel in hero_group4:
        hero_axel.update(frame_time)
        hero_axel.draw()
        hero_axel.draw_bb()

    for hero_fenrich in hero_group5:
        hero_fenrich.update(frame_time)
        hero_fenrich.draw()
        hero_fenrich.draw_bb()

    for hero_gunner in hero_group6:
        hero_gunner.update(frame_time)
        hero_gunner.draw()
        hero_gunner.draw_bb()

    for hero_ninja in hero_group7:
        hero_ninja.update(frame_time)
        hero_ninja.draw()
        hero_ninja.draw_bb()

    for hero_pram in hero_group8:
        hero_pram.update(frame_time)
        hero_pram.draw()
        hero_pram.draw_bb()

    for hero_prof in hero_group9:
        hero_prof.update(frame_time)
        hero_prof.draw()
        hero_prof.draw_bb()

    user_valva.draw_bb()
    update_canvas()






