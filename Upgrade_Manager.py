import pico2d
import json
import game_framework
import Object_Hero
import Main_Scene

from pico2d import *

class UpgradeStar_Main:
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
        self.upgrade_star = load_image('UI/Upgrade_Star_Main.png')

    def draw(self, x, y):
        self.upgrade_star.draw(x, y)

class UpgradeStar:
    def __init__(self, x = 0, y = 0):
        self.x, self.y = x, y
        self.upgrade_star = load_image('UI/Upgrade_Star.png')

    def draw(self, x, y):
        self.upgrade_star.draw(x, y)

class HeroBuyManager:
    sell_6 = 0
    sell_7 = 0
    sell_8 = 0
    sell_9 = 0
    def __init__(self):
        self.sell_6 = 0
        self.sell_7 = 0
        self.sell_8 = 0
        self.sell_9 = 0

class UpgradeManager:
    hero_1_star_level = 0
    hero_2_star_level = 0
    hero_3_star_level = 0
    hero_4_star_level = 0
    hero_5_star_level = 0
    hero_6_star_level = 0
    hero_7_star_level = 0
    hero_8_star_level = 0
    hero_9_star_level = 0
    magic_1_star_level = 0
    magic_2_star_level = 0
    magic_3_star_level = 0

    def __init__(self):
        self.hero_1_star_level = 0
        self.hero_2_star_level = 0
        self.hero_3_star_level = 0
        self.hero_4_star_level = 0
        self.hero_5_star_level = 0
        self.hero_6_star_level = 0
        self.hero_7_star_level = 0
        self.hero_8_star_level = 0
        self.hero_9_star_level = 0

        self.magic_1_star_level = 0
        self.magic_2_star_level = 0
        self.magic_3_star_level = 0
        self.hero_adell = Object_Hero.Hero_Adell()

