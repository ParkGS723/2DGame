import game_framework
from pico2d import *

import Upgrade_Manager
import Main_Scene

level_hard = None
level_normal = None
level_easy = None
setting_draw = None
mx, my = 0, 0
name = "MenuScene"
Title_bkg = None
herobar = None
buy_ask = None
hero_up_ask = None
magic_up_ask = None

hero1_sell = None
hero2_sell = None
hero3_sell = None
hero4_sell = None
hero5_sell = None
hero6_sell = None
hero7_sell = None
hero8_sell = None
hero9_sell = None

hero1_buy = None
hero2_buy = None
hero3_buy = None
hero4_buy = None
hero5_buy = None
hero6_buy = None
hero7_buy = None
hero8_buy = None
hero9_buy = None

magic_upgrade = None
hero_upgrade = None
up_ask = None
up_ask2 = None
hero_star_1 = None
hero_star_2 = None
hero_star_3 = None
hero_star_4 = None
hero_star_5 = None
hero_star_6 = None
hero_star_7 = None
hero_star_8 = None
hero_star_9 = None
magic_star_1 = None
magic_star_2 = None
magic_star_3 = None
hero1_up = 0
hero2_up = 0
hero3_up = 0
hero4_up = 0
hero5_up = 0
hero6_up = 0
hero7_up = 0
hero8_up = 0
hero9_up = 0
magic1_up = 0
magic2_up = 0
magic3_up = 0

class MenuBackGround:
    def __init__(self):
        self.x, self.y = 640, 360
        self.image = load_image('UI/MainMenu.png')

    def draw(self):
        self.image.draw(self.x, self.y)


class MenuSound:
    button_sound = None

    def __init__(self):
        if MenuSound.button_sound == None:
            MenuSound.button_sound = load_wav('Sound/test.wav')
            MenuSound.button_sound.set_volume(32)

    def click(self):
        self.button_sound.play()



def enter():
    global MainMenu_bg, Menu_1, Menu_1_over, Menu_2, Menu_2_over, Menu_3, Menu_3_over, Search, Search_over, level_setting, clicksound
    global Menu_buy_yes, Menu_buy_yes_over, Menu_buy_no, Menu_buy_no_over, store_exit, store_exit_over, hero_buy_ask
    global store_main, store_upgrade_1, store_upgrade_2, store_hero1, store_hero1_over, store_hero1_sell, store_hero2, store_hero2_over, store_hero2_sell, store_hero3, store_hero3_over, store_hero3_sell
    global store_hero4, store_hero4_over, store_hero4_sell, store_hero5, store_hero5_over, store_hero5_sell, store_hero6, store_hero6_over, store_hero6_sell, store_hero7, store_hero7_over, store_hero7_sell
    global store_hero8, store_hero8_over, store_hero8_sell, store_hero9, store_hero9_over, store_hero9_sell, store_user_magic_1, store_user_magic_1_over, store_user_magic_2, store_user_magic_2_over, store_user_magic_3, store_user_magic_3_over
    global hero_up_ask, magic_up_ask, upgradestar, star_group, diamond, font, bgm

    upgradestar = Upgrade_Manager.UpgradeStar()
    diamond = 999999
    font = load_font('ENCR10B.TTF')
    star_group = []
    bgm = load_music('Sound/menu_bgm.mp3')
    bgm.set_volume(64)
    bgm.repeat_play()

    MainMenu_bg = MenuBackGround()
    clicksound = MenuSound()
    Menu_1 = load_image('UI/Menu_1.png')
    Menu_1_over = load_image('UI/Menu_1(over).png')
    Menu_2 = load_image('UI/Menu_2.png')
    Menu_2_over = load_image('UI/Menu_2(over).png')
    Menu_3 = load_image('UI/Menu_3.png')
    Menu_3_over = load_image('UI/Menu_3(over).png')
    Search = load_image('UI/Search.png')
    Search_over = load_image('UI/Search(over).png')

    Menu_buy_yes = load_image('UI/Buy_yes.png')
    Menu_buy_yes_over = load_image('UI/Buy_yes(over).png')
    Menu_buy_no = load_image('UI/Buy_no.png')
    Menu_buy_no_over = load_image('UI/Buy_no(over).png')
    store_exit = load_image('UI/store_exit.png')
    store_exit_over = load_image('UI/store_exit(over).png')
    hero_buy_ask = load_image('UI/hero_buy.png')
    hero_up_ask = load_image('UI/hero_upgrade.png')
    magic_up_ask = load_image('UI/magic_upgrade.png')
    store_main = load_image('UI/store_main.png')
    store_upgrade_1 = load_image('UI/store_upgrade1.png')
    store_upgrade_2 = load_image('UI/store_upgrade2.png')
    store_hero1 = load_image('UI/store_hero1.png')
    store_hero1_over = load_image('UI/store_hero1_over.png')
    store_hero1_sell = load_image('UI/store_hero1_sell.png')
    store_hero2 = load_image('UI/store_hero2.png')
    store_hero2_over = load_image('UI/store_hero2_over.png')
    store_hero2_sell = load_image('UI/store_hero2_sell.png')
    store_hero3 = load_image('UI/store_hero3.png')
    store_hero3_over = load_image('UI/store_hero3_over.png')
    store_hero3_sell = load_image('UI/store_hero3_sell.png')
    store_hero4 = load_image('UI/store_hero4.png')
    store_hero4_over = load_image('UI/store_hero4_over.png')
    store_hero4_sell = load_image('UI/store_hero4_sell.png')
    store_hero5 = load_image('UI/store_hero5.png')
    store_hero5_over = load_image('UI/store_hero5_over.png')
    store_hero5_sell = load_image('UI/store_hero5_sell.png')
    store_hero6 = load_image('UI/store_hero6.png')
    store_hero6_over = load_image('UI/store_hero6_over.png')
    store_hero6_sell = load_image('UI/store_hero6_sell.png')
    store_hero7 = load_image('UI/store_hero7.png')
    store_hero7_over = load_image('UI/store_hero7_over.png')
    store_hero7_sell = load_image('UI/store_hero7_sell.png')
    store_hero8 = load_image('UI/store_hero8.png')
    store_hero8_over = load_image('UI/store_hero8_over.png')
    store_hero8_sell = load_image('UI/store_hero8_sell.png')
    store_hero9 = load_image('UI/store_hero9.png')
    store_hero9_over = load_image('UI/store_hero9_over.png')
    store_hero9_sell = load_image('UI/store_hero9_sell.png')
    store_user_magic_1 = load_image('UI/store_user_magic_1.png')
    store_user_magic_1_over = load_image('UI/store_user_magic_1_over.png')
    store_user_magic_2 = load_image('UI/store_user_magic_2.png')
    store_user_magic_2_over = load_image('UI/store_user_magic_2_over.png')
    store_user_magic_3 = load_image('UI/store_user_magic_3.png')
    store_user_magic_3_over = load_image('UI/store_user_magic_3_over.png')
    level_setting = load_image('UI/level_settings.png')


def exit():
    pass

def pause():
    pass

def resume():
    pass

def handle_events(frame_time):
    events = get_events()
    global mx, my, level_easy, level_normal, level_hard, setting_draw, clicksound, herobar, buy_ask, up_ask, up_ask2
    global hero1_sell, hero2_sell, hero3_sell, hero4_sell, hero5_sell, hero6_sell, hero7_sell, hero8_sell, hero9_sell
    global buy_yes, buy_no, hero_upgrade, magic_upgrade, diamond, magic_star_1, magic_star_2, magic_star_3, magic1_up, magic2_up, magic3_up
    global hero1_buy, hero2_buy, hero3_buy, hero4_buy, hero5_buy, hero6_buy, hero7_buy, hero8_buy, hero9_buy
    global hero1_up, hero2_up, hero3_up, hero4_up, hero5_up, hero6_up, hero7_up, hero8_up, hero9_up, sell_six
    global hero_star_1, hero_star_2, hero_star_3, hero_star_4,hero_star_5, hero_star_6, hero_star_7, hero_star_8, hero_star_9
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
                if 135 < mx < 566 and 575 < my < 670: #전투영웅
                    clicksound.click()
                    hero_upgrade = True
                if 749 < mx < 1173 and 580 < my < 655: #유저영웅
                    clicksound.click()
                    magic_upgrade = True
                if 990 < mx < 1260 and 312 < my < 392: #선술집
                    clicksound.click()
                    herobar = True

                if magic_upgrade == True:
                    if 855 < mx < 905 and 529 < my < 570:
                        up_ask2 = False
                        magic_upgrade = False

                    if 440 < mx < 525 and 293 < my < 368:
                        up_ask2 = True
                        magic_star_1 = True
                    if magic_star_1 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask2 = False
                            diamond -= 100
                            magic1_up += 1
                            Upgrade_Manager.UpgradeStar.magic_1_star_level += 1
                            if Upgrade_Manager.UpgradeStar.magic_1_star_level > 3:
                                Upgrade_Manager.UpgradeStar.magic_1_star_level = 3
                            if magic1_up > 3:
                                magic1_up = 3
                            magic_star_1 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask2 = False
                            magic_star_1 = False
                    if 590 < mx < 680 and 293 < my < 368:
                        up_ask2 = True
                        magic_star_2 = True
                    if magic_star_2 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask2 = False
                            magic2_up += 1
                            diamond -= 500
                            Upgrade_Manager.UpgradeManager.magic_2_star_level += 1
                            if Upgrade_Manager.UpgradeManager.hero_star_level > 3:
                                Upgrade_Manager.UpgradeManager.magic_2_star_level = 3
                            if magic2_up > 3:
                                magic2_up = 3
                            magic_star_2 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask2 = False
                            magic_star_2 = False
                    if 745 < mx < 830 and 293 < my < 368:
                        up_ask2 = True
                        magic_star_3 = True
                    if magic_star_3 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask2 = False
                            magic3_up += 1
                            diamond -= 1000
                            Upgrade_Manager.UpgradeManager.magic_3_star_level += 1
                            if Upgrade_Manager.UpgradeManager.magic_3_star_level > 3:
                                Upgrade_Manager.UpgradeManager.magic_3_star_level = 3
                            if magic3_up > 3:
                                magic3_up = 3
                            magic_star_3 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask2 = False
                            magic_star_3 = False

                if hero_upgrade == True:
                    if 855 < mx < 905 and 529 < my < 570:
                        up_ask = False
                        hero_upgrade = False
                    if 372 < mx < 457 and 388 < my < 478:
                        up_ask = True
                        hero_star_1 = True
                    if hero_star_1 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask = False
                            hero1_up += 1
                            diamond -= 100
                            Upgrade_Manager.UpgradeManager.hero_1_star_level += 1
                            if Upgrade_Manager.UpgradeManager.hero_1_star_level > 7:
                                Upgrade_Manager.UpgradeManager.hero_1_star_level = 7
                            if hero1_up > 7:
                                hero1_up = 7
                            hero_star_1 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask = False
                            hero_star_1 = False

                    if 477 < mx < 561 and 388 < my < 478:
                        up_ask = True
                        hero_star_2 = True
                    if hero_star_2 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask = False
                            hero2_up += 1
                            diamond -= 300
                            Upgrade_Manager.UpgradeManager.hero_2_star_level += 1
                            if Upgrade_Manager.UpgradeManager.hero_2_star_level > 7:
                                Upgrade_Manager.UpgradeManager.hero_2_star_level = 7
                            if hero2_up > 7:
                                hero2_up = 7
                            hero_star_2 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask = False
                            hero_star_2 = False

                    if 583 < mx < 667 and 388 < my < 478:
                        up_ask = True
                        hero_star_3 = True
                    if hero_star_3 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask = False
                            hero3_up += 1
                            diamond -= 500
                            Upgrade_Manager.UpgradeManager.hero_3_star_level += 1
                            if Upgrade_Manager.UpgradeManager.hero_3_star_level > 7:
                                Upgrade_Manager.UpgradeManager.hero_3_star_level = 7
                            if hero3_up > 7:
                                hero3_up = 7
                            hero_star_3 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask = False
                            hero_star_3 = False

                    if 687 < mx < 775 and 388 < my < 478:
                        up_ask = True
                        hero_star_4 = True
                    if hero_star_4 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask = False
                            hero4_up += 1
                            diamond -= 1000
                            Upgrade_Manager.UpgradeManager.hero_4_star_level += 1
                            if Upgrade_Manager.UpgradeManager.hero_4_star_level > 7:
                                Upgrade_Manager.UpgradeManager.hero_4_star_level = 7
                            if hero4_up > 7:
                                hero4_up = 7
                            hero_star_4 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask = False
                            hero_star_4 = False

                    if 796 < mx < 882 and 388 < my < 478:
                        up_ask = True
                        hero_star_5 = True
                    if hero_star_5 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask = False
                            hero5_up += 1
                            diamond -= 1500
                            Upgrade_Manager.UpgradeManager.hero_5_star_level += 1
                            if Upgrade_Manager.UpgradeManager.hero_5_star_level > 7:
                                Upgrade_Manager.UpgradeManager.hero_5_star_level = 7
                            if hero5_up > 7:
                                hero5_up = 7
                            hero_star_5 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask = False
                            hero_star_5 = False

                    if 429 < mx < 515 and 250 < my < 335:
                        up_ask = True
                        hero_star_6 = True
                    if hero_star_6 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask = False
                            hero6_up += 1
                            diamond -= 2000
                            Upgrade_Manager.UpgradeManager.hero_6_star_level += 1
                            if Upgrade_Manager.UpgradeManager.hero_6_star_level > 7:
                                Upgrade_Manager.UpgradeManager.hero_6_star_level = 7
                            if hero6_up > 7:
                                hero6_up = 7
                            hero_star_6 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask = False
                            hero_star_6 = False

                    if 535 < mx < 622 and 250 < my < 335:
                        up_ask = True
                        hero_star_7 = True
                    if hero_star_7 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask = False
                            hero7_up += 1
                            diamond -= 3000
                            Upgrade_Manager.UpgradeManager.hero_7_star_level += 1
                            if Upgrade_Manager.UpgradeManager.hero_7_star_level > 7:
                                Upgrade_Manager.UpgradeManager.hero_7_star_level = 7
                            if hero7_up > 7:
                                hero7_up = 7
                            hero_star_7 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask = False
                            hero_star_7 = False

                    if 642 < mx < 724 and 250 < my < 335:
                        up_ask = True
                        hero_star_8 = True
                    if hero_star_8 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask = False
                            hero8_up += 1
                            diamond -= 5000
                            Upgrade_Manager.UpgradeManager.hero_8_star_level += 1
                            if Upgrade_Manager.UpgradeManager.hero_8_star_level > 7:
                                Upgrade_Manager.UpgradeManager.hero_8_star_level = 7
                            if hero8_up > 7:
                                hero8_up = 7
                            hero_star_8 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask = False
                            hero_star_8 = False

                    if 747 < mx < 835 and 250 < my < 335:
                        up_ask = True
                        hero_star_9 = True
                    if hero_star_9 == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            up_ask = False
                            hero9_up += 1
                            diamond -= 7000
                            Upgrade_Manager.UpgradeManager.hero_9_star_level += 1
                            if Upgrade_Manager.UpgradeManager.hero_9_star_level > 7:
                                Upgrade_Manager.UpgradeManager.hero_9_star_level = 7
                            if hero9_up > 7:
                                hero9_up = 7
                            hero_star_9 = False
                        if 679 < mx < 712 and 360 < my < 400:
                            up_ask = False
                            hero_star_9 = False

                if herobar == True:
                    if 855 < mx < 905 and 529 < my < 570:
                        buy_ask = False
                        herobar = False
                    if 429 < mx < 515 and 280 < my < 365:
                        buy_ask = True
                        hero6_buy = True
                    if hero6_buy == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            buy_ask = False
                            hero6_sell = True
                            diamond -= 2000
                            Upgrade_Manager.HeroBuyManager.sell_6 = 2
                        if 679 < mx < 712 and 360 < my < 400:
                            buy_ask = False

                    if 535 < mx < 622 and 280 < my < 365:
                        buy_ask = True
                        hero7_buy = True
                    if hero7_buy == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            buy_ask = False
                            hero7_sell = True
                            diamond -= 3000
                            Upgrade_Manager.HeroBuyManager.sell_7 = 2
                        if 679 < mx < 712 and 360 < my < 400:
                            buy_ask = False

                    if 642 < mx < 724 and 280 < my < 365:
                        buy_ask = True
                        hero8_buy = True
                    if hero8_buy == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            buy_ask = False
                            hero8_sell = True
                            diamond -= 5000
                            Upgrade_Manager.HeroBuyManager.sell_8 = 2
                        if 679 < mx < 712 and 360 < my < 400:
                            buy_ask = False

                    if 747 < mx < 835 and 280 < my < 365:
                        buy_ask = True
                        hero9_buy = True
                    if hero9_buy == True:
                        if 566 < mx < 601 and 360 < my < 400:
                            buy_ask = False
                            diamond -= 7000
                            hero9_sell = True
                            Upgrade_Manager.HeroBuyManager.sell_9 = 2
                        if 679 < mx < 712 and 360 < my < 400:
                            buy_ask = False

                if 458 < mx < 820 and 40 < my < 193:
                    clicksound.click()
                    setting_draw = True

                if setting_draw == True:
                    if 610 < mx < 680 and 430 < my < 460:
                        level_easy = True
                        clicksound.click()
                        game_framework.change_state(Main_Scene)
                    if 610 < mx < 690 and 390 < my < 420:
                        level_normal = True
                        clicksound.click()
                        game_framework.change_state(Main_Scene)
                    if 610 < mx < 690 and 340 < my < 370:
                        level_hard = True
                        clicksound.click()
                        game_framework.change_state(Main_Scene)

def update(frame_time):
    pass

def draw(frame_time):
    global mx, my
    global MainMenu_bkg, Menu_1, Menu_1_over, Menu_2, Menu_2_over, Menu_3, Menu_3_over,Search, Search_over
    global Menu_buy_yes, Menu_buy_yes_over, Menu_buy_no, Menu_buy_no_over, store_exit, store_exit_over, buy_ask
    global store_main, store_upgrade_1, store_upgrade_2, store_hero1, store_hero1_over, store_hero1_sell, store_hero2, store_hero2_over, store_hero2_sell, store_hero3, store_hero3_over, store_hero3_sell
    global store_hero4, store_hero4_over, store_hero4_sell, store_hero5, store_hero5_over, store_hero5_sell, store_hero6, store_hero6_over, store_hero6_sell, store_hero7, store_hero7_over, store_hero7_sell
    global store_hero8, store_hero8_over, store_hero8_sell, store_hero9, store_hero9_over, store_hero9_sell, store_user_magic_1, store_user_magic_1_over, store_user_magic_2, store_user_magic_2_over, store_user_magic_3, store_user_magic_3_over
    global hero1_sell, hero2_sell, hero3_sell, hero4_sell, hero5_sell, hero6_sell, hero7_sell, hero8_sell, hero9_sell, hero_buy_ask, Menu_buy_yes, Menu_buy_yes_over, Menu_buy_no, Menu_buy_no_over
    global buy_complete, hero_upgrade, diamond

    clear_canvas()
    MainMenu_bg.draw()
    if 135 < mx < 566 and 575 < my < 670:
        Menu_1_over.draw(640, 360)
    else:
        Menu_1.draw(640, 360)

    if 749 < mx < 1173 and 580 < my < 655:
        Menu_2_over.draw(640, 360)
    else:
        Menu_2.draw(640, 360)

    if 990 < mx < 1260 and 312 < my < 392:
        Menu_3_over.draw(640, 360)
    else:
        Menu_3.draw(640, 360)

    if 458 < mx < 820 and 40 < my < 193:
        Search_over.draw(640, 360)
    else:
        Search.draw(640, 360)

    if setting_draw == True:
        level_setting.draw(640, 400)

    if magic_upgrade == True:
        store_upgrade_2.draw(640,360)
        font.draw(440, 530, '%d' % diamond)
        if 855 < mx < 905 and 529 < my < 570:
            store_exit_over.draw(640,360)
        else:
            store_exit.draw(640,360)
        if 440 < mx < 525 and 293 < my < 368:
            store_user_magic_1_over.draw(640, 360)
        else:
            store_user_magic_1.draw(640, 360)
        if 590 < mx < 680 and 293 < my < 368:
            store_user_magic_2_over.draw(640, 360)
        else:
            store_user_magic_2.draw(640, 360)
        if 745 < mx < 830 and 293 < my < 368:
            store_user_magic_3_over.draw(640, 360)
        else:
            store_user_magic_3.draw(640, 360)

        if magic1_up == 1:
            upgradestar.draw(720, 250)
        if magic1_up == 2:
            upgradestar.draw(720, 250)
            upgradestar.draw(740, 250)
        if magic1_up == 3:
            upgradestar.draw(720, 250)
            upgradestar.draw(740, 250)
            upgradestar.draw(760, 250)

        if magic2_up == 1:
            upgradestar.draw(870, 250)
        if magic2_up == 2:
            upgradestar.draw(870, 250)
            upgradestar.draw(890, 250)
        if magic2_up == 3:
            upgradestar.draw(870, 250)
            upgradestar.draw(890, 250)
            upgradestar.draw(910, 250)

        if magic3_up == 1:
            upgradestar.draw(1025, 250)
        if magic3_up == 2:
            upgradestar.draw(1025, 250)
            upgradestar.draw(1045, 250)
        if magic3_up == 3:
            upgradestar.draw(1025, 250)
            upgradestar.draw(1045, 250)
            upgradestar.draw(1065, 250)


    if herobar == True:
        store_main.draw(640,360)
        font.draw(440, 530, '%d' % diamond)
        if 855 < mx < 905 and 529 < my < 570:
            store_exit_over.draw(640,360)
        else:
            store_exit.draw(640,360)

        store_hero1_sell.draw(640, 360)
        store_hero2_sell.draw(640, 360)
        store_hero3_sell.draw(640, 360)
        store_hero4_sell.draw(640, 360)
        store_hero5_sell.draw(640, 360)
        if hero6_sell == True:
            store_hero6_sell.draw(640, 360)
        else:
            if 429 < mx < 515 and 280 < my < 365:
                store_hero6_over.draw(640, 360)
            else:
                store_hero6.draw(640, 360)
        if hero7_sell == True:
            store_hero7_sell.draw(640, 360)
        else:
            if 535 < mx < 622 and 280 < my < 365:
                store_hero7_over.draw(640, 360)
            else:
                store_hero7.draw(640, 360)
        if hero8_sell == True:
            store_hero8_sell.draw(640, 360)
        else:
            if 642 < mx < 724 and 280 < my < 365:
                store_hero8_over.draw(640, 360)
            else:
                store_hero8.draw(640, 360)
        if hero9_sell == True:
            store_hero9_sell.draw(640, 360)
        else:
            if 747 < mx < 835 and 280 < my < 365:
                store_hero9_over.draw(640, 360)
            else:
                store_hero9.draw(640, 360)

    if hero_upgrade == True:
        store_upgrade_1.draw(640, 360)
        font.draw(440, 530, '%d' % diamond)
        if 855 < mx < 905 and 529 < my < 570:
            store_exit_over.draw(640,360)
        else:
            store_exit.draw(640,360)

        if 372 < mx < 457 and 388 < my < 478:
            store_hero1_over.draw(640, 360)
        else:
            store_hero1.draw(640, 360)
        if 477 < mx < 561 and 388 < my < 478:
            store_hero2_over.draw(640, 360)
        else:
            store_hero2.draw(640, 360)
        if 583 < mx < 667 and 388 < my < 478:
            store_hero3_over.draw(640, 360)
        else:
            store_hero3.draw(640, 360)
        if 687 < mx < 775 and 388 < my < 478:
            store_hero4_over.draw(640, 360)
        else:
            store_hero4.draw(640, 360)
        if 796 < mx < 882 and 388 < my < 478:
            store_hero5_over.draw(640, 360)
        else:
            store_hero5.draw(640, 360)
        if 429 < mx < 515 and 250 < my < 335:
            store_hero6_over.draw(640, 330)
        else:
            store_hero6.draw(640, 330)
        if 535 < mx < 622 and 250 < my < 335:
            store_hero7_over.draw(640, 330)
        else:
            store_hero7.draw(640, 330)
        if 642 < mx < 724 and 250 < my < 335:
            store_hero8_over.draw(640, 330)
        else:
            store_hero8.draw(640, 330)
        if 747 < mx < 835 and 250 < my < 335:
            store_hero9_over.draw(640, 330)
        else:
            store_hero9.draw(640, 330)

        if hero1_up == 1:
            upgradestar.draw(640, 360)
        if hero1_up == 2:
            upgradestar.draw(640, 360)
            upgradestar.draw(650, 360)
        if hero1_up == 3:
            upgradestar.draw(640, 360)
            upgradestar.draw(650, 360)
            upgradestar.draw(660, 360)
        if hero1_up == 4:
            upgradestar.draw(640, 360)
            upgradestar.draw(650, 360)
            upgradestar.draw(660, 360)
            upgradestar.draw(670, 360)
        if hero1_up == 5:
            upgradestar.draw(640, 360)
            upgradestar.draw(650, 360)
            upgradestar.draw(660, 360)
            upgradestar.draw(670, 360)
            upgradestar.draw(680, 360)
        if hero1_up == 6:
            upgradestar.draw(640, 360)
            upgradestar.draw(650, 360)
            upgradestar.draw(660, 360)
            upgradestar.draw(670, 360)
            upgradestar.draw(680, 360)
            upgradestar.draw(690, 360)
        if hero1_up == 7:
            upgradestar.draw(640, 360)
            upgradestar.draw(650, 360)
            upgradestar.draw(660, 360)
            upgradestar.draw(670, 360)
            upgradestar.draw(680, 360)
            upgradestar.draw(690, 360)
            upgradestar.draw(700, 360)

        if hero2_up == 1:
            upgradestar.draw(745, 360)
        if hero2_up == 2:
            upgradestar.draw(745, 360)
            upgradestar.draw(755, 360)
        if hero2_up == 3:
            upgradestar.draw(745, 360)
            upgradestar.draw(755, 360)
            upgradestar.draw(765, 360)
        if hero2_up == 4:
            upgradestar.draw(745, 360)
            upgradestar.draw(755, 360)
            upgradestar.draw(765, 360)
            upgradestar.draw(775, 360)
        if hero2_up == 5:
            upgradestar.draw(745, 360)
            upgradestar.draw(755, 360)
            upgradestar.draw(765, 360)
            upgradestar.draw(775, 360)
            upgradestar.draw(785, 360)
        if hero2_up == 6:
            upgradestar.draw(745, 360)
            upgradestar.draw(755, 360)
            upgradestar.draw(765, 360)
            upgradestar.draw(775, 360)
            upgradestar.draw(785, 360)
            upgradestar.draw(795, 360)
        if hero2_up == 7:
            upgradestar.draw(745, 360)
            upgradestar.draw(755, 360)
            upgradestar.draw(765, 360)
            upgradestar.draw(775, 360)
            upgradestar.draw(785, 360)
            upgradestar.draw(795, 360)
            upgradestar.draw(805, 360)

        if hero3_up == 1:
            upgradestar.draw(850, 360)
        if hero3_up == 2:
            upgradestar.draw(850, 360)
            upgradestar.draw(860, 360)
        if hero3_up == 3:
            upgradestar.draw(850, 360)
            upgradestar.draw(860, 360)
            upgradestar.draw(870, 360)
        if hero3_up == 4:
            upgradestar.draw(850, 360)
            upgradestar.draw(860, 360)
            upgradestar.draw(870, 360)
            upgradestar.draw(880, 360)
        if hero3_up == 5:
            upgradestar.draw(850, 360)
            upgradestar.draw(860, 360)
            upgradestar.draw(870, 360)
            upgradestar.draw(880, 360)
            upgradestar.draw(890, 360)
        if hero3_up == 6:
            upgradestar.draw(850, 360)
            upgradestar.draw(860, 360)
            upgradestar.draw(870, 360)
            upgradestar.draw(880, 360)
            upgradestar.draw(890, 360)
            upgradestar.draw(900, 360)
        if hero3_up == 7:
            upgradestar.draw(850, 360)
            upgradestar.draw(860, 360)
            upgradestar.draw(870, 360)
            upgradestar.draw(880, 360)
            upgradestar.draw(890, 360)
            upgradestar.draw(900, 360)
            upgradestar.draw(910, 360)

        if hero4_up == 1:
            upgradestar.draw(955, 360)
        if hero4_up == 2:
            upgradestar.draw(955, 360)
            upgradestar.draw(965, 360)
        if hero4_up == 3:
            upgradestar.draw(955, 360)
            upgradestar.draw(965, 360)
            upgradestar.draw(975, 360)
        if hero4_up == 4:
            upgradestar.draw(955, 360)
            upgradestar.draw(965, 360)
            upgradestar.draw(975, 360)
            upgradestar.draw(985, 360)
        if hero4_up == 5:
            upgradestar.draw(955, 360)
            upgradestar.draw(965, 360)
            upgradestar.draw(975, 360)
            upgradestar.draw(985, 360)
            upgradestar.draw(995, 360)
        if hero4_up == 6:
            upgradestar.draw(955, 360)
            upgradestar.draw(965, 360)
            upgradestar.draw(975, 360)
            upgradestar.draw(985, 360)
            upgradestar.draw(995, 360)
            upgradestar.draw(1005, 360)
        if hero4_up == 7:
            upgradestar.draw(955, 360)
            upgradestar.draw(965, 360)
            upgradestar.draw(975, 360)
            upgradestar.draw(985, 360)
            upgradestar.draw(995, 360)
            upgradestar.draw(1005, 360)
            upgradestar.draw(1015, 360)

        if hero5_up == 1:
            upgradestar.draw(1060, 360)
        if hero5_up == 2:
            upgradestar.draw(1060, 360)
            upgradestar.draw(1070, 360)
        if hero5_up == 3:
            upgradestar.draw(1060, 360)
            upgradestar.draw(1070, 360)
            upgradestar.draw(1080, 360)
        if hero5_up == 4:
            upgradestar.draw(1060, 360)
            upgradestar.draw(1070, 360)
            upgradestar.draw(1080, 360)
            upgradestar.draw(1090, 360)
        if hero5_up == 5:
            upgradestar.draw(1060, 360)
            upgradestar.draw(1070, 360)
            upgradestar.draw(1080, 360)
            upgradestar.draw(1090, 360)
            upgradestar.draw(1100, 360)
        if hero5_up == 6:
            upgradestar.draw(1060, 360)
            upgradestar.draw(1070, 360)
            upgradestar.draw(1080, 360)
            upgradestar.draw(1090, 360)
            upgradestar.draw(1100, 360)
            upgradestar.draw(1110, 360)
        if hero5_up == 7:
            upgradestar.draw(1060, 360)
            upgradestar.draw(1070, 360)
            upgradestar.draw(1080, 360)
            upgradestar.draw(1090, 360)
            upgradestar.draw(1100, 360)
            upgradestar.draw(1110, 360)
            upgradestar.draw(1120, 360)

        if hero6_up == 1:
            upgradestar.draw(700, 220)
        if hero6_up == 2:
            upgradestar.draw(700, 220)
            upgradestar.draw(710, 220)
        if hero6_up == 3:
            upgradestar.draw(700, 220)
            upgradestar.draw(710, 220)
            upgradestar.draw(720, 220)
        if hero6_up == 4:
            upgradestar.draw(700, 220)
            upgradestar.draw(710, 220)
            upgradestar.draw(720, 220)
            upgradestar.draw(730, 220)
        if hero6_up == 5:
            upgradestar.draw(700, 220)
            upgradestar.draw(710, 220)
            upgradestar.draw(720, 220)
            upgradestar.draw(730, 220)
            upgradestar.draw(740, 220)
        if hero6_up == 6:
            upgradestar.draw(700, 220)
            upgradestar.draw(710, 220)
            upgradestar.draw(720, 220)
            upgradestar.draw(730, 220)
            upgradestar.draw(740, 220)
            upgradestar.draw(750, 220)
        if hero6_up == 7:
            upgradestar.draw(700, 220)
            upgradestar.draw(710, 220)
            upgradestar.draw(720, 220)
            upgradestar.draw(730, 220)
            upgradestar.draw(740, 220)
            upgradestar.draw(750, 220)
            upgradestar.draw(760, 220)

        if hero7_up == 1:
            upgradestar.draw(805, 220)
        if hero7_up == 2:
            upgradestar.draw(805, 220)
            upgradestar.draw(815, 220)
        if hero7_up == 3:
            upgradestar.draw(805, 220)
            upgradestar.draw(815, 220)
            upgradestar.draw(825, 220)
        if hero7_up == 4:
            upgradestar.draw(805, 220)
            upgradestar.draw(815, 220)
            upgradestar.draw(825, 220)
            upgradestar.draw(835, 220)
        if hero7_up == 5:
            upgradestar.draw(805, 220)
            upgradestar.draw(815, 220)
            upgradestar.draw(825, 220)
            upgradestar.draw(835, 220)
            upgradestar.draw(845, 220)
        if hero7_up == 6:
            upgradestar.draw(805, 220)
            upgradestar.draw(815, 220)
            upgradestar.draw(825, 220)
            upgradestar.draw(835, 220)
            upgradestar.draw(845, 220)
            upgradestar.draw(855, 220)
        if hero7_up == 7:
            upgradestar.draw(805, 220)
            upgradestar.draw(815, 220)
            upgradestar.draw(825, 220)
            upgradestar.draw(835, 220)
            upgradestar.draw(845, 220)
            upgradestar.draw(855, 220)
            upgradestar.draw(865, 220)

        if hero8_up == 1:
            upgradestar.draw(910, 220)
        if hero8_up == 2:
            upgradestar.draw(910, 220)
            upgradestar.draw(920, 220)
        if hero8_up == 3:
            upgradestar.draw(910, 220)
            upgradestar.draw(920, 220)
            upgradestar.draw(930, 220)
        if hero8_up == 4:
            upgradestar.draw(910, 220)
            upgradestar.draw(920, 220)
            upgradestar.draw(930, 220)
            upgradestar.draw(940, 220)
        if hero8_up == 5:
            upgradestar.draw(910, 220)
            upgradestar.draw(920, 220)
            upgradestar.draw(930, 220)
            upgradestar.draw(940, 220)
            upgradestar.draw(950, 220)
        if hero8_up == 6:
            upgradestar.draw(910, 220)
            upgradestar.draw(920, 220)
            upgradestar.draw(930, 220)
            upgradestar.draw(940, 220)
            upgradestar.draw(950, 220)
            upgradestar.draw(960, 220)
        if hero8_up == 7:
            upgradestar.draw(910, 220)
            upgradestar.draw(920, 220)
            upgradestar.draw(930, 220)
            upgradestar.draw(940, 220)
            upgradestar.draw(950, 220)
            upgradestar.draw(960, 220)
            upgradestar.draw(970, 220)

        if hero9_up == 1:
            upgradestar.draw(1015, 220)
        if hero9_up == 2:
            upgradestar.draw(1015, 220)
            upgradestar.draw(1025, 220)
        if hero9_up == 3:
            upgradestar.draw(1015, 220)
            upgradestar.draw(1025, 220)
            upgradestar.draw(1035, 220)
        if hero9_up == 4:
            upgradestar.draw(1015, 220)
            upgradestar.draw(1025, 220)
            upgradestar.draw(1035, 220)
            upgradestar.draw(1045, 220)
        if hero9_up == 5:
            upgradestar.draw(1015, 220)
            upgradestar.draw(1025, 220)
            upgradestar.draw(1035, 220)
            upgradestar.draw(1045, 220)
            upgradestar.draw(1055, 220)
        if hero9_up == 6:
            upgradestar.draw(1015, 220)
            upgradestar.draw(1025, 220)
            upgradestar.draw(1035, 220)
            upgradestar.draw(1045, 220)
            upgradestar.draw(1055, 220)
            upgradestar.draw(1065, 220)
        if hero9_up == 7:
            upgradestar.draw(1015, 220)
            upgradestar.draw(1025, 220)
            upgradestar.draw(1035, 220)
            upgradestar.draw(1045, 220)
            upgradestar.draw(1055, 220)
            upgradestar.draw(1065, 220)
            upgradestar.draw(1075, 220)

    if buy_ask == True:
        hero_buy_ask.draw(640,460)
        if 566 < mx < 601 and 360 < my < 400:
            Menu_buy_yes_over.draw(640,460)
        else:
            Menu_buy_yes.draw(640,460)
        if 679 < mx < 712 and 360 < my < 400:
            Menu_buy_no_over.draw(640,460)
        else:
            Menu_buy_no.draw(640,460)

    if up_ask2 == True:
        magic_up_ask.draw(640, 460)
        if 566 < mx < 601 and 360 < my < 400:
            Menu_buy_yes_over.draw(640,460)
        else:
            Menu_buy_yes.draw(640,460)
        if 679 < mx < 712 and 360 < my < 400:
            Menu_buy_no_over.draw(640,460)
        else:
            Menu_buy_no.draw(640,460)

    if up_ask == True:
        hero_up_ask.draw(640, 460)
        if 566 < mx < 601 and 360 < my < 400:
            Menu_buy_yes_over.draw(640,460)
        else:
            Menu_buy_yes.draw(640,460)
        if 679 < mx < 712 and 360 < my < 400:
            Menu_buy_no_over.draw(640,460)
        else:
            Menu_buy_no.draw(640,460)

    update_canvas()



