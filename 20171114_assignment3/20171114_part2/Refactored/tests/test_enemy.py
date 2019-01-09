import os
import sys
import pytest
from importlib import reload
if 'tests' in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), '../'))
elif 'Refactored' not in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), './Refactored/'))

import config
import small_enemy
import scene
import mario_player
import person

HEIGHT, WIDTH = 37,168

class Test_enemy:

    def test_follow(self):
        enemy = small_enemy.enemy_1(HEIGHT-4,WIDTH-12)
        Mario = scene.Mario_map(HEIGHT,WIDTH)
        Mario.initialize()
        enemy.draw(Mario.map_mario) 
        Player = mario_player.Mario(HEIGHT-4,WIDTH-13)
        Player.draw(Mario.map_mario)
        assert enemy.follow(Player.get_y(),enemy.y_original) == -1
        Player2 = mario_player.Mario(HEIGHT-4,WIDTH-11)
        Player2.draw(Mario.map_mario)
        assert enemy.follow(Player2.get_y(),enemy.y_original) == 1


    def test_detect(self):
        Mario = scene.Mario_map(HEIGHT,WIDTH)
        Mario.initialize()
        enemy = small_enemy.enemy_1(HEIGHT-4,WIDTH-12)
        config.enemy_count.append(enemy)
        enemy.draw(Mario.map_mario)
        assert enemy.follow_coefficient == -1
        Mario.map_mario[HEIGHT-4][WIDTH-11] = "#"
        assert Mario.map_mario[HEIGHT-4][WIDTH-11] == "#"
        enemy.detect_collision(Mario.map_mario)
        assert enemy.follow_coefficient == 1

    def test_smash(self):
        Mario = scene.Mario_map(HEIGHT,WIDTH)
        Mario.initialize()
        enemy = small_enemy.enemy_1(HEIGHT-4,WIDTH-12)
        config.enemy_count.append(enemy)
        enemy.draw(Mario.map_mario)
        Player = mario_player.Mario(HEIGHT-5,WIDTH-12)
        Player.draw(Mario.map_mario)
        assert Mario.map_mario[HEIGHT-4][WIDTH-12] == "e"
        Mario.smash_enemy(Player.get_y(),Player.get_x())
        assert Mario.map_mario[HEIGHT-4][WIDTH-12] == "."



    