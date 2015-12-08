import game_framework
from pico2d import *

import Upgrade_Manager
import Main_Scene

level_hard = None
level_normal = None
level_easy = None
setting_draw = None
button_x, button_y = 0, 0
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


upgrade_data_file = open('Json/upgrade_data.txt','r')
upgrade_data = json.load(upgrade_data_file)
upgrade_data_file.close()
hero1_up = upgrade_data['Upgrade_Hero_1']['level']
hero2_up = upgrade_data['Upgrade_Hero_2']['level']
hero3_up = upgrade_data['Upgrade_Hero_3']['level']
hero4_up = upgrade_data['Upgrade_Hero_4']['level']
hero5_up = upgrade_data['Upgrade_Hero_5']['level']
hero6_up = upgrade_data['Upgrade_Hero_6']['level']
hero7_up = upgrade_data['Upgrade_Hero_7']['level']
hero8_up = upgrade_data['Upgrade_Hero_8']['level']
hero9_up = upgrade_data['Upgrade_Hero_9']['level']
magic1_up = upgrade_data['Upgrade_Magic_1']['level']
magic2_up = upgrade_data['Upgrade_Magic_2']['level']
magic3_up = upgrade_data['Upgrade_Magic_3']['level']

game_data_file = open('Json/game_data.txt','r')
game_data = json.load(game_data_file)
game_data_file.close()
diamond = game_data['Game_Diamond']['diamond']

hero6_buy = None
hero7_buy = None
hero8_buy = None
hero9_buy = None

class MenuBackGround:
    def __init__(self):
        self.x, self.y = 640, 360
        self.image = load_image('UI/MainMenu.png')
        self.bgm = load_music('Sound/menu_bgm.mp3')
        self.bgm.set_volume(64)
        self.bgm.repeat_play()

    def draw(self):
        self.image.draw(self.x, self.y)


class MenuSound:
    button_sound = None
    search_sound = None
    upgrade_sound = None
    ss_sound = None
    buy_sound = None
    level_sound = None

    def __init__(self):
        if MenuSound.button_sound == None:
            MenuSound.button_sound = load_wav('Sound/menu_GameClick.wav')
            MenuSound.button_sound.set_volume(64)

        if MenuSound.search_sound == None:
            MenuSound.search_sound = load_wav('Sound/menu_SearchClick.wav')
            MenuSound.search_sound.set_volume(64)

        if MenuSound.ss_sound == None:
            MenuSound.ss_sound = load_wav('Sound/menu_SearchSound.wav')
            MenuSound.ss_sound.set_volume(64)

        if MenuSound.upgrade_sound == None:
            MenuSound.upgrade_sound = load_wav('Sound/menu_upgrade.wav')
            MenuSound.upgrade_sound.set_volume(64)

        if MenuSound.buy_sound == None:
            MenuSound.buy_sound = load_wav('Sound/Hero_buy.wav')
            MenuSound.buy_sound.set_volume(64)

        if MenuSound.level_sound == None:
            MenuSound.level_sound = load_wav('Sound/Level_Click.wav')
            MenuSound.level_sound.set_volume(64)

    def buy(self):
        self.buy_sound.play()

    def level(self):
        self.level_sound.play()

    def search2(self):
        self.ss_sound.play()

    def click(self):
        self.button_sound.play()

    def search(self):
        self.search_sound.play()

    def upgrade(self):
        self.upgrade_sound.play()


def enter():
    global MainMenu_bg, Menu_1, Menu_1_over, Menu_2, Menu_2_over, Menu_3, Menu_3_over, Search, Search_over, level_setting, clicksound
    global Menu_buy_yes, Menu_buy_yes_over, Menu_buy_no, Menu_buy_no_over, store_exit, store_exit_over, hero_buy_ask
    global store_main, store_upgrade_1, store_upgrade_2, store_hero1, store_hero1_over, store_hero1_sell, store_hero2, store_hero2_over, store_hero2_sell, store_hero3, store_hero3_over, store_hero3_sell
    global store_hero4, store_hero4_over, store_hero4_sell, store_hero5, store_hero5_over, store_hero5_sell, store_hero6, store_hero6_over, store_hero6_sell, store_hero7, store_hero7_over, store_hero7_sell
    global store_hero8, store_hero8_over, store_hero8_sell, store_hero9, store_hero9_over, store_hero9_sell, store_user_magic_1, store_user_magic_1_over, store_user_magic_2, store_user_magic_2_over, store_user_magic_3, store_user_magic_3_over
    global hero_up_ask, magic_up_ask, upgradestar, star_group, diamond, font, bgm, game_exit


    upgradestar = Upgrade_Manager.UpgradeStar()
    # Json Data Init
    Upgrade_Manager.UpgradeManager.magic_1_star_level = magic1_up
    Upgrade_Manager.UpgradeManager.magic_2_star_level = magic2_up
    Upgrade_Manager.UpgradeManager.magic_3_star_level = magic3_up
    Upgrade_Manager.UpgradeManager.hero_1_star_level = hero1_up
    Upgrade_Manager.UpgradeManager.hero_2_star_level = hero2_up
    Upgrade_Manager.UpgradeManager.hero_3_star_level = hero3_up
    Upgrade_Manager.UpgradeManager.hero_4_star_level = hero4_up
    Upgrade_Manager.UpgradeManager.hero_5_star_level = hero5_up
    Upgrade_Manager.UpgradeManager.hero_6_star_level = hero6_up
    Upgrade_Manager.UpgradeManager.hero_7_star_level = hero7_up
    Upgrade_Manager.UpgradeManager.hero_8_star_level = hero8_up
    Upgrade_Manager.UpgradeManager.hero_9_star_level = hero9_up



    font = load_font('Font/ENCR10B.TTF')
    star_group = []
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

    game_exit = load_image('UI/game_exit.png')

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
    global button_x, button_y, level_easy, level_normal, level_hard, setting_draw, clicksound, herobar, buy_ask, up_ask, up_ask2
    global hero1_sell, hero2_sell, hero3_sell, hero4_sell, hero5_sell, hero6_sell, hero7_sell, hero8_sell, hero9_sell
    global buy_yes, buy_no, hero_upgrade, magic_upgrade, diamond, magic_star_1, magic_star_2, magic_star_3, magic1_up, magic2_up, magic3_up
    global hero6_buy, hero7_buy, hero8_buy, hero9_buy
    global hero1_up, hero2_up, hero3_up, hero4_up, hero5_up, hero6_up, hero7_up, hero8_up, hero9_up
    global hero_star_1, hero_star_2, hero_star_3, hero_star_4,hero_star_5, hero_star_6, hero_star_7, hero_star_8, hero_star_9
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_MOUSEMOTION:
            button_x, button_y = event.x, 720 - event.y
        else:
            if (event.type, event.button) == (SDL_MOUSEBUTTONDOWN, SDL_BUTTON_LEFT ):
                #print(button_x, button_y)
                if 1213 < button_x < 1266 and 653 < button_y < 705:
                    game_framework.quit()
                if 135 < button_x < 566 and 575 < button_y < 670: #전투영웅
                    clicksound.click()
                    hero_upgrade = True
                if 749 < button_x < 1173 and 580 < button_y < 655: #유저영웅
                    clicksound.click()
                    magic_upgrade = True
                if 990 < button_x < 1260 and 312 < button_y < 392: #선술집
                    clicksound.click()
                    herobar = True

                if magic_upgrade == True:
                    if 855 < button_x < 905 and 529 < button_y < 570:
                        clicksound.click()
                        up_ask2 = False
                        magic_upgrade = False

                    if 440 < button_x < 525 and 293 < button_y < 368:
                        clicksound.click()
                        up_ask2 = True
                        magic_star_1 = True
                    if magic_star_1 == True:
                        if diamond > 100:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.upgrade()
                                up_ask2 = False
                                diamond -= 100
                                magic1_up += 1
                                Upgrade_Manager.UpgradeManager.magic_1_star_level += 1
                                if Upgrade_Manager.UpgradeManager.magic_1_star_level > 3:
                                    Upgrade_Manager.UpgradeManager.magic_1_star_level = 3
                                if magic1_up > 3:
                                    magic1_up = 3
                                magic_star_1 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask2 = False
                            magic_star_1 = False
                    if 590 < button_x < 680 and 293 < button_y < 368:
                        clicksound.click()
                        up_ask2 = True
                        magic_star_2 = True
                    if magic_star_2 == True:
                        if diamond > 500:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.upgrade()
                                up_ask2 = False
                                magic2_up += 1
                                diamond -= 500
                                Upgrade_Manager.UpgradeManager.magic_2_star_level += 1
                                if Upgrade_Manager.UpgradeManager.magic_2_star_level > 3:
                                    Upgrade_Manager.UpgradeManager.magic_2_star_level = 3
                                if magic2_up > 3:
                                    magic2_up = 3
                                magic_star_2 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask2 = False
                            magic_star_2 = False
                    if 745 < button_x < 830 and 293 < button_y < 368:
                        clicksound.click()
                        up_ask2 = True
                        magic_star_3 = True
                    if magic_star_3 == True:
                        if diamond > 1000:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.upgrade()
                                up_ask2 = False
                                magic3_up += 1
                                diamond -= 1000
                                Upgrade_Manager.UpgradeManager.magic_3_star_level += 1
                                if Upgrade_Manager.UpgradeManager.magic_3_star_level > 3:
                                    Upgrade_Manager.UpgradeManager.magic_3_star_level = 3
                                if magic3_up > 3:
                                    magic3_up = 3
                                magic_star_3 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask2 = False
                            magic_star_3 = False

                if hero_upgrade == True:
                    if 855 < button_x < 905 and 529 < button_y < 570:
                        clicksound.click()
                        up_ask = False
                        hero_upgrade = False
                    if 372 < button_x < 457 and 388 < button_y < 478:
                        clicksound.click()
                        up_ask = True
                        hero_star_1 = True
                    if hero_star_1 == True:
                        if diamond > 100:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                up_ask = False
                                clicksound.upgrade()
                                hero1_up += 1
                                diamond -= 100
                                Upgrade_Manager.UpgradeManager.hero_1_star_level += 1
                                if Upgrade_Manager.UpgradeManager.hero_1_star_level > 7:
                                    Upgrade_Manager.UpgradeManager.hero_1_star_level = 7
                                if hero1_up > 7:
                                    hero1_up = 7
                                hero_star_1 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask = False
                            hero_star_1 = False

                    if 477 < button_x < 561 and 388 < button_y < 478:
                        clicksound.click()
                        up_ask = True
                        hero_star_2 = True
                    if hero_star_2 == True:
                        if diamond > 300:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                up_ask = False
                                clicksound.upgrade()
                                hero2_up += 1
                                diamond -= 300
                                Upgrade_Manager.UpgradeManager.hero_2_star_level += 1
                                if Upgrade_Manager.UpgradeManager.hero_2_star_level > 7:
                                    Upgrade_Manager.UpgradeManager.hero_2_star_level = 7
                                if hero2_up > 7:
                                    hero2_up = 7
                                hero_star_2 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask = False
                            hero_star_2 = False

                    if 583 < button_x < 667 and 388 < button_y < 478:
                        clicksound.click()
                        up_ask = True
                        hero_star_3 = True
                    if hero_star_3 == True:
                        if diamond > 500:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.upgrade()
                                up_ask = False
                                hero3_up += 1
                                diamond -= 500
                                Upgrade_Manager.UpgradeManager.hero_3_star_level += 1
                                if Upgrade_Manager.UpgradeManager.hero_3_star_level > 7:
                                    Upgrade_Manager.UpgradeManager.hero_3_star_level = 7
                                if hero3_up > 7:
                                    hero3_up = 7
                                hero_star_3 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask = False
                            hero_star_3 = False

                    if 687 < button_x < 775 and 388 < button_y < 478:
                        clicksound.click()
                        up_ask = True
                        hero_star_4 = True
                    if hero_star_4 == True:
                        if diamond > 1000:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.upgrade()
                                up_ask = False
                                hero4_up += 1
                                diamond -= 1000
                                Upgrade_Manager.UpgradeManager.hero_4_star_level += 1
                                if Upgrade_Manager.UpgradeManager.hero_4_star_level > 7:
                                    Upgrade_Manager.UpgradeManager.hero_4_star_level = 7
                                if hero4_up > 7:
                                    hero4_up = 7
                                hero_star_4 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask = False
                            hero_star_4 = False

                    if 796 < button_x < 882 and 388 < button_y < 478:
                        clicksound.click()
                        up_ask = True
                        hero_star_5 = True
                    if hero_star_5 == True:
                        if diamond > 1500:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.upgrade()
                                up_ask = False
                                hero5_up += 1
                                diamond -= 1500
                                Upgrade_Manager.UpgradeManager.hero_5_star_level += 1
                                if Upgrade_Manager.UpgradeManager.hero_5_star_level > 7:
                                    Upgrade_Manager.UpgradeManager.hero_5_star_level = 7
                                if hero5_up > 7:
                                    hero5_up = 7
                                hero_star_5 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask = False
                            hero_star_5 = False

                    if 429 < button_x < 515 and 250 < button_y < 335:
                        clicksound.click()
                        up_ask = True
                        hero_star_6 = True
                    if hero_star_6 == True:
                        if diamond > 2000:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.upgrade()
                                up_ask = False
                                hero6_up += 1
                                diamond -= 2000
                                Upgrade_Manager.UpgradeManager.hero_6_star_level += 1
                                if Upgrade_Manager.UpgradeManager.hero_6_star_level > 7:
                                    Upgrade_Manager.UpgradeManager.hero_6_star_level = 7
                                if hero6_up > 7:
                                    hero6_up = 7
                                hero_star_6 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask = False
                            hero_star_6 = False

                    if 535 < button_x < 622 and 250 < button_y < 335:
                        clicksound.click()
                        up_ask = True
                        hero_star_7 = True
                    if hero_star_7 == True:
                        if diamond > 3000:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.upgrade()
                                up_ask = False
                                hero7_up += 1
                                diamond -= 3000
                                Upgrade_Manager.UpgradeManager.hero_7_star_level += 1
                                if Upgrade_Manager.UpgradeManager.hero_7_star_level > 7:
                                    Upgrade_Manager.UpgradeManager.hero_7_star_level = 7
                                if hero7_up > 7:
                                    hero7_up = 7
                                hero_star_7 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask = False
                            hero_star_7 = False

                    if 642 < button_x < 724 and 250 < button_y < 335:
                        clicksound.click()
                        up_ask = True
                        hero_star_8 = True
                    if hero_star_8 == True:
                        if diamond > 5000:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.upgrade()
                                up_ask = False
                                hero8_up += 1
                                diamond -= 5000
                                Upgrade_Manager.UpgradeManager.hero_8_star_level += 1
                                if Upgrade_Manager.UpgradeManager.hero_8_star_level > 7:
                                    Upgrade_Manager.UpgradeManager.hero_8_star_level = 7
                                if hero8_up > 7:
                                    hero8_up = 7
                                hero_star_8 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask = False
                            hero_star_8 = False

                    if 747 < button_x < 835 and 250 < button_y < 335:
                        clicksound.click()
                        up_ask = True
                        hero_star_9 = True
                    if hero_star_9 == True:
                        if diamond > 7000:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.upgrade()
                                up_ask = False
                                hero9_up += 1
                                diamond -= 7000
                                Upgrade_Manager.UpgradeManager.hero_9_star_level += 1
                                if Upgrade_Manager.UpgradeManager.hero_9_star_level > 7:
                                    Upgrade_Manager.UpgradeManager.hero_9_star_level = 7
                                if hero9_up > 7:
                                    hero9_up = 7
                                hero_star_9 = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            up_ask = False
                            hero_star_9 = False

                if herobar == True:
                    if 855 < button_x < 905 and 529 < button_y < 570:
                        clicksound.click()
                        buy_ask = False
                        herobar = False
                    if 429 < button_x < 515 and 280 < button_y < 365:
                        clicksound.click()
                        buy_ask = True
                        hero6_buy = True
                    if hero6_buy == True:
                        if diamond > 2000:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.buy()
                                buy_ask = False
                                hero6_sell = True
                                diamond -= 2000
                                Upgrade_Manager.HeroBuyManager.sell_6 = 2
                                hero6_buy = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            buy_ask = False
                            hero6_buy = False

                    if 535 < button_x < 622 and 280 < button_y < 365:
                        clicksound.click()
                        buy_ask = True
                        hero7_buy = True
                    if hero7_buy == True:
                        if diamond > 3000:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.buy()
                                buy_ask = False
                                hero7_sell = True
                                diamond -= 3000
                                Upgrade_Manager.HeroBuyManager.sell_7 = 2
                                hero7_buy = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            buy_ask = False
                            hero7_buy = False

                    if 642 < button_x < 724 and 280 < button_y < 365:
                        clicksound.click()
                        buy_ask = True
                        hero8_buy = True
                    if hero8_buy == True:
                        if diamond > 5000:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.buy()
                                buy_ask = False
                                hero8_sell = True
                                diamond -= 5000
                                Upgrade_Manager.HeroBuyManager.sell_8 = 2
                                hero8_buy = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            buy_ask = False
                            hero8_buy = False

                    if 747 < button_x < 835 and 280 < button_y < 365:
                        clicksound.click()
                        buy_ask = True
                        hero9_buy = True
                    if hero9_buy == True:
                        if diamond > 7000:
                            if 566 < button_x < 601 and 360 < button_y < 400:
                                clicksound.buy()
                                buy_ask = False
                                diamond -= 7000
                                hero9_sell = True
                                Upgrade_Manager.HeroBuyManager.sell_9 = 2
                                hero9_buy = False
                        if 679 < button_x < 712 and 360 < button_y < 400:
                            clicksound.click()
                            buy_ask = False
                            hero9_buy = False
                if 458 < button_x < 820 and 40 < button_y < 193:
                    clicksound.search2()
                    setting_draw = True
                if 575 < button_x < 605 and 288 < button_y < 320:
                    clicksound.click()
                    setting_draw = False

                if setting_draw == True:
                    if 610 < button_x < 680 and 430 < button_y < 460:
                        level_easy = True
                        clicksound.level()
                        game_framework.change_state(Main_Scene)
                        setting_draw = False
                    if 610 < button_x < 690 and 390 < button_y < 420:
                        level_normal = True
                        clicksound.level()
                        game_framework.change_state(Main_Scene)
                        setting_draw = False
                    if 610 < button_x < 690 and 340 < button_y < 370:
                        level_hard = True
                        clicksound.level()
                        game_framework.change_state(Main_Scene)
                        setting_draw = False

def update(frame_time):
    pass

def draw(frame_time):
    global button_x, button_y
    global MainMenu_bkg, Menu_1, Menu_1_over, Menu_2, Menu_2_over, Menu_3, Menu_3_over,Search, Search_over
    global Menu_buy_yes, Menu_buy_yes_over, Menu_buy_no, Menu_buy_no_over, store_exit, store_exit_over, buy_ask
    global store_main, store_upgrade_1, store_upgrade_2, store_hero1, store_hero1_over, store_hero1_sell, store_hero2, store_hero2_over, store_hero2_sell, store_hero3, store_hero3_over, store_hero3_sell
    global store_hero4, store_hero4_over, store_hero4_sell, store_hero5, store_hero5_over, store_hero5_sell, store_hero6, store_hero6_over, store_hero6_sell, store_hero7, store_hero7_over, store_hero7_sell
    global store_hero8, store_hero8_over, store_hero8_sell, store_hero9, store_hero9_over, store_hero9_sell, store_user_magic_1, store_user_magic_1_over, store_user_magic_2, store_user_magic_2_over, store_user_magic_3, store_user_magic_3_over
    global hero1_sell, hero2_sell, hero3_sell, hero4_sell, hero5_sell, hero6_sell, hero7_sell, hero8_sell, hero9_sell, hero_buy_ask, Menu_buy_yes, Menu_buy_yes_over, Menu_buy_no, Menu_buy_no_over
    global buy_complete, hero_upgrade, diamond

    clear_canvas()
    MainMenu_bg.draw()
    if 135 < button_x < 566 and 575 < button_y < 670:
        Menu_1_over.draw(640, 360)
    else:
        Menu_1.draw(640, 360)

    if 749 < button_x < 1173 and 580 < button_y < 655:
        Menu_2_over.draw(640, 360)
    else:
        Menu_2.draw(640, 360)

    if 990 < button_x < 1260 and 312 < button_y < 392:
        Menu_3_over.draw(640, 360)
    else:
        Menu_3.draw(640, 360)

    if 458 < button_x < 820 and 40 < button_y < 193:
        Search_over.draw(640, 360)
    else:
        Search.draw(640, 360)

    if setting_draw == True:
        level_setting.draw(640, 400)

    if magic_upgrade == True:
        store_upgrade_2.draw(640,360)
        font.draw(420, 530, '%d' % diamond)
        if 855 < button_x < 905 and 529 < button_y < 570:
            store_exit_over.draw(640,360)
        else:
            store_exit.draw(640,360)
        if 440 < button_x < 525 and 293 < button_y < 368:
            store_user_magic_1_over.draw(640, 360)
        else:
            store_user_magic_1.draw(640, 360)
        if 590 < button_x < 680 and 293 < button_y < 368:
            store_user_magic_2_over.draw(640, 360)
        else:
            store_user_magic_2.draw(640, 360)
        if 745 < button_x < 830 and 293 < button_y < 368:
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
        font.draw(420, 530, '%d' % diamond)
        if 855 < button_x < 905 and 529 < button_y < 570:
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
            if 429 < button_x < 515 and 280 < button_y < 365:
                store_hero6_over.draw(640, 360)
            else:
                store_hero6.draw(640, 360)
        if hero7_sell == True:
            store_hero7_sell.draw(640, 360)
        else:
            if 535 < button_x < 622 and 280 < button_y < 365:
                store_hero7_over.draw(640, 360)
            else:
                store_hero7.draw(640, 360)
        if hero8_sell == True:
            store_hero8_sell.draw(640, 360)
        else:
            if 642 < button_x < 724 and 280 < button_y < 365:
                store_hero8_over.draw(640, 360)
            else:
                store_hero8.draw(640, 360)
        if hero9_sell == True:
            store_hero9_sell.draw(640, 360)
        else:
            if 747 < button_x < 835 and 280 < button_y < 365:
                store_hero9_over.draw(640, 360)
            else:
                store_hero9.draw(640, 360)

    if hero_upgrade == True:
        store_upgrade_1.draw(640, 360)
        font.draw(420, 530, '%d' % diamond)
        if 855 < button_x < 905 and 529 < button_y < 570:
            store_exit_over.draw(640,360)
        else:
            store_exit.draw(640,360)

        if 372 < button_x < 457 and 388 < button_y < 478:
            store_hero1_over.draw(640, 360)
        else:
            store_hero1.draw(640, 360)
        if 477 < button_x < 561 and 388 < button_y < 478:
            store_hero2_over.draw(640, 360)
        else:
            store_hero2.draw(640, 360)
        if 583 < button_x < 667 and 388 < button_y < 478:
            store_hero3_over.draw(640, 360)
        else:
            store_hero3.draw(640, 360)
        if 687 < button_x < 775 and 388 < button_y < 478:
            store_hero4_over.draw(640, 360)
        else:
            store_hero4.draw(640, 360)
        if 796 < button_x < 882 and 388 < button_y < 478:
            store_hero5_over.draw(640, 360)
        else:
            store_hero5.draw(640, 360)
        if 429 < button_x < 515 and 250 < button_y < 335:
            store_hero6_over.draw(640, 330)
        else:
            store_hero6.draw(640, 330)
        if 535 < button_x < 622 and 250 < button_y < 335:
            store_hero7_over.draw(640, 330)
        else:
            store_hero7.draw(640, 330)
        if 642 < button_x < 724 and 250 < button_y < 335:
            store_hero8_over.draw(640, 330)
        else:
            store_hero8.draw(640, 330)
        if 747 < button_x < 835 and 250 < button_y < 335:
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
        if 566 < button_x < 601 and 360 < button_y < 400:
            Menu_buy_yes_over.draw(640,460)
        else:
            Menu_buy_yes.draw(640,460)
        if 679 < button_x < 712 and 360 < button_y < 400:
            Menu_buy_no_over.draw(640,460)
        else:
            Menu_buy_no.draw(640,460)

    if up_ask2 == True:
        magic_up_ask.draw(640, 460)
        if 566 < button_x < 601 and 360 < button_y < 400:
            Menu_buy_yes_over.draw(640,460)
        else:
            Menu_buy_yes.draw(640,460)
        if 679 < button_x < 712 and 360 < button_y < 400:
            Menu_buy_no_over.draw(640,460)
        else:
            Menu_buy_no.draw(640,460)

    if up_ask == True:
        hero_up_ask.draw(640, 460)
        if 566 < button_x < 601 and 360 < button_y < 400:
            Menu_buy_yes_over.draw(640,460)
        else:
            Menu_buy_yes.draw(640,460)
        if 679 < button_x < 712 and 360 < button_y < 400:
            Menu_buy_no_over.draw(640,460)
        else:
            Menu_buy_no.draw(640,460)

    if 1213 < button_x < 1266 and 653 < button_y < 705:
        game_exit.opacify(0.5)
        game_exit.draw(1240, 680)
    else:
        game_exit.opacify(1)
        game_exit.draw(1240, 680)

    update_canvas()



