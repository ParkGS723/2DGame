import random
import json
import os
import game_framework
import Title_Scene
import Menu_Scene
import Object_Hero
import Object_Enemy
import Object_User
import Object_Castle
import Object_Magic
import Object_Castle
import Upgrade_Manager
import Stage_Background

from pico2d import *


#Main

result_font = None
time_font = None
font = None
timer = False
coll_chk = None
coll_chk_pic = None
m_exp = None
m_exp_1 = None
m_exp_2 = None
m_exp_3 = None
m_exp_4 = None
m_exp_5 = None
m_exp_6 = None
m_exp_7 = None
m_exp_8 = None
m_exp_9 = None
m_exp_10 = None
m_exp_11 = None
m_exp_12 = None
m_exp_13 = None
m_exp_14 = None
m_exp_15 = None
m_exp_16 = None
m_exp_17 = None
m_exp_18 = None
m_exp_19 = None

button_x, button_y = 0, 0
name = "MainScene"

chk_time = 0.0
load_time = 0.0
play_time = 0.0
m_load_time = 0.0
cool_time_1 = 0.0
cool_time_2 = 0.0
cool_time_3 = 0.0

gold_manager = 1.0
gold = 0
score = 0
meteor_numb = 6
tornado_numb = 4
explosion_numb = 2
result_score = 0
meteor_limit = 0
tornado_limit = 0
explosion_limit = 0

def enter():
    global hero_adell, hero_archer, hero_axel, hero_asuka, hero_fenrich, hero_gunner, hero_ninja, hero_pram, hero_prof
    global m_Skeleton, enemy_castle, enemy_slime, enemy_zombie, enemy_golem, enemy_pringer, enemy_demon, enemy_succubus
    global user_valva, user_castle, random_stage
    global stage_background, stage2_background, stage3_background, stage4_background, stage5_background, cloud, gold, font, time_font, result_font
    global gameUI_easy, gameUI_normal, gameUI_hard, score, star_bar, effect_die
    global hero_group1, hero_group2, hero_group3, hero_group4, hero_group5, hero_group6, hero_group7, hero_group8, hero_group9
    global enemy_group1, enemy_group2, enemy_group3, enemy_group4, enemy_group5, enemy_group6
    global magic_group1, magic_group2, magic_group3, castle_group1, castle_group2, effect_group1
    global magic_meteor, magic_tornado, magic_explosion, ui_timer, gamesound
    global magic_exp_image_1, magic_exp_image_2, magic_exp_image_3, magic_exp_image_4, magic_exp_image_5, magic_exp_image_6, magic_exp_image_7, magic_exp_image_8
    global magic_exp_image_9, magic_exp_image_10, magic_exp_image_11, magic_exp_image_12, magic_exp_image_13, magic_exp_image_14, magic_exp_image_15, magic_exp_image_16, magic_exp_image_17, magic_exp_image_18, magic_exp_image_19
    global ui_adell_pic, ui_adell_pic_over, ui_archer_pic, ui_archer_pic_over, ui_asuka_pic, ui_asuka_pic_over, ui_axel_pic, ui_axel_pic_over, ui_fenrich_pic, ui_fenrich_pic_over
    global ui_gunner_pic, ui_gunner_pic_over, ui_ninja_pic, ui_ninja_pic_over, ui_pram_pic, ui_pram_pic_over, ui_prof_pic, ui_prof_pic_over
    global ui_meteor_pic, ui_meteor_pic_over, ui_tornado_pic, ui_tornado_pic_over, ui_explosion_pic, ui_explosion_pic_over, ui_goldup, ui_goldup_over
    global upgrade_manager, hero_buy_manager, upgradestar, bgm, team_data, team_data_txt
    global ui_victory, ui_defeat, ui_restart, ui_restart_over, ui_gotown, ui_gotown_over, ui_gotown2, ui_gotown2_over, ui_collchk, ui_collchk_over

    bgm = load_music('Sound/game_bgm.mp3')
    bgm.set_volume(75)
    bgm.repeat_play()
    gold = 30000
    score = 10000
    upgrade_manager = Upgrade_Manager.UpgradeStar_Main()
    random_stage = random.randint(1, 50)
    gamesound = GameSound()
    castle_group1 = []
    castle_group2 = []

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
    enemy_group5 = []
    enemy_group6 = []

    magic_group1 = []
    magic_group2 = []
    magic_group3 = []

    user_valva = Object_User.User_Valvatorez()
    user_castle = Object_Castle.User_Castle()
    enemy_castle = Object_Castle.Enemy_Castle()
    star_bar = Object_Magic.Star_Bar()

    hero_adell = Object_Hero.Hero_Adell()
    hero_archer = Object_Hero.Hero_Archer()
    hero_asuka = Object_Hero.Hero_Asuka()
    hero_axel = Object_Hero.Hero_Axel()
    hero_fenrich = Object_Hero.Hero_Fenrich()
    hero_gunner = Object_Hero.Hero_Gunner()
    hero_ninja = Object_Hero.Hero_Ninja()
    hero_pram = Object_Hero.Hero_Pram()
    hero_prof = Object_Hero.Hero_Prof()

    effect_die = Object_Magic.Effect_Die()
    magic_meteor = Object_Magic.Magic_Meteor()
    magic_tornado = Object_Magic.Magic_Tornado()
    magic_explosion = Object_Magic.Magic_Explosion()

    enemy_slime = Object_Enemy.Enemy_Slime()
    enemy_zombie = Object_Enemy.Enemy_Zombie()
    enemy_golem = Object_Enemy.Enemy_Golem()
    enemy_pringer = Object_Enemy.Enemy_Pringer()
    enemy_demon = Object_Enemy.Enemy_Demon()
    enemy_succubus = Object_Enemy.Enemy_Succubus()

    gameUI_easy = load_image('UI/GameUI_easy_set.png')
    gameUI_normal = load_image('UI/GameUI_medium_set.png')
    gameUI_hard = load_image('UI/GameUI_hard_set.png')

    ui_victory = load_image('UI/UI_victory.png')
    ui_defeat = load_image('UI/UI_defeat.png')
    ui_restart = load_image('UI/UI_restart.png')
    ui_restart_over = load_image('UI/UI_restart(over).png')
    ui_gotown = load_image('UI/UI_gotown.png')
    ui_gotown_over = load_image('UI/UI_gotown(over).png')
    ui_gotown2 = load_image('UI/UI_gotown2.png')
    ui_gotown2_over = load_image('UI/UI_gotown2(over).png')
    ui_collchk = load_image('UI/UI_collchk.png')
    ui_collchk_over = load_image('UI/UI_collchk(over).png')
    ui_timer = load_image('UI/UI_time.png')
    ui_adell_pic = load_image('UI/UI_Adell.png')
    ui_adell_pic_over = load_image('UI/UI_Adell(Over).png')
    ui_archer_pic = load_image('UI/UI_Archer.png')
    ui_archer_pic_over = load_image('UI/UI_Archer(Over).png')
    ui_asuka_pic = load_image('UI/UI_Asuka.png')
    ui_asuka_pic_over = load_image('UI/UI_Asuka(Over).png')
    ui_axel_pic = load_image('UI/UI_Axel.png')
    ui_axel_pic_over = load_image('UI/UI_Axel(Over).png')
    ui_fenrich_pic = load_image('UI/UI_Fenrich.png')
    ui_fenrich_pic_over = load_image('UI/UI_Fenrich(Over).png')
    ui_gunner_pic = load_image('UI/UI_Gunner.png')
    ui_gunner_pic_over = load_image('UI/UI_Gunner(Over).png')
    ui_ninja_pic = load_image('UI/UI_Ninja.png')
    ui_ninja_pic_over = load_image('UI/UI_Ninja(Over).png')
    ui_pram_pic = load_image('UI/UI_Pram.png')
    ui_pram_pic_over = load_image('UI/UI_Pram(Over).png')
    ui_prof_pic = load_image('UI/UI_Prof.png')
    ui_prof_pic_over = load_image('UI/UI_Prof(Over).png')
    ui_meteor_pic = load_image('UI/UI_Meteor.png')
    ui_meteor_pic_over = load_image('UI/UI_Meteor(Over).png')
    ui_tornado_pic = load_image('UI/UI_Tornado.png')
    ui_tornado_pic_over = load_image('UI/UI_Tornado(Over).png')
    ui_explosion_pic = load_image('UI/UI_Explosion.png')
    ui_explosion_pic_over = load_image('UI/UI_Explosion(Over).png')
    ui_goldup = load_image('UI/UI_goldup.png')
    ui_goldup_over = load_image('UI/UI_goldup(Over).png')
    magic_exp_image_1 = load_image('Magic/Magic_Explosion_1.png')
    magic_exp_image_2 = load_image('Magic/Magic_Explosion_2.png')
    magic_exp_image_3 = load_image('Magic/Magic_Explosion_3.png')
    magic_exp_image_4 = load_image('Magic/Magic_Explosion_4.png')
    magic_exp_image_5 = load_image('Magic/Magic_Explosion_5.png')
    magic_exp_image_6 = load_image('Magic/Magic_Explosion_6.png')
    magic_exp_image_7 = load_image('Magic/Magic_Explosion_7.png')
    magic_exp_image_8 = load_image('Magic/Magic_Explosion_8.png')
    magic_exp_image_9 = load_image('Magic/Magic_Explosion_9.png')
    magic_exp_image_10 = load_image('Magic/Magic_Explosion_10.png')
    magic_exp_image_11 = load_image('Magic/Magic_Explosion_11.png')
    magic_exp_image_12 = load_image('Magic/Magic_Explosion_12.png')
    magic_exp_image_13 = load_image('Magic/Magic_Explosion_13.png')
    magic_exp_image_14 = load_image('Magic/Magic_Explosion_14.png')
    magic_exp_image_15 = load_image('Magic/Magic_Explosion_15.png')
    magic_exp_image_16 = load_image('Magic/Magic_Explosion_16.png')
    magic_exp_image_17 = load_image('Magic/Magic_Explosion_17.png')
    magic_exp_image_18 = load_image('Magic/Magic_Explosion_18.png')
    magic_exp_image_19 = load_image('Magic/Magic_Explosion_19.png')

    stage_background = Stage_Background.BackGround()
    stage2_background = Stage_Background.BackGround2()
    stage3_background = Stage_Background.BackGround3()
    stage4_background = Stage_Background.BackGround3()
    stage5_background = Stage_Background.BackGround3()

    cloud = load_image('Map/cloud.png')
    font = load_font('ENCR10B.TTF')
    result_font = load_font('ENCR10B.TTF', 30)
    time_font = load_font('ENCR10B.TTF', 30)
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

class GameSound:
    bomb_sound = None
    goldup_sound = None
    meteor_sound = None
    punch2_sound = None
    slap_sound = None
    tornado_sound = None
    hero1_sound = None
    hero2_sound = None
    hero3_sound = None
    hero4_sound = None
    hero5_sound = None
    hero6_sound = None
    hero7_sound = None
    hero8_sound = None
    hero9_sound = None
    victory_sound = None
    defeat_sound = None

    def __init__(self):
        if GameSound.victory_sound == None:
            GameSound.victory_sound = load_wav('Sound/Stage_Victory.wav')
            GameSound.victory_sound.set_volume(80)

        if GameSound.defeat_sound == None:
            GameSound.defeat_sound = load_wav('Sound/Stage_Defeat.wav')
            GameSound.defeat_sound.set_volume(80)

        if GameSound.bomb_sound == None:
            GameSound.bomb_sound = load_wav('Sound/game_bomb.wav')
            GameSound.bomb_sound.set_volume(100)

        if GameSound.goldup_sound == None:
            GameSound.goldup_sound = load_wav('Sound/game_goldup.wav')
            GameSound.goldup_sound.set_volume(64)

        if GameSound.meteor_sound == None:
            GameSound.meteor_sound = load_wav('Sound/game_meteor.wav')
            GameSound.meteor_sound.set_volume(64)

        if GameSound.punch2_sound == None:
            GameSound.punch2_sound = load_wav('Sound/game_punch2.wav')
            GameSound.punch2_sound.set_volume(5)

        if GameSound.slap_sound == None:
            GameSound.slap_sound = load_wav('Sound/game_slap.wav')
            GameSound.slap_sound.set_volume(5)

        if GameSound.tornado_sound == None:
            GameSound.tornado_sound = load_wav('Sound/game_Tornado.wav')
            GameSound.tornado_sound.set_volume(64)

        if GameSound.hero1_sound == None:
            GameSound.hero1_sound = load_wav('Sound/game_hero1.wav')
            GameSound.hero1_sound.set_volume(100)

        if GameSound.hero2_sound == None:
            GameSound.hero2_sound = load_wav('Sound/game_hero2.wav')
            GameSound.hero2_sound.set_volume(100)

        if GameSound.hero3_sound == None:
            GameSound.hero3_sound = load_wav('Sound/game_hero3.wav')
            GameSound.hero3_sound.set_volume(100)

        if GameSound.hero4_sound == None:
            GameSound.hero4_sound = load_wav('Sound/game_hero4.wav')
            GameSound.hero4_sound.set_volume(100)

        if GameSound.hero5_sound == None:
            GameSound.hero5_sound = load_wav('Sound/game_hero5.wav')
            GameSound.hero5_sound.set_volume(100)

        if GameSound.hero6_sound == None:
            GameSound.hero6_sound = load_wav('Sound/game_hero6.wav')
            GameSound.hero6_sound.set_volume(100)

        if GameSound.hero7_sound == None:
            GameSound.hero7_sound = load_wav('Sound/game_hero7.wav')
            GameSound.hero7_sound.set_volume(100)

        if GameSound.hero8_sound == None:
            GameSound.hero8_sound = load_wav('Sound/game_hero8.wav')
            GameSound.hero8_sound.set_volume(100)

        if GameSound.hero9_sound == None:
            GameSound.hero9_sound = load_wav('Sound/game_hero9.wav')
            GameSound.hero9_sound.set_volume(100)

    def bomb(self):
        self.bomb_sound.play()

    def goldup(self):
        self.goldup_sound.play()

    def meteor(self):
        self.meteor_sound.play()

    def punch2(self):
        self.punch2_sound.play()

    def slap(self):
        self.slap_sound.play()

    def tornado(self):
        self.tornado_sound.play()

    def hero1(self):
        self.hero1_sound.play()

    def hero2(self):
        self.hero2_sound.play()

    def hero3(self):
        self.hero3_sound.play()

    def hero4(self):
        self.hero4_sound.play()

    def hero5(self):
        self.hero5_sound.play()

    def hero6(self):
        self.hero6_sound.play()

    def hero7(self):
        self.hero7_sound.play()

    def hero8(self):
        self.hero8_sound.play()

    def hero9(self):
        self.hero9_sound.play()

    def victory(self):
        self.victory_sound.play()

    def defeat(self):
        self.defeat_sound.play()

def collide(a, b):
    left_a, bottom_a, right_a, top_a = a.get_bb()
    left_b, bottom_b, right_b, top_b = b.get_bb()

    if left_a > right_b : return False
    if right_a < left_b : return False
    if top_a < bottom_b : return False
    if bottom_a > top_b : return False

    return True

def collide_enter(frame_time):
    global score, result_score

    for magic_meteor in magic_group1:
        if magic_meteor.y < 300:
            magic_group1.remove(magic_meteor)
        for enemy_slime in enemy_group1:
            if collide(enemy_slime, magic_meteor) == True:
                enemy_group1.remove(enemy_slime)

        for enemy_zombie in enemy_group2:
            if collide(enemy_zombie, magic_meteor) == True:
                enemy_group2.remove(enemy_zombie)
        for enemy_golem in enemy_group3:
            if collide(enemy_golem, magic_meteor) == True:
                enemy_group3.remove(enemy_golem)
        for enemy_pringer in enemy_group4:
            if collide(enemy_pringer, magic_meteor) == True:
                enemy_group4.remove(enemy_pringer)
        for enemy_demon in enemy_group5:
            if collide(enemy_demon, magic_meteor) == True:
                enemy_group5.remove(enemy_demon)
        for enemy_succubus in enemy_group6:
            if collide(enemy_succubus, magic_meteor) == True:
                enemy_group6.remove(enemy_succubus)

    for magic_tornado in magic_group2:
        if magic_tornado.x > 1500:
            magic_group2.remove(magic_tornado)
        for enemy_slime in enemy_group1:
            if collide(enemy_slime, magic_tornado) == True:
                enemy_slime.x += 250 * frame_time
                if enemy_slime.x > 1500:
                    score += 100
                    star_bar.StarBar += 1
                    result_score += 100
                    enemy_group1.remove(enemy_slime)
        for enemy_zombie in enemy_group2:
            if collide(enemy_zombie, magic_tornado) == True:
                enemy_zombie.x += 250 * frame_time
                if enemy_zombie.x > 1500:
                    score += 200
                    star_bar.StarBar += 2
                    result_score += 200
                    enemy_group2.remove(enemy_zombie)
        for enemy_golem in enemy_group3:
            if collide(enemy_golem, magic_tornado) == True:
                enemy_golem.x += 250 * frame_time
                if enemy_golem.x > 1500:
                    score += 500
                    star_bar.StarBar += 5
                    result_score += 500
                    enemy_group3.remove(enemy_golem)
        for enemy_pringer in enemy_group4:
            if collide(enemy_pringer, magic_tornado) == True:
                enemy_pringer.x += 250 * frame_time
                if enemy_pringer.x > 1500:
                    score += 700
                    star_bar.StarBar += 7
                    result_score += 700
                    enemy_group4.remove(enemy_pringer)

    for magic_explosion in magic_group3:
        for enemy_slime in enemy_group1:
            if collide(enemy_slime, magic_explosion) == True:
                if m_exp_10 == True:
                    score += 100
                    star_bar.StarBar += 1
                    result_score += 100
                    enemy_group1.remove(enemy_slime)
        for enemy_zombie in enemy_group2:
            if collide(enemy_zombie, magic_explosion) == True:
                if m_exp_10 == True:
                    score += 200
                    star_bar.StarBar += 2
                    result_score += 200
                    enemy_group2.remove(enemy_zombie)
        for enemy_golem in enemy_group3:
            if collide(enemy_golem, magic_explosion) == True:
                if m_exp_10 == True:
                    score += 500
                    star_bar.StarBar += 5
                    result_score += 500
                    enemy_group3.remove(enemy_golem)
        for enemy_pringer in enemy_group4:
            if collide(enemy_pringer, magic_explosion) == True:
                if m_exp_10 == True:
                    score += 700
                    star_bar.StarBar += 7
                    result_score += 700
                    enemy_group4.remove(enemy_pringer)
        for enemy_demon in enemy_group5:
            if collide(enemy_demon, magic_explosion) == True:
                if m_exp_10 == True:
                    score += 1000
                    star_bar.StarBar += 10
                    result_score += 1000
                    enemy_group5.remove(enemy_demon)
        for enemy_succbus in enemy_group6:
            if collide(enemy_succbus, magic_explosion) == True:
                if m_exp_10 == True:
                    score += 2000
                    star_bar.StarBar += 20
                    result_score += 2000
                    enemy_group6.remove(enemy_succbus)


    for enemy_slime in enemy_group1:
        if collide(enemy_slime, user_castle) == True:
            user_castle.user_hp -= 1
            user_castle.user_hpbar -= 1
            enemy_group1.remove(enemy_slime)

    for enemy_zombie in enemy_group2:
        if collide(enemy_zombie, user_castle) == True:
            user_castle.user_hp -= 1
            user_castle.user_hpbar -= 1
            enemy_group2.remove(enemy_zombie)

    for enemy_golem in enemy_group3:
        if collide(enemy_golem, user_castle) == True:
            user_castle.user_hp -= 1
            user_castle.user_hpbar -= 1
            enemy_group3.remove(enemy_golem)

    for enemy_pringer in enemy_group4:
        if collide(enemy_pringer, user_castle) == True:
            user_castle.user_hp -= 1
            user_castle.user_hpbar -= 1
            enemy_group4.remove(enemy_pringer)

    for enemy_demon in enemy_group5:
        if collide(enemy_demon, user_castle) == True:
            user_castle.user_hp -= 1
            user_castle.user_hpbar -= 1
            enemy_group5.remove(enemy_demon)

    for enemy_succubus in enemy_group6:
        if collide(enemy_succubus, user_castle) == True:
            user_castle.user_hp -= 1
            user_castle.user_hpbar -= 1
            enemy_group6.remove(enemy_succubus)


    for hero_adell in hero_group1:
        if collide(hero_adell, enemy_castle) == True:
            enemy_castle.enemy_hp -= 1
            enemy_castle.enemy_hpbar -= 1
            hero_group1.remove(hero_adell)


    for hero_archer in hero_group2:
        if collide(hero_archer, enemy_castle) == True:
            enemy_castle.enemy_hp -= 1
            enemy_castle.enemy_hpbar -= 1
            hero_group2.remove(hero_archer)

    for hero_asuka in hero_group3:
        if collide(hero_asuka, enemy_castle) == True:
            enemy_castle.enemy_hp -= 1
            enemy_castle.enemy_hpbar -= 1
            hero_group3.remove(hero_asuka)

    for hero_axel in hero_group4:
        if collide(hero_axel, enemy_castle) == True:
            enemy_castle.enemy_hp -= 1
            enemy_castle.enemy_hpbar -= 1
            hero_group4.remove(hero_axel)

    for hero_gunner in hero_group5:
        if collide(hero_gunner, enemy_castle) == True:
            enemy_castle.enemy_hp -= 1
            enemy_castle.enemy_hpbar -= 1
            hero_group5.remove(hero_gunner)

    for hero_fenrich in hero_group6:
        if collide(hero_fenrich, enemy_castle) == True:
            enemy_castle.enemy_hp -= 1
            enemy_castle.enemy_hpbar -= 1
            hero_group6.remove(hero_fenrich)

    for hero_ninja in hero_group7:
        if collide(hero_ninja, enemy_castle) == True:
            enemy_castle.enemy_hp -= 1
            enemy_castle.enemy_hpbar -= 1
            hero_group7.remove(hero_ninja)

    for hero_pram in hero_group8:
        if collide(hero_pram, enemy_castle) == True:
            enemy_castle.enemy_hp -= 1
            enemy_castle.enemy_hpbar -= 1
            hero_group8.remove(hero_pram)

    for hero_prof in hero_group9:
        if collide(hero_prof, enemy_castle) == True:
            enemy_castle.enemy_hp -= 1
            enemy_castle.enemy_hpbar -= 1
            hero_group9.remove(hero_prof)

    for enemy_slime in enemy_group1:
        for hero_adell in hero_group1:
            if collide(hero_adell, enemy_slime) == True:
                gamesound.punch2()
                enemy_slime.check = 1
                hero_adell.check = 1
                if hero_adell.die(enemy_slime, frame_time) == True:
                    hero_group1.remove(hero_adell)
                    enemy_slime.check = 0

                elif enemy_slime.die(hero_adell, frame_time) == True:
                    score += 100
                    star_bar.StarBar += 1
                    result_score += 100
                    enemy_group1.remove(enemy_slime)
                    hero_adell.check = 0

        for hero_archer in hero_group2:
            if collide(hero_archer, enemy_slime) == True:
                gamesound.punch2()
                enemy_slime.check += 1
                hero_archer.check += 1

                if hero_archer.die(enemy_slime, frame_time) == True:
                    hero_group2.remove(hero_archer)
                    enemy_slime.check = 0

                elif enemy_slime.die(hero_archer, frame_time) == True:
                    score += 100
                    star_bar.StarBar += 1
                    result_score += 100
                    enemy_group1.remove(enemy_slime)
                    hero_archer.check = 0

        for hero_asuka in hero_group3:
            if collide(hero_asuka, enemy_slime) == True:
                gamesound.punch2()
                enemy_slime.check += 1
                hero_asuka.check += 1

                if hero_asuka.die(enemy_slime, frame_time) == True:
                    hero_group3.remove(hero_asuka)
                    enemy_slime.check = 0

                elif enemy_slime.die(hero_asuka, frame_time) == True:
                    score += 100
                    star_bar.StarBar += 1
                    result_score += 100
                    enemy_group1.remove(enemy_slime)
                    hero_asuka.check = 0

        for hero_axel in hero_group4:
            if collide(hero_axel, enemy_slime) == True:
                gamesound.punch2()
                enemy_slime.check += 1
                hero_axel.check += 1

                if hero_axel.die(enemy_slime, frame_time) == True:
                    hero_group4.remove(hero_axel)
                    enemy_slime.check = 0

                elif enemy_slime.die(hero_axel, frame_time) == True:
                    score += 100
                    star_bar.StarBar += 1
                    result_score += 100
                    enemy_group1.remove(enemy_slime)
                    hero_axel.check = 0

        for hero_gunner in hero_group5:
            if collide(hero_gunner, enemy_slime) == True:
                gamesound.punch2()
                enemy_slime.check += 1
                hero_gunner.check += 1

                if hero_gunner.die(enemy_slime, frame_time) == True:
                    hero_group5.remove(hero_gunner)
                    enemy_slime.check = 0

                elif enemy_slime.die(hero_gunner, frame_time) == True:
                    score += 100
                    star_bar.StarBar += 1
                    result_score += 100
                    enemy_group1.remove(enemy_slime)
                    hero_gunner.check = 0

        for hero_fenrich in hero_group6:
            if collide(hero_fenrich, enemy_slime) == True:
                gamesound.punch2()
                enemy_slime.check += 1
                hero_fenrich.check += 1

                if hero_fenrich.die(enemy_slime, frame_time) == True:
                    hero_group6.remove(hero_fenrich)
                    enemy_slime.check = 0

                elif enemy_slime.die(hero_fenrich, frame_time) == True:
                    score += 100
                    star_bar.StarBar += 1
                    result_score += 100
                    enemy_group1.remove(enemy_slime)
                    hero_fenrich.check = 0

        for hero_ninja in hero_group7:
            if collide(hero_ninja, enemy_slime) == True:
                gamesound.punch2()
                enemy_slime.check += 1
                hero_ninja.check += 1

                if hero_ninja.die(enemy_slime, frame_time) == True:
                    hero_group7.remove(hero_ninja)
                    enemy_slime.check = 0

                elif enemy_slime.die(hero_ninja, frame_time) == True:
                    score += 100
                    star_bar.StarBar += 1
                    result_score += 100
                    enemy_group1.remove(enemy_slime)
                    hero_ninja.check = 0

        for hero_pram in hero_group8:
            if collide(hero_pram, enemy_slime) == True:
                gamesound.punch2()
                enemy_slime.check += 1
                hero_pram.check += 1

                if hero_pram.die(enemy_slime, frame_time) == True:
                    hero_group8.remove(hero_pram)
                    enemy_slime.check = 0

                elif enemy_slime.die(hero_pram, frame_time) == True:
                    score += 100
                    star_bar.StarBar += 1
                    result_score += 100
                    enemy_group1.remove(enemy_slime)
                    hero_pram.check = 0

        for hero_prof in hero_group9:
            if collide(hero_prof, enemy_slime) == True:
                gamesound.punch2()
                enemy_slime.check += 1
                hero_prof.check += 1

                if hero_prof.die(enemy_slime, frame_time) == True:
                    hero_group9.remove(hero_prof)
                    enemy_slime.check = 0

                elif enemy_slime.die(hero_prof, frame_time) == True:
                    score += 300
                    star_bar.StarBar += 3
                    result_score += 300
                    enemy_group1.remove(enemy_slime)
                    hero_prof.check = 0

    for enemy_zombie in enemy_group2:
        for hero_adell in hero_group1:
            if collide(hero_adell, enemy_zombie) == True:
                gamesound.punch2()
                enemy_zombie.check += 1
                hero_adell.check += 1

                if hero_adell.die(enemy_zombie, frame_time) == True:
                    hero_group1.remove(hero_adell)
                    enemy_zombie.check = 0

                elif enemy_zombie.die(hero_adell, frame_time) == True:
                    score += 300
                    star_bar.StarBar += 3
                    result_score += 300
                    enemy_group2.remove(enemy_zombie)
                    hero_adell.check = 0

        for hero_archer in hero_group2:
            if collide(hero_archer, enemy_zombie) == True:
                gamesound.punch2()
                enemy_zombie.check += 1
                hero_archer.check += 1

                if hero_archer.die(enemy_zombie, frame_time) == True:
                    hero_group2.remove(hero_archer)
                    enemy_zombie.check = 0

                elif enemy_zombie.die(hero_archer, frame_time) == True:
                    score += 300
                    star_bar.StarBar += 3
                    result_score += 300
                    enemy_group2.remove(enemy_zombie)
                    hero_archer.check = 0

        for hero_asuka in hero_group3:
            if collide(hero_asuka, enemy_zombie) == True:
                gamesound.punch2()
                enemy_zombie.check += 1
                hero_asuka.check += 1

                if hero_asuka.die(enemy_zombie, frame_time) == True:
                    hero_group3.remove(hero_asuka)
                    enemy_zombie.check = 0

                elif enemy_zombie.die(hero_asuka, frame_time) == True:
                    score += 300
                    star_bar.StarBar += 3
                    result_score += 300
                    enemy_group2.remove(enemy_zombie)
                    hero_asuka.check = 0

        for hero_axel in hero_group4:
            if collide(hero_axel, enemy_zombie) == True:
                gamesound.punch2()
                enemy_zombie.check += 1
                hero_axel.check += 1

                if hero_axel.die(enemy_zombie, frame_time) == True:
                    hero_group4.remove(hero_axel)
                    enemy_zombie.check = 0

                elif enemy_zombie.die(hero_axel, frame_time) == True:
                    score += 300
                    star_bar.StarBar += 3
                    result_score += 300
                    enemy_group2.remove(enemy_zombie)
                    hero_axel.check = 0

        for hero_gunner in hero_group5:
            if collide(hero_gunner, enemy_zombie) == True:
                gamesound.punch2()
                enemy_zombie.check += 1
                hero_gunner.check += 1

                if hero_gunner.die(enemy_zombie, frame_time) == True:
                    hero_group5.remove(hero_gunner)
                    enemy_zombie.check = 0

                elif enemy_zombie.die(hero_gunner, frame_time) == True:
                    score += 300
                    star_bar.StarBar += 3
                    result_score += 300
                    enemy_group2.remove(enemy_zombie)
                    hero_gunner.check = 0

        for hero_fenrich in hero_group6:
            if collide(hero_fenrich, enemy_zombie) == True:
                gamesound.punch2()
                enemy_zombie.check += 1
                hero_fenrich.check += 1

                if hero_fenrich.die(enemy_zombie, frame_time) == True:
                    hero_group6.remove(hero_fenrich)
                    enemy_zombie.check = 0

                elif enemy_zombie.die(hero_fenrich, frame_time) == True:
                    score += 300
                    star_bar.StarBar += 3
                    result_score += 300
                    enemy_group2.remove(enemy_zombie)
                    hero_fenrich.check = 0

        for hero_ninja in hero_group7:
            if collide(hero_ninja, enemy_zombie) == True:
                gamesound.punch2()
                enemy_zombie.check += 1
                hero_ninja.check += 1

                if hero_ninja.die(enemy_zombie, frame_time) == True:
                    hero_group7.remove(hero_ninja)
                    enemy_zombie.check = 0

                elif enemy_zombie.die(hero_ninja, frame_time) == True:
                    score += 300
                    star_bar.StarBar += 3
                    result_score += 300
                    enemy_group2.remove(enemy_zombie)
                    hero_ninja.check = 0

        for hero_pram in hero_group8:
            if collide(hero_pram, enemy_zombie) == True:
                gamesound.punch2()
                enemy_zombie.check += 1
                hero_pram.check += 1

                if hero_pram.die(enemy_zombie, frame_time) == True:
                    hero_group8.remove(hero_pram)
                    enemy_zombie.check = 0

                elif enemy_zombie.die(hero_pram, frame_time) == True:
                    score += 300
                    star_bar.StarBar += 3
                    result_score += 300
                    enemy_group2.remove(enemy_zombie)
                    hero_pram.check = 0

        for hero_prof in hero_group9:
            if collide(hero_prof, enemy_zombie) == True:
                gamesound.punch2()
                enemy_zombie.check += 1
                hero_prof.check += 1

                if hero_prof.die(enemy_zombie, frame_time) == True:
                    hero_group9.remove(hero_prof)
                    enemy_zombie.check = 0

                elif enemy_zombie.die(hero_prof, frame_time) == True:
                    score += 300
                    star_bar.StarBar += 3
                    result_score += 300
                    enemy_group2.remove(enemy_zombie)
                    hero_prof.check = 0

    for enemy_golem in enemy_group3:
        for hero_adell in hero_group1:
            if collide(hero_adell, enemy_golem) == True:
                gamesound.punch2()
                enemy_golem.check += 1
                hero_adell.check += 1

                if hero_adell.die(enemy_golem, frame_time) == True:
                    hero_group1.remove(hero_adell)
                    enemy_golem.check = 0


                elif enemy_golem.die(hero_adell, frame_time) == True:
                    score += 500
                    star_bar.StarBar += 5
                    result_score += 500
                    enemy_group3.remove(enemy_golem)
                    hero_adell.check = 0

        for hero_archer in hero_group2:
            if collide(hero_archer, enemy_golem) == True:
                gamesound.punch2()
                enemy_golem.check += 1
                hero_archer.check += 1

                if hero_archer.die(enemy_golem, frame_time) == True:
                    hero_group2.remove(hero_archer)
                    enemy_golem.check = 0

                elif enemy_golem.die(hero_archer, frame_time) == True:
                    score += 500
                    star_bar.StarBar += 5
                    result_score += 500
                    enemy_group3.remove(enemy_golem)
                    hero_archer.check = 0

        for hero_asuka in hero_group3:
            if collide(hero_asuka, enemy_golem) == True:
                gamesound.punch2()
                enemy_golem.check += 1
                hero_asuka.check += 1

                if hero_asuka.die(enemy_golem, frame_time) == True:
                    hero_group3.remove(hero_asuka)
                    enemy_golem.check = 0

                elif enemy_golem.die(hero_asuka, frame_time) == True:
                    score += 500
                    star_bar.StarBar += 5
                    result_score += 500
                    enemy_group3.remove(enemy_golem)
                    hero_asuka.check = 0

        for hero_axel in hero_group4:
            if collide(hero_axel, enemy_golem) == True:
                gamesound.punch2()
                enemy_golem.check += 1
                hero_axel.check += 1

                if hero_axel.die(enemy_golem, frame_time) == True:
                    hero_group4.remove(hero_axel)
                    enemy_golem.check = 0

                elif enemy_golem.die(hero_axel, frame_time) == True:
                    score += 500
                    star_bar.StarBar += 5
                    result_score += 500
                    enemy_group3.remove(enemy_golem)
                    hero_axel.check = 0

        for hero_gunner in hero_group5:
            if collide(hero_gunner, enemy_golem) == True:
                gamesound.punch2()
                enemy_golem.check += 1
                hero_gunner.check += 1

                if hero_gunner.die(enemy_golem, frame_time) == True:
                    hero_group5.remove(hero_gunner)
                    enemy_golem.check = 0

                elif enemy_golem.die(hero_gunner, frame_time) == True:
                    score += 500
                    star_bar.StarBar += 5
                    result_score += 500
                    enemy_group3.remove(enemy_golem)
                    hero_gunner.check = 0

        for hero_fenrich in hero_group6:
            if collide(hero_fenrich, enemy_golem) == True:
                gamesound.punch2()
                enemy_golem.check += 1
                hero_fenrich.check += 1

                if hero_fenrich.die(enemy_golem, frame_time) == True:
                    hero_group6.remove(hero_fenrich)
                    enemy_golem.check = 0

                elif enemy_golem.die(hero_fenrich, frame_time) == True:
                    score += 500
                    star_bar.StarBar += 5
                    result_score += 500
                    enemy_group3.remove(enemy_golem)
                    hero_fenrich.check = 0

        for hero_ninja in hero_group7:
            if collide(hero_ninja, enemy_golem) == True:
                gamesound.punch2()
                enemy_golem.check += 1
                hero_ninja.check += 1

                if hero_ninja.die(enemy_golem, frame_time) == True:
                    hero_group7.remove(hero_ninja)
                    enemy_golem.check = 0

                elif enemy_golem.die(hero_ninja, frame_time) == True:
                    score += 500
                    star_bar.StarBar += 5
                    result_score += 500
                    enemy_group3.remove(enemy_golem)
                    hero_ninja.check = 0

        for hero_pram in hero_group8:
            if collide(hero_pram, enemy_golem) == True:
                gamesound.punch2()
                enemy_golem.check += 1
                hero_pram.check += 1

                if hero_pram.die(enemy_golem, frame_time) == True:
                    hero_group8.remove(hero_pram)
                    enemy_golem.check = 0

                elif enemy_golem.die(hero_pram, frame_time) == True:
                    score += 500
                    star_bar.StarBar += 5
                    result_score += 500
                    enemy_group3.remove(enemy_golem)
                    hero_pram.check = 0

        for hero_prof in hero_group9:
            if collide(hero_prof, enemy_golem) == True:
                gamesound.punch2()
                enemy_golem.check += 1
                hero_prof.check += 1

                if hero_prof.die(enemy_golem, frame_time) == True:
                    hero_group9.remove(hero_prof)
                    enemy_golem.check = 0

                elif enemy_golem.die(hero_prof, frame_time) == True:
                    score += 500
                    star_bar.StarBar += 5
                    result_score += 500
                    enemy_group3.remove(enemy_golem)
                    hero_prof.check = 0

    for enemy_pringer in enemy_group4:
        for hero_adell in hero_group1:
            if collide(hero_adell, enemy_pringer) == True:
                gamesound.punch2()
                enemy_pringer.check += 1
                hero_adell.check += 1

                if hero_adell.die(enemy_pringer, frame_time) == True:
                    hero_group1.remove(hero_adell)
                    enemy_pringer.check = 0


                elif enemy_pringer.die(hero_adell, frame_time) == True:
                    score += 700
                    star_bar.StarBar += 7
                    result_score += 700
                    enemy_group4.remove(enemy_pringer)
                    hero_adell.check = 0

        for hero_archer in hero_group2:
            if collide(hero_archer, enemy_pringer) == True:
                gamesound.punch2()
                enemy_pringer.check += 1
                hero_archer.check += 1

                if hero_archer.die(enemy_pringer, frame_time) == True:
                    hero_group2.remove(hero_archer)
                    enemy_pringer.check = 0

                elif enemy_pringer.die(hero_archer, frame_time) == True:
                    score += 700
                    star_bar.StarBar += 7
                    result_score += 700
                    enemy_group4.remove(enemy_pringer)
                    hero_archer.check = 0

        for hero_asuka in hero_group3:
            if collide(hero_asuka, enemy_pringer) == True:
                gamesound.punch2()
                enemy_pringer.check += 1
                hero_asuka.check += 1

                if hero_asuka.die(enemy_pringer, frame_time) == True:
                    hero_group3.remove(hero_asuka)
                    enemy_pringer.check = 0

                elif enemy_pringer.die(hero_asuka, frame_time) == True:
                    score += 700
                    star_bar.StarBar += 7
                    result_score += 700
                    enemy_group4.remove(enemy_pringer)
                    hero_asuka.check = 0

        for hero_axel in hero_group4:
            if collide(hero_axel, enemy_pringer) == True:
                gamesound.punch2()
                enemy_pringer.check += 1
                hero_axel.check += 1

                if hero_axel.die(enemy_pringer, frame_time) == True:
                    hero_group4.remove(hero_axel)
                    enemy_pringer.check = 0

                elif enemy_pringer.die(hero_axel, frame_time) == True:
                    score += 700
                    star_bar.StarBar += 7
                    result_score += 700
                    enemy_group4.remove(enemy_pringer)
                    hero_axel.check = 0

        for hero_gunner in hero_group5:
            if collide(hero_gunner, enemy_pringer) == True:
                gamesound.punch2()
                enemy_pringer.check += 1
                hero_gunner.check += 1

                if hero_gunner.die(enemy_pringer, frame_time) == True:
                    hero_group5.remove(hero_gunner)
                    enemy_pringer.check = 0

                elif enemy_pringer.die(hero_gunner, frame_time) == True:
                    score += 700
                    star_bar.StarBar += 7
                    result_score += 700
                    enemy_group4.remove(enemy_pringer)
                    hero_gunner.check = 0

        for hero_fenrich in hero_group6:
            if collide(hero_fenrich, enemy_pringer) == True:
                gamesound.punch2()
                enemy_pringer.check += 1
                hero_fenrich.check += 1

                if hero_fenrich.die(enemy_pringer, frame_time) == True:
                    hero_group6.remove(hero_fenrich)
                    enemy_pringer.check = 0

                elif enemy_pringer.die(hero_fenrich, frame_time) == True:
                    score += 700
                    star_bar.StarBar += 7
                    result_score += 700
                    enemy_group4.remove(enemy_pringer)
                    hero_fenrich.check = 0

        for hero_ninja in hero_group7:
            if collide(hero_ninja, enemy_pringer) == True:
                gamesound.punch2()
                enemy_pringer.check += 1
                hero_ninja.check += 1

                if hero_ninja.die(enemy_pringer, frame_time) == True:
                    hero_group7.remove(hero_ninja)
                    enemy_pringer.check = 0

                elif enemy_pringer.die(hero_ninja, frame_time) == True:
                    score += 700
                    star_bar.StarBar += 7
                    result_score += 700
                    enemy_group4.remove(enemy_pringer)
                    hero_ninja.check = 0

        for hero_pram in hero_group8:
            if collide(hero_pram, enemy_pringer) == True:
                gamesound.punch2()
                enemy_pringer.check += 1
                hero_pram.check += 1

                if hero_pram.die(enemy_pringer, frame_time) == True:
                    hero_group8.remove(hero_pram)
                    enemy_pringer.check = 0

                elif enemy_pringer.die(hero_pram, frame_time) == True:
                    score += 700
                    star_bar.StarBar += 7
                    result_score += 700
                    enemy_group4.remove(enemy_pringer)
                    hero_pram.check = 0

        for hero_prof in hero_group9:
            if collide(hero_prof, enemy_pringer) == True:
                gamesound.punch2()
                enemy_pringer.check += 1
                hero_prof.check += 1

                if hero_prof.die(enemy_pringer, frame_time) == True:
                    hero_group9.remove(hero_prof)
                    enemy_pringer.check = 0

                elif enemy_pringer.die(hero_prof, frame_time) == True:
                    score += 700
                    star_bar.StarBar += 7
                    result_score += 700
                    enemy_group4.remove(enemy_pringer)
                    hero_prof.check = 0

    for enemy_demon in enemy_group5:
        for hero_adell in hero_group1:
            if collide(hero_adell, enemy_demon) == True:
                gamesound.punch2()
                enemy_demon.check += 1
                hero_adell.check += 1

                if hero_adell.die(enemy_demon, frame_time) == True:
                    hero_group1.remove(hero_adell)
                    enemy_demon.check = 0

                elif enemy_demon.die(hero_adell, frame_time) == True:
                    score += 1000
                    star_bar.StarBar += 10
                    result_score += 1000
                    enemy_group5.remove(enemy_demon)
                    hero_adell.check = 0

        for hero_archer in hero_group2:
            if collide(hero_archer, enemy_demon) == True:
                gamesound.punch2()
                enemy_demon.check += 1
                hero_archer.check += 1

                if hero_archer.die(enemy_demon, frame_time) == True:
                    hero_group2.remove(hero_archer)
                    enemy_demon.check = 0

                elif enemy_demon.die(hero_archer, frame_time) == True:
                    score += 1000
                    star_bar.StarBar += 10
                    result_score += 1000
                    enemy_group5.remove(enemy_demon)
                    hero_archer.check = 0

        for hero_asuka in hero_group3:
            if collide(hero_asuka, enemy_demon) == True:
                gamesound.punch2()
                enemy_demon.check += 1
                hero_asuka.check += 1

                if hero_asuka.die(enemy_demon, frame_time) == True:
                    hero_group3.remove(hero_asuka)
                    enemy_demon.check = 0

                elif enemy_demon.die(hero_asuka, frame_time) == True:
                    score += 1000
                    star_bar.StarBar += 10
                    result_score += 1000
                    enemy_group5.remove(enemy_demon)
                    hero_asuka.check = 0

        for hero_axel in hero_group4:
            if collide(hero_axel, enemy_demon) == True:
                gamesound.punch2()
                enemy_demon.check += 1
                hero_axel.check += 1

                if hero_axel.die(enemy_demon, frame_time) == True:
                    hero_group4.remove(hero_axel)
                    enemy_demon.check = 0

                elif enemy_demon.die(hero_axel, frame_time) == True:
                    score += 1000
                    star_bar.StarBar += 10
                    result_score += 1000
                    enemy_group5.remove(enemy_demon)
                    hero_axel.check = 0

        for hero_gunner in hero_group5:
            if collide(hero_gunner, enemy_demon) == True:
                gamesound.punch2()
                enemy_demon.check += 1
                hero_gunner.check += 1

                if hero_gunner.die(enemy_demon, frame_time) == True:
                    hero_group5.remove(hero_gunner)
                    enemy_demon.check = 0

                elif enemy_demon.die(hero_gunner, frame_time) == True:
                    score += 1000
                    star_bar.StarBar += 10
                    result_score += 1000
                    enemy_group5.remove(enemy_demon)
                    hero_gunner.check = 0

        for hero_fenrich in hero_group6:
            if collide(hero_fenrich, enemy_demon) == True:
                gamesound.punch2()
                enemy_demon.check += 1
                hero_fenrich.check += 1

                if hero_fenrich.die(enemy_demon, frame_time) == True:
                    hero_group6.remove(hero_fenrich)
                    enemy_demon.check = 0

                elif enemy_demon.die(hero_fenrich, frame_time) == True:
                    score += 1000
                    star_bar.StarBar += 10
                    result_score += 1000
                    enemy_group5.remove(enemy_demon)
                    hero_fenrich.check = 0

        for hero_ninja in hero_group7:
            if collide(hero_ninja, enemy_demon) == True:
                gamesound.punch2()
                enemy_demon.check += 1
                hero_ninja.check += 1

                if hero_ninja.die(enemy_demon, frame_time) == True:
                    hero_group7.remove(hero_ninja)
                    enemy_demon.check = 0

                elif enemy_demon.die(hero_ninja, frame_time) == True:
                    score += 1000
                    star_bar.StarBar += 10
                    result_score += 1000
                    enemy_group5.remove(enemy_demon)
                    hero_ninja.check = 0

        for hero_pram in hero_group8:
            if collide(hero_pram, enemy_demon) == True:
                gamesound.punch2()
                enemy_demon.check += 1
                hero_pram.check += 1

                if hero_pram.die(enemy_demon, frame_time) == True:
                    hero_group8.remove(hero_pram)
                    enemy_demon.check = 0

                elif enemy_demon.die(hero_pram, frame_time) == True:
                    score += 1000
                    star_bar.StarBar += 10
                    result_score += 1000
                    enemy_group5.remove(enemy_demon)
                    hero_pram.check = 0

        for hero_prof in hero_group9:
            if collide(hero_prof, enemy_demon) == True:
                gamesound.punch2()
                enemy_demon.check += 1
                hero_prof.check += 1

                if hero_prof.die(enemy_demon, frame_time) == True:
                    hero_group9.remove(hero_prof)
                    enemy_demon.check = 0

                elif enemy_demon.die(hero_prof, frame_time) == True:
                    score += 1000
                    star_bar.StarBar += 10
                    result_score += 1000
                    enemy_group5.remove(enemy_demon)
                    hero_prof.check = 0

    for enemy_succubus in enemy_group6:
        for hero_adell in hero_group1:
            if collide(hero_adell, enemy_succubus) == True:
                gamesound.punch2()
                enemy_succubus.check += 1
                hero_adell.check += 1

                if hero_adell.die(enemy_succubus, frame_time) == True:
                    hero_group1.remove(hero_adell)
                    enemy_succubus.check = 0

                elif enemy_succubus.die(hero_adell, frame_time) == True:
                    score += 2000
                    star_bar.StarBar += 20
                    result_score += 2000
                    enemy_group6.remove(enemy_succubus)
                    hero_adell.check = 0

        for hero_archer in hero_group2:
            if collide(hero_archer, enemy_succubus) == True:
                gamesound.punch2()
                enemy_succubus.check += 1
                hero_archer.check += 1

                if hero_archer.die(enemy_succubus, frame_time) == True:
                    hero_group2.remove(hero_archer)
                    enemy_succubus.check = 0

                elif enemy_succubus.die(hero_archer, frame_time) == True:
                    score += 2000
                    star_bar.StarBar += 20
                    result_score += 2000
                    enemy_group6.remove(enemy_succubus)
                    hero_archer.check = 0

        for hero_asuka in hero_group3:
            if collide(hero_asuka, enemy_succubus) == True:
                gamesound.punch2()
                enemy_succubus.check += 1
                hero_asuka.check += 1

                if hero_asuka.die(enemy_succubus, frame_time) == True:
                    hero_group3.remove(hero_asuka)
                    enemy_succubus.check = 0

                elif enemy_succubus.die(hero_asuka, frame_time) == True:
                    score += 2000
                    star_bar.StarBar += 20
                    result_score += 2000
                    enemy_group6.remove(enemy_succubus)
                    hero_asuka.check = 0

        for hero_axel in hero_group4:
            if collide(hero_axel, enemy_succubus) == True:
                gamesound.punch2()
                enemy_succubus.check += 1
                hero_axel.check += 1

                if hero_axel.die(enemy_succubus, frame_time) == True:
                    hero_group4.remove(hero_axel)
                    enemy_succubus.check = 0

                elif enemy_succubus.die(hero_axel, frame_time) == True:
                    score += 2000
                    star_bar.StarBar += 20
                    result_score += 2000
                    enemy_group6.remove(enemy_succubus)
                    hero_axel.check = 0

        for hero_gunner in hero_group5:
            if collide(hero_gunner, enemy_succubus) == True:
                gamesound.punch2()
                enemy_succubus.check += 1
                hero_gunner.check += 1

                if hero_gunner.die(enemy_succubus, frame_time) == True:
                    hero_group5.remove(hero_gunner)
                    enemy_succubus.check = 0

                elif enemy_succubus.die(hero_gunner, frame_time) == True:
                    score += 2000
                    star_bar.StarBar += 20
                    result_score += 2000
                    enemy_group6.remove(enemy_succubus)
                    hero_gunner.check = 0

        for hero_fenrich in hero_group6:
            if collide(hero_fenrich, enemy_succubus) == True:
                gamesound.punch2()
                enemy_succubus.check += 1
                hero_fenrich.check += 1

                if hero_fenrich.die(enemy_succubus, frame_time) == True:
                    hero_group6.remove(hero_fenrich)
                    enemy_succubus.check = 0

                elif enemy_succubus.die(hero_fenrich, frame_time) == True:
                    score += 2000
                    star_bar.StarBar += 20
                    result_score += 2000
                    enemy_group6.remove(enemy_succubus)
                    hero_fenrich.check = 0

        for hero_ninja in hero_group7:
            if collide(hero_ninja, enemy_succubus) == True:
                gamesound.punch2()
                enemy_succubus.check += 1
                hero_ninja.check += 1

                if hero_ninja.die(enemy_succubus, frame_time) == True:
                    hero_group7.remove(hero_ninja)
                    enemy_succubus.check = 0

                elif enemy_succubus.die(hero_ninja, frame_time) == True:
                    score += 2000
                    star_bar.StarBar += 20
                    result_score += 2000
                    enemy_group6.remove(enemy_succubus)
                    hero_ninja.check = 0

        for hero_pram in hero_group8:
            if collide(hero_pram, enemy_succubus) == True:
                gamesound.punch2()
                enemy_succubus.check += 1
                hero_pram.check += 1

                if hero_pram.die(enemy_succubus, frame_time) == True:
                    hero_group8.remove(hero_pram)
                    enemy_succubus.check = 0

                elif enemy_succubus.die(hero_pram, frame_time) == True:
                    score += 2000
                    star_bar.StarBar += 20
                    result_score += 2000
                    enemy_group6.remove(enemy_succubus)
                    hero_pram.check = 0

        for hero_prof in hero_group9:
            if collide(hero_prof, enemy_succubus) == True:
                gamesound.punch2()
                enemy_succubus.check += 1
                hero_prof.check += 1

                if hero_prof.die(enemy_succubus, frame_time) == True:
                    hero_group9.remove(hero_prof)
                    enemy_succubus.check = 0

                elif enemy_succubus.die(hero_prof, frame_time) == True:
                    score += 2000
                    star_bar.StarBar += 20
                    result_score += 2000
                    enemy_group6.remove(enemy_succubus)
                    hero_prof.check = 0

def button_click():
    global hero_adell, hero_archer, hero_asuka, hero_axel, hero_fenrich, hero_gunner, hero_ninja, hero_pram, hero_prof, magic_meteor, magic_tornado, magic_explosion
    global m_exp, m_exp_1, score, gold
    global meteor_limit, tornado_limit, explosion_limit, gold_manager
    if gold > 100:
        if 49 < button_x < 170 and 80 < button_y < 210:
            hero_adell = Object_Hero.Hero_Adell(x = 100)
            gold = gold - 100
            gamesound.hero1()
            if len(hero_group1) < 5:
                hero_adell.draw()
                hero_group1.append(hero_adell)
    if gold > 300:
        if 179 < button_x < 310 and 85 < button_y < 210:
            hero_archer = Object_Hero.Hero_Archer(x = 100)
            gold = gold - 300
            gamesound.hero2()
            if len(hero_group2) < 5:
                hero_group2.append(hero_archer)
    if gold > 500:
        if 309 < button_x < 440 and 85 < button_y < 210:
            hero_asuka = Object_Hero.Hero_Asuka(x = 100)
            gold = gold - 500
            gamesound.hero3()
            if len(hero_group3) < 5:
                hero_group3.append(hero_asuka)
    if gold > 1000:
        if 439 < button_x < 560 and 85 < button_y < 210:
            hero_axel = Object_Hero.Hero_Axel(x = 100)
            gold = gold - 1000
            gamesound.hero4()
            if len(hero_group4) < 5:
                hero_group4.append(hero_axel)
    if gold > 1500:
        if 569 < button_x < 690 and 85 < button_y < 210:
            gold = gold - 1500
            hero_gunner = Object_Hero.Hero_Gunner(x = 100)
            gamesound.hero5()
            if len(hero_group5) < 5:
                hero_group5.append(hero_gunner)
    if Menu_Scene.hero6_buy == True:
        if gold > 2000:
            if 699 < button_x < 820 and 85 < button_y < 210:
                gold = gold - 2000
                hero_fenrich = Object_Hero.Hero_Fenrich(x = 100)
                gamesound.hero6()
                if len(hero_group6) < 5:
                    hero_group6.append(hero_fenrich)
    if Menu_Scene.hero7_buy == True:
        if gold > 3000:
            if 829 < button_x < 950 and 85 < button_y < 210:
                gold = gold - 3000
                hero_ninja = Object_Hero.Hero_Ninja(x = 100)
                gamesound.hero7()
                if len(hero_group7) < 4:
                    hero_group7.append(hero_ninja)
    if Menu_Scene.hero8_buy == True:
        if gold > 5000:
            if 959 < button_x < 1080 and 85 < button_y < 210:
                gold = gold - 5000
                hero_pram = Object_Hero.Hero_Pram(x = 100)
                gamesound.hero8()
                if len(hero_group8) < 3:
                    hero_group8.append(hero_pram)
    if Menu_Scene.hero9_buy == True:
        if gold > 7000:
            if 1089 < button_x < 1209 and 85 < button_y < 210:
                gold = gold - 7000
                hero_prof = Object_Hero.Hero_Prof(x = 100)
                gamesound.hero9()
                if len(hero_group9) < 2:
                    hero_group9.append(hero_prof)
    if star_bar.StarBar >= 25:
         if 1071 < button_x < 1150 and 5 < button_y < 78:
             gamesound.goldup()
             star_bar.StarBar -= 25
             gold_manager += 0.1
    if meteor_limit > 0:
        if 100 < button_x < 700 and 300 < button_y < 768:
            magic_meteor = Object_Magic.Magic_Meteor(y = 800)
            gamesound.meteor()
            meteor_limit -= 1
            if len(magic_group1) < 6 + meteor_numb:
                 magic_meteor.x = button_x
                 magic_group1.append(magic_meteor)
                 if magic_meteor.y < 350:
                     magic_group1.remove(magic_meteor)
    if tornado_limit > 0:
        if 831 < button_x < 910 and 5 < button_y < 78:
            magic_tornado = Object_Magic.Magic_Tornado()
            gamesound.tornado()
            tornado_limit -= 1
            if len(magic_group2) < 4 + tornado_numb:
                magic_tornado.x = 100
                magic_group2.append(magic_tornado)
                if magic_tornado.x > 1400:
                    magic_group2.remove(magic_tornado)
    if explosion_limit > 0:
        if 961 < button_x < 1040 and 5 < button_y < 78:
            explosion_limit -= 1
            gamesound.bomb()
            if len(magic_group3) < 2 + explosion_numb:
                magic_group3.append(magic_explosion)
                m_exp = True
                m_exp_1 = True

def Level_Design(frame_time):
    global load_time, summon_random
    load_time += frame_time
    if load_time > 0.5:
        summon_random = random.randint(0, 100)
        load_time = 0
    #print(summon_random)
    if Menu_Scene.level_easy == True:
        if 0 < summon_random < 50 and len(enemy_group1) < 5:
            enemy_slime = Object_Enemy.Enemy_Slime(x = 1200)
            enemy_group1.append(enemy_slime)

    if Menu_Scene.level_normal == True:
        if 0 < summon_random < 20 and len(enemy_group1) < 10:
            enemy_slime = Object_Enemy.Enemy_Slime(x = 1200)
            enemy_group1.append(enemy_slime)

        if 20 < summon_random < 35 and len(enemy_group2) < 5:
            enemy_zombie = Object_Enemy.Enemy_Zombie(x = 1250)
            enemy_group2.append(enemy_zombie)

        if 35 < summon_random < 45 and len(enemy_group3) < 3:
            enemy_golem = Object_Enemy.Enemy_Golem(x = 1250)
            enemy_group3.append(enemy_golem)

    if Menu_Scene.level_hard == True:
        if 0 < summon_random < 20 and len(enemy_group1) < 15:
            enemy_slime = Object_Enemy.Enemy_Slime(x = 1200)
            enemy_group1.append(enemy_slime)

        if 20 < summon_random < 35 and len(enemy_group2) < 10:
            enemy_zombie = Object_Enemy.Enemy_Zombie(x = 1250)
            enemy_group2.append(enemy_zombie)

        if 35 < summon_random < 45 and len(enemy_group3) < 8:
            enemy_golem = Object_Enemy.Enemy_Golem(x = 1250)
            enemy_group3.append(enemy_golem)

        if 45 < summon_random < 54 and len(enemy_group4) < 6:
            enemy_pringer = Object_Enemy.Enemy_Pringer(x = 1250)
            enemy_group4.append(enemy_pringer)

        if 54 < summon_random < 63 and len(enemy_group5) < 4:
            enemy_demon = Object_Enemy.Enemy_Demon(x = 1250)
            enemy_group5.append(enemy_demon)

        if 63 < summon_random < 80 and len(enemy_group6) < 2:
            enemy_succubus = Object_Enemy.Enemy_Succubus(x = 1250)
            enemy_group6.append(enemy_succubus)

def Gameobj_state(frame_time):
    for hero_adell in hero_group1:
        if hero_adell.check > 0:
            hero_adell.state = hero_adell.ATTACK
        elif hero_adell.check <= 0:
            hero_adell.state = hero_adell.WALK


    for hero_archer in hero_group2:
        if hero_archer.check > 0:
            hero_archer.state = hero_archer.ATTACK
        elif hero_archer.check <= 0:
            hero_archer.state = hero_archer.WALK

    for hero_asuka in hero_group3:
        if hero_asuka.check > 0:
            hero_asuka.state = hero_asuka.ATTACK
        elif hero_asuka.check <= 0:
            hero_asuka.state = hero_asuka.WALK

    for hero_axel in hero_group4:
        if hero_axel.check > 0:
            hero_axel.state = hero_axel.ATTACK
        elif hero_axel.check <= 0:
            hero_axel.state = hero_axel.WALK

    for hero_gunner in hero_group5:
        if hero_gunner.check > 0:
            hero_gunner.state = hero_gunner.ATTACK
        elif hero_gunner.check <= 0:
            hero_gunner.state = hero_gunner.WALK

    for hero_fenrich in hero_group6:
        if hero_fenrich.check > 0:
            hero_fenrich.state = hero_fenrich.ATTACK
        elif hero_fenrich.check <= 0:
            hero_fenrich.state = hero_fenrich.WALK

    for hero_ninja in hero_group7:
        if hero_ninja.check > 0:
            hero_ninja.state = hero_ninja.ATTACK
        elif hero_ninja.check <= 0:
            hero_ninja.state = hero_ninja.WALK

    for hero_pram in hero_group8:
        if hero_pram.check > 0:
            hero_pram.state = hero_pram.ATTACK
        elif hero_pram.check <= 0:
            hero_pram.state = hero_pram.WALK

    for hero_prof in hero_group9:
        if hero_prof.check > 0:
            hero_prof.state = hero_prof.ATTACK
        elif hero_prof.check <= 0:
            hero_prof.state = hero_prof.WALK

    for enemy_slime in enemy_group1:
        if enemy_slime.check > 0:
            enemy_slime.state = enemy_slime.ATTACK
        elif enemy_slime.check <= 0:
            enemy_slime.state = enemy_slime.WALK

    for enemy_zombie in enemy_group2:
        if enemy_zombie.check > 0:
            enemy_zombie.state = enemy_zombie.ATTACK
        elif enemy_zombie.check <= 0:
            enemy_zombie.state = enemy_zombie.WALK

    for enemy_golem in enemy_group3:
        if enemy_golem.check > 0:
            enemy_golem.state = enemy_golem.ATTACK
        elif enemy_golem.check <= 0:
            enemy_golem.state = enemy_golem.WALK

    for enemy_pringer in enemy_group4:
        if enemy_pringer.check > 0:
            enemy_pringer.state = enemy_pringer.ATTACK
        elif enemy_pringer.check <= 0:
            enemy_pringer.state = enemy_pringer.WALK

    for enemy_demon in enemy_group5:
        if enemy_demon.check > 0:
            enemy_demon.state = enemy_demon.ATTACK
        elif enemy_demon.check <= 0:
            enemy_demon.state = enemy_demon.WALK

    for enemy_succubus in enemy_group6:
        if enemy_succubus.check > 0:
            enemy_succubus.state = enemy_succubus.ATTACK
        elif enemy_succubus.check <= 0:
            enemy_succubus.state = enemy_succubus.WALK

def handle_events(frame_time):
    global button_x, button_y, user_valva, coll_chk, coll_chk_pic, m_exp, m_exp_1
    events = get_events()
    coll_chk_pic = True
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
            if 10 < button_x < 100 and 10 < button_y < 100:
                user_valva.state = user_valva.MTK
                timer = False
            if 150 < button_x < 250 and 150 < button_y < 250:
                timer = False
            if 1190 < button_x < 1245 and 639 < button_y < 694:
                Menu_Scene.setting_draw = False
                Menu_Scene.level_easy = False
                Menu_Scene.level_normal = False
                Menu_Scene.level_hard = False
                game_framework.change_state(Menu_Scene)
            if 728 < button_x < 775 and 199 < button_y < 245:
                game_framework.change_state(Menu_Scene)
            if 579 < button_x < 623 and 199 < button_y < 245:
                game_framework.change_state(Menu_Scene)
            if 728 < button_x < 775 and 199 < button_y < 245:
                game_framework.change_state(Menu_Scene)

            if coll_chk_pic == True:
                if 1075 < button_x < 1130 and 639 < button_y < 694:
                    coll_chk = True
                    coll_chk_pic = False

            #if coll_chk_pic == False:
                #if 1075 < button_x < 1130 and 639 < button_y < 694:
                    #coll_chk = False
                    #coll_chk_pic = True

def update(frame_time):
    global chk_time, load_time, timer, m_load_time, cool_time_1, cool_time_2, cool_time_3
    global meteor_limit, tornado_limit, explosion_limit, gold, play_time
    if user_castle.defeat == False and enemy_castle.defeat == False:
        load_time += frame_time
        m_load_time += frame_time
        cool_time_1 += frame_time
        cool_time_2 += frame_time
        cool_time_3 += frame_time
        play_time += frame_time
        user_castle.update(frame_time)
        enemy_castle.update(frame_time)

        if m_load_time > 0.5:
            m_load_time = 0

        if load_time > 0.5:
            Level_Design(frame_time)
            load_time = 0

        if cool_time_1 > 3.0:
            cool_time_1 = 0.0
            if meteor_limit < meteor_numb:
                meteor_limit += 1

        if cool_time_2 > 8.0:
            cool_time_2 = 0.0
            if tornado_limit < tornado_numb:
                tornado_limit += 1

        if cool_time_3 > 15.0:
            cool_time_3 = 0.0
            if explosion_limit < explosion_numb:
                explosion_limit += 1

        star_bar.update()
        user_valva.update(frame_time)
        Gameobj_state(frame_time)
        collide_enter(frame_time)
        gold += (frame_time * 100 ) * gold_manager
        if timer == False:
            chk_time += frame_time
        if chk_time > 1.0:
            timer = True
            chk_time = 0.0
            user_valva.state = user_valva.IDLE

def draw(frame_time):
    global gold, score, coll_chk, magic_meteor, magic_tornado, magic_explosion, m_load_time, random_stage
    global meteor_limit, tornado_limit, explosion_limit, gold_manager, meteor_numb, tornado_numb, explosion_numb
    global button_x, button_y, hero_adell, hero_archer, hero_asuka, hero_axel, hero_fenrich, hero_gunner, hero_ninja, hero_pram, hero_prof
    global m_exp, m_exp_1, m_exp_2, m_exp_3, m_exp_4, m_exp_5, m_exp_6, m_exp_7, m_exp_8, m_exp_9, m_exp_10, m_exp_11, m_exp_12, m_exp_13, m_exp_14, m_exp_15, m_exp_16, m_exp_17, m_exp_18, m_exp_19
    clear_canvas()


    if 1 <= random_stage < 11:
        stage_background.draw()
    elif 11 <= random_stage < 21:
        stage2_background.draw()
    elif 21 <= random_stage < 31:
        stage3_background.draw()
    elif 31 <= random_stage < 41:
        stage4_background.draw()
    elif 41 <= random_stage < 51:
        stage5_background.draw()

    if Menu_Scene.level_easy == True:
        gameUI_easy.draw(640, 70)

    if Menu_Scene.level_normal == True:
        gameUI_normal.draw(640, 70)

    if Menu_Scene.level_hard == True:
        gameUI_hard.draw(640, 70)

    if 49 < button_x < 170 and 80 < button_y < 210:
        ui_adell_pic_over.draw(640, 70)
    else:
        ui_adell_pic.draw(640, 70)

    if 179 < button_x < 310 and 85 < button_y < 210:
        ui_archer_pic_over.draw(640, 70)
    else:
        ui_archer_pic.draw(640, 70)

    if 309 < button_x < 440 and 85 < button_y < 210:
        ui_asuka_pic_over.draw(640, 70)
    else:
        ui_asuka_pic.draw(640, 70)

    if 439 < button_x < 560 and 85 < button_y < 210:
        ui_axel_pic_over.draw(640, 70)
    else:
        ui_axel_pic.draw(640, 70)

    if 569 < button_x < 690 and 85 < button_y < 210:
        ui_gunner_pic_over.draw(640, 70)
    else:
        ui_gunner_pic.draw(640, 70)


    if Upgrade_Manager.HeroBuyManager.sell_6 > 1:
        if 699 < button_x < 820 and 85 < button_y < 210:
            ui_fenrich_pic_over.draw(640, 70)
        else:
            ui_fenrich_pic.draw(640, 70)

    if Upgrade_Manager.HeroBuyManager.sell_7 > 1:
        if 829 < button_x < 950 and 85 < button_y < 210:
            ui_ninja_pic_over.draw(640, 70)
        else:
            ui_ninja_pic.draw(640, 70)


    if Upgrade_Manager.HeroBuyManager.sell_8 > 1:
        if 959 < button_x < 1080 and 85 < button_y < 210:
            ui_pram_pic_over.draw(640, 70)
        else:
            ui_pram_pic.draw(640, 70)

    if Upgrade_Manager.HeroBuyManager.sell_9 > 1:
        if 1089 < button_x < 1209 and 85 < button_y < 210:
            ui_prof_pic_over.draw(640, 70)
        else:
            ui_prof_pic.draw(640, 70)

    if 699 < button_x < 775 and 5 < button_y < 78:
        ui_meteor_pic_over.draw(640, 70)
    else:
        ui_meteor_pic.draw(640, 70)

    if 831 < button_x < 910 and 5 < button_y < 78:
        ui_tornado_pic_over.draw(640, 70)
    else:
        ui_tornado_pic.draw(640, 70)

    if 961 < button_x < 1040 and 5 < button_y < 78:
        ui_explosion_pic_over.draw(640, 70)
    else:
        ui_explosion_pic.draw(640, 70)

    if 1071 < button_x < 1150 and 5 < button_y < 78:
        ui_goldup_over.draw(640, 70)
    else:
        ui_goldup.draw(640, 70)

    cloud.draw(90, 500)
    if 1075 < button_x < 1130 and 639 < button_y < 694:
        ui_collchk_over.draw(640, 360)
    else:
        ui_collchk.draw(640, 360)

    if 1190 < button_x < 1245 and 639 < button_y < 694:
        ui_gotown2_over.draw(640, 360)
    else:
        ui_gotown2.draw(640, 360)

    user_castle.draw()
    enemy_castle.draw()
    if user_castle.defeat == False and enemy_castle.defeat == False:
        if coll_chk == True:
            user_castle.draw_bb()
            enemy_castle.draw_bb()

        for enemy_slime in enemy_group1:
            enemy_slime.update(frame_time)
            enemy_slime.draw()
            if coll_chk == True:
                enemy_slime.draw_bb()

        for enemy_zombie in enemy_group2:
            enemy_zombie.update(frame_time)
            enemy_zombie.draw()
            if coll_chk == True:
                enemy_zombie.draw_bb()

        for enemy_golem in enemy_group3:
            enemy_golem.update(frame_time)
            enemy_golem.draw()
            if coll_chk == True:
                enemy_golem.draw_bb()

        for enemy_pringer in enemy_group4:
            enemy_pringer.update(frame_time)
            enemy_pringer.draw()
            if coll_chk == True:
                enemy_pringer.draw_bb()

        for enemy_demon in enemy_group5:
            enemy_demon.update(frame_time)
            enemy_demon.draw()
            if coll_chk == True:
                enemy_demon.draw_bb()

        for enemy_succubus in enemy_group6:
            enemy_succubus.update(frame_time)
            enemy_succubus.draw()
            if coll_chk == True:
                enemy_succubus.draw_bb()
        for hero_adell in hero_group1:
            hero_adell.update(frame_time)
            hero_adell.draw()
            if coll_chk == True:
                hero_adell.draw_bb()

        for hero_archer in hero_group2:
            hero_archer.update(frame_time)
            hero_archer.draw()
            if coll_chk == True:
                hero_archer.draw_bb()

        for hero_asuka in hero_group3:
            hero_asuka.update(frame_time)
            hero_asuka.draw()
            if coll_chk == True:
                hero_asuka.draw_bb()

        for hero_axel in hero_group4:
            hero_axel.update(frame_time)
            hero_axel.draw()
            if coll_chk == True:
                hero_axel.draw_bb()

        for hero_fenrich in hero_group5:
            hero_fenrich.update(frame_time)
            hero_fenrich.draw()
            if coll_chk == True:
                hero_fenrich.draw_bb()

        for hero_gunner in hero_group6:
            hero_gunner.update(frame_time)
            hero_gunner.draw()
            if coll_chk == True:
                hero_gunner.draw_bb()

        for hero_ninja in hero_group7:
            hero_ninja.update(frame_time)
            hero_ninja.draw()
            if coll_chk == True:
                hero_ninja.draw_bb()

        for hero_pram in hero_group8:
            hero_pram.update(frame_time)
            hero_pram.draw()
            if coll_chk == True:
                hero_pram.draw_bb()

        for hero_prof in hero_group9:
            hero_prof.update(frame_time)
            hero_prof.draw()
            if coll_chk == True:
                hero_prof.draw_bb()

    font.draw(500, 55, '%1.f' % gold)
    font.draw(767, 12, '%d' % meteor_limit)
    font.draw(900, 12, '%d' % tornado_limit)
    font.draw(1030, 12, '%d' % explosion_limit)

    # hero_1
    if Upgrade_Manager.UpgradeManager.hero_1_star_level == 1:
        upgrade_manager.draw(640, 75)
        hero_adell.atk = 15
        hero_adell.hp = 150
    if Upgrade_Manager.UpgradeManager.hero_1_star_level == 2:
        upgrade_manager.draw(640, 75)
        upgrade_manager.draw(655, 75)
        hero_adell.atk = 20
        hero_adell.hp = 200
    if Upgrade_Manager.UpgradeManager.hero_1_star_level == 3:
        upgrade_manager.draw(640, 75)
        upgrade_manager.draw(655, 75)
        upgrade_manager.draw(670, 75)
        hero_adell.atk = 25
        hero_adell.hp = 250
    if Upgrade_Manager.UpgradeManager.hero_1_star_level == 4:
        upgrade_manager.draw(640, 75)
        upgrade_manager.draw(655, 75)
        upgrade_manager.draw(670, 75)
        upgrade_manager.draw(685, 75)
        hero_adell.atk = 30
        hero_adell.hp = 300
    if Upgrade_Manager.UpgradeManager.hero_1_star_level == 5:
        upgrade_manager.draw(640, 75)
        upgrade_manager.draw(655, 75)
        upgrade_manager.draw(670, 75)
        upgrade_manager.draw(685, 75)
        upgrade_manager.draw(700, 75)
        hero_adell.atk = 35
        hero_adell.hp = 350
    if Upgrade_Manager.UpgradeManager.hero_1_star_level == 6:
        upgrade_manager.draw(640, 75)
        upgrade_manager.draw(655, 75)
        upgrade_manager.draw(670, 75)
        upgrade_manager.draw(685, 75)
        upgrade_manager.draw(700, 75)
        upgrade_manager.draw(715, 75)
        hero_adell.atk = 40
        hero_adell.hp = 400
    if Upgrade_Manager.UpgradeManager.hero_1_star_level == 7:
        upgrade_manager.draw(640, 75)
        upgrade_manager.draw(655, 75)
        upgrade_manager.draw(670, 75)
        upgrade_manager.draw(685, 75)
        upgrade_manager.draw(700, 75)
        upgrade_manager.draw(715, 75)
        upgrade_manager.draw(730, 75)
        hero_adell.atk = 50
        hero_adell.hp = 500

    # hero_2
    if Upgrade_Manager.UpgradeManager.hero_2_star_level == 1:
        upgrade_manager.draw(770, 75)
        hero_archer.atk = 20
        hero_archer.hp = 300
    if Upgrade_Manager.UpgradeManager.hero_2_star_level == 2:
        upgrade_manager.draw(770, 75)
        upgrade_manager.draw(785, 75)
        hero_archer.atk = 25
        hero_archer.hp = 350
    if Upgrade_Manager.UpgradeManager.hero_2_star_level == 3:
        upgrade_manager.draw(770, 75)
        upgrade_manager.draw(785, 75)
        upgrade_manager.draw(800, 75)
        hero_archer.atk = 30
        hero_archer.hp = 400
    if Upgrade_Manager.UpgradeManager.hero_2_star_level == 4:
        upgrade_manager.draw(770, 75)
        upgrade_manager.draw(785, 75)
        upgrade_manager.draw(800, 75)
        upgrade_manager.draw(815, 75)
        hero_archer.atk = 35
        hero_archer.hp = 450
    if Upgrade_Manager.UpgradeManager.hero_2_star_level == 5:
        upgrade_manager.draw(770, 75)
        upgrade_manager.draw(785, 75)
        upgrade_manager.draw(800, 75)
        upgrade_manager.draw(815, 75)
        upgrade_manager.draw(830, 75)
        hero_archer.atk = 40
        hero_archer.hp = 500
    if Upgrade_Manager.UpgradeManager.hero_2_star_level == 6:
        upgrade_manager.draw(770, 75)
        upgrade_manager.draw(785, 75)
        upgrade_manager.draw(800, 75)
        upgrade_manager.draw(815, 75)
        upgrade_manager.draw(830, 75)
        upgrade_manager.draw(845, 75)
        hero_archer.atk = 50
        hero_archer.hp = 600
    if Upgrade_Manager.UpgradeManager.hero_2_star_level == 7:
        upgrade_manager.draw(770, 75)
        upgrade_manager.draw(785, 75)
        upgrade_manager.draw(800, 75)
        upgrade_manager.draw(815, 75)
        upgrade_manager.draw(830, 75)
        upgrade_manager.draw(845, 75)
        upgrade_manager.draw(860, 75)
        hero_archer.atk = 70
        hero_archer.hp = 700

    # hero_3
    if Upgrade_Manager.UpgradeManager.hero_3_star_level == 1:
        upgrade_manager.draw(900, 75)
        hero_asuka.atk = 40
        hero_asuka.hp = 550
    if Upgrade_Manager.UpgradeManager.hero_3_star_level == 2:
        upgrade_manager.draw(900, 75)
        upgrade_manager.draw(915, 75)
        hero_asuka.atk = 45
        hero_asuka.hp = 600
    if Upgrade_Manager.UpgradeManager.hero_3_star_level == 3:
        upgrade_manager.draw(900, 75)
        upgrade_manager.draw(915, 75)
        upgrade_manager.draw(930, 75)
        hero_asuka.atk = 50
        hero_asuka.hp = 650
    if Upgrade_Manager.UpgradeManager.hero_3_star_level == 4:
        upgrade_manager.draw(900, 75)
        upgrade_manager.draw(915, 75)
        upgrade_manager.draw(930, 75)
        upgrade_manager.draw(945, 75)
        hero_asuka.atk = 55
        hero_asuka.hp = 700
    if Upgrade_Manager.UpgradeManager.hero_3_star_level == 5:
        upgrade_manager.draw(900, 75)
        upgrade_manager.draw(915, 75)
        upgrade_manager.draw(930, 75)
        upgrade_manager.draw(945, 75)
        upgrade_manager.draw(960, 75)
        hero_asuka.atk = 60
        hero_asuka.hp = 750
    if Upgrade_Manager.UpgradeManager.hero_3_star_level == 6:
        upgrade_manager.draw(900, 75)
        upgrade_manager.draw(915, 75)
        upgrade_manager.draw(930, 75)
        upgrade_manager.draw(945, 75)
        upgrade_manager.draw(960, 75)
        upgrade_manager.draw(975, 75)
        hero_asuka.atk = 65
        hero_asuka.hp = 800
    if Upgrade_Manager.UpgradeManager.hero_3_star_level == 7:
        upgrade_manager.draw(900, 75)
        upgrade_manager.draw(915, 75)
        upgrade_manager.draw(930, 75)
        upgrade_manager.draw(945, 75)
        upgrade_manager.draw(960, 75)
        upgrade_manager.draw(975, 75)
        upgrade_manager.draw(990, 75)
        hero_asuka.atk = 80
        hero_asuka.hp = 1000

    # hero_4
    if Upgrade_Manager.UpgradeManager.hero_4_star_level == 1:
        upgrade_manager.draw(1030, 75)
        hero_axel.atk = 15
        hero_axel.hp = 1200
    if Upgrade_Manager.UpgradeManager.hero_4_star_level == 2:
        upgrade_manager.draw(1030, 75)
        upgrade_manager.draw(1045, 75)
        hero_axel.atk = 20
        hero_axel.hp = 1400
    if Upgrade_Manager.UpgradeManager.hero_4_star_level == 3:
        upgrade_manager.draw(1030, 75)
        upgrade_manager.draw(1045, 75)
        upgrade_manager.draw(1060, 75)
        hero_axel.atk = 25
        hero_axel.hp = 1600
    if Upgrade_Manager.UpgradeManager.hero_4_star_level == 4:
        upgrade_manager.draw(1030, 75)
        upgrade_manager.draw(1045, 75)
        upgrade_manager.draw(1060, 75)
        upgrade_manager.draw(1075, 75)
        hero_axel.atk = 30
        hero_axel.hp = 1800
    if Upgrade_Manager.UpgradeManager.hero_4_star_level == 5:
        upgrade_manager.draw(1030, 75)
        upgrade_manager.draw(1045, 75)
        upgrade_manager.draw(1060, 75)
        upgrade_manager.draw(1075, 75)
        upgrade_manager.draw(1090, 75)
        hero_axel.atk = 35
        hero_axel.hp = 2000
    if Upgrade_Manager.UpgradeManager.hero_4_star_level == 6:
        upgrade_manager.draw(1030, 75)
        upgrade_manager.draw(1045, 75)
        upgrade_manager.draw(1060, 75)
        upgrade_manager.draw(1075, 75)
        upgrade_manager.draw(1090, 75)
        upgrade_manager.draw(1105, 75)
        hero_axel.atk = 40
        hero_axel.hp = 2200
    if Upgrade_Manager.UpgradeManager.hero_4_star_level == 7:
        upgrade_manager.draw(1030, 75)
        upgrade_manager.draw(1045, 75)
        upgrade_manager.draw(1060, 75)
        upgrade_manager.draw(1075, 75)
        upgrade_manager.draw(1090, 75)
        upgrade_manager.draw(1105, 75)
        upgrade_manager.draw(1120, 75)
        hero_axel.atk = 50
        hero_axel.hp = 2500

    # hero_5
    if Upgrade_Manager.UpgradeManager.hero_5_star_level == 1:
        upgrade_manager.draw(1160, 75)
        hero_fenrich.atk = 80
        hero_fenrich.hp = 550
    if Upgrade_Manager.UpgradeManager.hero_5_star_level == 2:
        upgrade_manager.draw(1160, 75)
        upgrade_manager.draw(1175, 75)
        hero_fenrich.atk = 90
        hero_fenrich.hp = 600
    if Upgrade_Manager.UpgradeManager.hero_5_star_level == 3:
        upgrade_manager.draw(1160, 75)
        upgrade_manager.draw(1175, 75)
        upgrade_manager.draw(1190, 75)
        hero_fenrich.atk = 100
        hero_fenrich.hp = 650
    if Upgrade_Manager.UpgradeManager.hero_5_star_level == 4:
        upgrade_manager.draw(1160, 75)
        upgrade_manager.draw(1175, 75)
        upgrade_manager.draw(1190, 75)
        upgrade_manager.draw(1205, 75)
        hero_fenrich.atk = 110
        hero_fenrich.hp = 700
    if Upgrade_Manager.UpgradeManager.hero_5_star_level == 5:
        upgrade_manager.draw(1160, 75)
        upgrade_manager.draw(1175, 75)
        upgrade_manager.draw(1190, 75)
        upgrade_manager.draw(1205, 75)
        upgrade_manager.draw(1220, 75)
        hero_fenrich.atk = 120
        hero_fenrich.hp = 800
    if Upgrade_Manager.UpgradeManager.hero_5_star_level == 6:
        upgrade_manager.draw(1160, 75)
        upgrade_manager.draw(1175, 75)
        upgrade_manager.draw(1190, 75)
        upgrade_manager.draw(1205, 75)
        upgrade_manager.draw(1220, 75)
        upgrade_manager.draw(1235, 75)
        hero_axel.atk = 130
        hero_axel.hp = 900
    if Upgrade_Manager.UpgradeManager.hero_5_star_level == 7:
        upgrade_manager.draw(1160, 75)
        upgrade_manager.draw(1175, 75)
        upgrade_manager.draw(1190, 75)
        upgrade_manager.draw(1205, 75)
        upgrade_manager.draw(1220, 75)
        upgrade_manager.draw(1235, 75)
        upgrade_manager.draw(1250, 75)
        hero_fenrich.atk = 150
        hero_fenrich.hp = 1000

    # hero_6
    if Upgrade_Manager.UpgradeManager.hero_6_star_level == 1:
        upgrade_manager.draw(1290, 75)
        hero_gunner.atk = 15
        hero_gunner.hp = 2200
    if Upgrade_Manager.UpgradeManager.hero_6_star_level == 2:
        upgrade_manager.draw(1290, 75)
        upgrade_manager.draw(1305, 75)
        hero_gunner.atk = 20
        hero_gunner.hp = 2400
    if Upgrade_Manager.UpgradeManager.hero_6_star_level == 3:
        upgrade_manager.draw(1290, 75)
        upgrade_manager.draw(1305, 75)
        upgrade_manager.draw(1320, 75)
        hero_gunner.atk = 25
        hero_gunner.hp = 2600
    if Upgrade_Manager.UpgradeManager.hero_6_star_level == 4:
        upgrade_manager.draw(1290, 75)
        upgrade_manager.draw(1305, 75)
        upgrade_manager.draw(1320, 75)
        upgrade_manager.draw(1335, 75)
        hero_gunner.atk = 30
        hero_gunner.hp = 2800
    if Upgrade_Manager.UpgradeManager.hero_6_star_level == 5:
        upgrade_manager.draw(1290, 75)
        upgrade_manager.draw(1305, 75)
        upgrade_manager.draw(1320, 75)
        upgrade_manager.draw(1335, 75)
        upgrade_manager.draw(1350, 75)
        hero_gunner.atk = 35
        hero_gunner.hp = 3000
    if Upgrade_Manager.UpgradeManager.hero_6_star_level == 6:
        upgrade_manager.draw(1290, 75)
        upgrade_manager.draw(1305, 75)
        upgrade_manager.draw(1320, 75)
        upgrade_manager.draw(1335, 75)
        upgrade_manager.draw(1350, 75)
        upgrade_manager.draw(1365, 75)
        hero_gunner.atk = 40
        hero_gunner.hp = 3200
    if Upgrade_Manager.UpgradeManager.hero_6_star_level == 7:
        upgrade_manager.draw(1290, 75)
        upgrade_manager.draw(1305, 75)
        upgrade_manager.draw(1320, 75)
        upgrade_manager.draw(1335, 75)
        upgrade_manager.draw(1350, 75)
        upgrade_manager.draw(1365, 75)
        upgrade_manager.draw(1380, 75)
        hero_gunner.atk = 50
        hero_gunner.hp = 3500

    # hero_7
    if Upgrade_Manager.UpgradeManager.hero_7_star_level == 1:
        upgrade_manager.draw(1420, 75)
        hero_ninja.atk = 90
        hero_ninja.hp = 1000
    if Upgrade_Manager.UpgradeManager.hero_7_star_level == 2:
        upgrade_manager.draw(1420, 75)
        upgrade_manager.draw(1435, 75)
        hero_ninja.atk = 100
        hero_ninja.hp = 1050
    if Upgrade_Manager.UpgradeManager.hero_7_star_level == 3:
        upgrade_manager.draw(1420, 75)
        upgrade_manager.draw(1435, 75)
        upgrade_manager.draw(1450, 75)
        hero_ninja.atk = 110
        hero_ninja.hp = 1150
    if Upgrade_Manager.UpgradeManager.hero_7_star_level == 4:
        upgrade_manager.draw(1420, 75)
        upgrade_manager.draw(1435, 75)
        upgrade_manager.draw(1450, 75)
        upgrade_manager.draw(1465, 75)
        hero_ninja.atk = 120
        hero_ninja.hp = 1200
    if Upgrade_Manager.UpgradeManager.hero_7_star_level == 5:
        upgrade_manager.draw(1420, 75)
        upgrade_manager.draw(1435, 75)
        upgrade_manager.draw(1450, 75)
        upgrade_manager.draw(1465, 75)
        upgrade_manager.draw(1480, 75)
        hero_ninja.atk = 130
        hero_ninja.hp = 1250
    if Upgrade_Manager.UpgradeManager.hero_7_star_level == 6:
        upgrade_manager.draw(1420, 75)
        upgrade_manager.draw(1435, 75)
        upgrade_manager.draw(1450, 75)
        upgrade_manager.draw(1465, 75)
        upgrade_manager.draw(1480, 75)
        upgrade_manager.draw(1495, 75)
        hero_ninja.atk = 140
        hero_ninja.hp = 1300
    if Upgrade_Manager.UpgradeManager.hero_7_star_level == 7:
        upgrade_manager.draw(1420, 75)
        upgrade_manager.draw(1435, 75)
        upgrade_manager.draw(1450, 75)
        upgrade_manager.draw(1465, 75)
        upgrade_manager.draw(1480, 75)
        upgrade_manager.draw(1495, 75)
        upgrade_manager.draw(1510, 75)
        hero_ninja.atk = 150
        hero_ninja.hp = 1500

    # hero_8
    if Upgrade_Manager.UpgradeManager.hero_8_star_level == 1:
        upgrade_manager.draw(1550, 75)
        hero_pram.atk = 120
        hero_pram.hp = 1600
    if Upgrade_Manager.UpgradeManager.hero_8_star_level == 2:
        upgrade_manager.draw(1550, 75)
        upgrade_manager.draw(1565, 75)
        hero_pram.atk = 140
        hero_pram.hp = 1700
    if Upgrade_Manager.UpgradeManager.hero_8_star_level == 3:
        upgrade_manager.draw(1550, 75)
        upgrade_manager.draw(1565, 75)
        upgrade_manager.draw(1580, 75)
        hero_pram.atk = 160
        hero_pram.hp = 1800
    if Upgrade_Manager.UpgradeManager.hero_8_star_level == 4:
        upgrade_manager.draw(1550, 75)
        upgrade_manager.draw(1565, 75)
        upgrade_manager.draw(1580, 75)
        upgrade_manager.draw(1595, 75)
        hero_pram.atk = 180
        hero_pram.hp = 1900
    if Upgrade_Manager.UpgradeManager.hero_8_star_level == 5:
        upgrade_manager.draw(1550, 75)
        upgrade_manager.draw(1565, 75)
        upgrade_manager.draw(1580, 75)
        upgrade_manager.draw(1595, 75)
        upgrade_manager.draw(1610, 75)
        hero_pram.atk = 200
        hero_pram.hp = 2000
    if Upgrade_Manager.UpgradeManager.hero_8_star_level == 6:
        upgrade_manager.draw(1550, 75)
        upgrade_manager.draw(1565, 75)
        upgrade_manager.draw(1580, 75)
        upgrade_manager.draw(1595, 75)
        upgrade_manager.draw(1610, 75)
        upgrade_manager.draw(1625, 75)
        hero_pram.atk = 220
        hero_pram.hp = 2200
    if Upgrade_Manager.UpgradeManager.hero_8_star_level == 7:
        upgrade_manager.draw(1550, 75)
        upgrade_manager.draw(1565, 75)
        upgrade_manager.draw(1580, 75)
        upgrade_manager.draw(1595, 75)
        upgrade_manager.draw(1610, 75)
        upgrade_manager.draw(1625, 75)
        upgrade_manager.draw(1640, 75)
        hero_pram.atk = 250
        hero_pram.hp = 2500

    # hero_9
    if Upgrade_Manager.UpgradeManager.hero_9_star_level == 1:
        upgrade_manager.draw(1680, 75)
        hero_pram.atk = 160
        hero_pram.hp = 2200
    if Upgrade_Manager.UpgradeManager.hero_9_star_level == 2:
        upgrade_manager.draw(1680, 75)
        upgrade_manager.draw(1695, 75)
        hero_pram.atk = 170
        hero_pram.hp = 2400
    if Upgrade_Manager.UpgradeManager.hero_9_star_level == 3:
        upgrade_manager.draw(1680, 75)
        upgrade_manager.draw(1695, 75)
        upgrade_manager.draw(1710, 75)
        hero_pram.atk = 180
        hero_pram.hp = 2600
    if Upgrade_Manager.UpgradeManager.hero_9_star_level == 4:
        upgrade_manager.draw(1680, 75)
        upgrade_manager.draw(1695, 75)
        upgrade_manager.draw(1710, 75)
        upgrade_manager.draw(1725, 75)
        hero_pram.atk = 190
        hero_pram.hp = 2800
    if Upgrade_Manager.UpgradeManager.hero_9_star_level == 5:
        upgrade_manager.draw(1680, 75)
        upgrade_manager.draw(1695, 75)
        upgrade_manager.draw(1710, 75)
        upgrade_manager.draw(1725, 75)
        upgrade_manager.draw(1740, 75)
        hero_pram.atk = 200
        hero_pram.hp = 3000
    if Upgrade_Manager.UpgradeManager.hero_9_star_level == 6:
        upgrade_manager.draw(1680, 75)
        upgrade_manager.draw(1695, 75)
        upgrade_manager.draw(1710, 75)
        upgrade_manager.draw(1725, 75)
        upgrade_manager.draw(1740, 75)
        upgrade_manager.draw(1755, 75)
        hero_pram.atk = 210
        hero_pram.hp = 3200
    if Upgrade_Manager.UpgradeManager.hero_9_star_level == 7:
        upgrade_manager.draw(1680, 75)
        upgrade_manager.draw(1695, 75)
        upgrade_manager.draw(1710, 75)
        upgrade_manager.draw(1725, 75)
        upgrade_manager.draw(1740, 75)
        upgrade_manager.draw(1755, 75)
        upgrade_manager.draw(1770, 75)
        hero_pram.atk = 2200
        hero_pram.hp = 3500

    # magic_1
    if Upgrade_Manager.UpgradeManager.magic_1_star_level == 1:
        upgrade_manager.draw(1290, -55)
        meteor_numb = 7
    if Upgrade_Manager.UpgradeManager.magic_1_star_level == 2:
        upgrade_manager.draw(1290, -55)
        upgrade_manager.draw(1315, -55)
        meteor_numb = 8
    if Upgrade_Manager.UpgradeManager.magic_1_star_level == 3:
        upgrade_manager.draw(1290, -55)
        upgrade_manager.draw(1315, -55)
        upgrade_manager.draw(1340, -55)
        meteor_numb = 9

    # magic_2
    if Upgrade_Manager.UpgradeManager.magic_2_star_level == 1:
        upgrade_manager.draw(1420, -55)
        tornado_numb = 5
    if Upgrade_Manager.UpgradeManager.magic_2_star_level == 2:
        upgrade_manager.draw(1420, -55)
        upgrade_manager.draw(1445, -55)
        tornado_numb = 6
    if Upgrade_Manager.UpgradeManager.magic_2_star_level == 3:
        upgrade_manager.draw(1420, -55)
        upgrade_manager.draw(1445, -55)
        upgrade_manager.draw(1470, -55)
        tornado_numb = 7

    # magic_3
    if Upgrade_Manager.UpgradeManager.magic_3_star_level == 1:
        upgrade_manager.draw(1550, -55)
        explosion_numb = 3
    if Upgrade_Manager.UpgradeManager.magic_3_star_level == 2:
        upgrade_manager.draw(1550, -55)
        upgrade_manager.draw(1575, -55)
        explosion_numb = 4
    if Upgrade_Manager.UpgradeManager.magic_3_star_level == 3:
        upgrade_manager.draw(1550, -55)
        upgrade_manager.draw(1575, -55)
        upgrade_manager.draw(1600, -55)
        explosion_numb = 5

    user_valva.draw()
    for magic_meteor in magic_group1:
        magic_meteor.update(frame_time)
        magic_meteor.draw()
        if coll_chk == True:
            magic_meteor.draw_bb()

    for magic_tornado in magic_group2:
        magic_tornado.update(frame_time)
        magic_tornado.draw()
        if coll_chk == True:
            magic_tornado.draw_bb()

    for magic_explosion in magic_group3:
        magic_explosion.update()
        magic_explosion.draw()
        if coll_chk == True:
            magic_explosion.draw_bb()

    star_bar.draw()

    if coll_chk == True:
        user_valva.draw_bb()
    if m_exp == True:
        if m_exp_1 == True:
            magic_exp_image_1.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_2 = True
                m_load_time = 0
                m_exp_1 = False
        elif m_exp_2 == True:
            magic_exp_image_2.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_3 = True
                m_load_time = 0
                m_exp_2 = False
        elif m_exp_3 == True:
            magic_exp_image_3.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_4 = True
                m_load_time = 0
                m_exp_3 = False
        elif m_exp_4 == True:
            magic_exp_image_4.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_5 = True
                m_load_time = 0
                m_exp_4 = False
        elif m_exp_5 == True:
            magic_exp_image_5.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_6 = True
                m_load_time = 0
                m_exp_5 = False
        elif m_exp_6 == True:
            magic_exp_image_6.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_7 = True
                m_load_time = 0
                m_exp_6 = False
        elif m_exp_7 == True:
            magic_exp_image_7.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_8 = True
                m_load_time = 0
                m_exp_7 = False
        elif m_exp_8 == True:
            magic_exp_image_8.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_9 = True
                m_load_time = 0
                m_exp_8 = False
        elif m_exp_9 == True:
            magic_exp_image_9.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_10 = True
                m_load_time = 0
                m_exp_9 = False
        elif m_exp_10 == True:
            magic_exp_image_10.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_11 = True
                m_load_time = 0
                m_exp_10 = False
        elif m_exp_11 == True:
            magic_exp_image_11.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_12 = True
                m_load_time = 0
                m_exp_11 = False
        elif m_exp_12 == True:
            magic_exp_image_12.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_13 = True
                m_load_time = 0
                m_exp_12 = False
        elif m_exp_13 == True:
            magic_exp_image_13.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_14 = True
                m_load_time = 0
                m_exp_13 = False
        elif m_exp_14 == True:
            magic_exp_image_14.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_15 = True
                m_load_time = 0
                m_exp_14 = False
        elif m_exp_15 == True:
            magic_exp_image_15.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_16 = True
                m_load_time = 0
                m_exp_15 = False
        elif m_exp_16 == True:
            magic_exp_image_16.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_17 = True
                m_load_time = 0
                m_exp_16 = False
        elif m_exp_17 == True:
            magic_exp_image_17.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_18 = True
                m_load_time = 0
                m_exp_17 = False
        elif m_exp_18 == True:
            magic_exp_image_18.draw(640, 360)
            if m_load_time > 0.1:
                m_exp_19 = True
                m_load_time = 0
                m_exp_18 = False
        elif m_exp_19 == True:
            magic_exp_image_19.draw(640, 360)
            if m_load_time > 0.1:
                m_load_time = 0
                magic_group3.remove(magic_explosion)
                m_exp_19 = False
                m_exp_1 = False

    if user_castle.defeat == True:
        gamesound.defeat()
        ui_defeat.draw(640,360)
        if 579 < button_x < 623 and 199 < button_y < 245:
            ui_restart_over.draw(640,360)
        else:
            ui_restart.draw(640,360)
        if 728 < button_x < 775 and 199 < button_y < 245:
            ui_gotown_over.draw(640,360)
        else:
            ui_gotown.draw(640,360)

    if enemy_castle.defeat == True:
        gamesound.victory()
        ui_victory.draw(640,360)
        if 728 < button_x < 775 and 199 < button_y < 245:
            ui_gotown_over.draw(640,360)
        else:
            ui_gotown.draw(640,360)

    ui_timer.draw(635, 690)
    time_font.draw(635, 687, '%0.1f' % play_time)
    if user_castle.defeat == True or enemy_castle.defeat == True:
        result_font.draw(730, 475, '%1.f' % ((result_score * play_time) / 50))
        result_font.draw(730, 387, '%1.f' % play_time)
        result_font.draw(730, 302, '%1.f' % (Menu_Scene.diamond + (play_time * 10.0)))

    update_canvas()





