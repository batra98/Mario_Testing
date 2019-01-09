import os
import sys
import pytest
from importlib import reload
if 'tests' in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), '../'))
elif 'Refactored' not in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), './Refactored/'))

import coins
import cake
import scene
import config
import collectable_objects
import bulletclass
import clouds
import poles

HEIGHT, WIDTH = 37,168
Coin = coins.Coins()
Cakes = cake.Cakes()
Mario = scene.Mario_map(HEIGHT,WIDTH)
Mario.initialize()

class Test_Objects:

    def test_powerup_problem(self):
        Mario.make_wall(HEIGHT-8,WIDTH-24,WIDTH-12,config.char,1)
        Cakes.set_position(HEIGHT-8,WIDTH-14)
        Cakes.draw(Mario.map_mario,HEIGHT-10,WIDTH-14)
        assert Mario.map_mario[HEIGHT-10][WIDTH-14]=="@" or Mario.map_mario[HEIGHT-10][WIDTH-14]=="$"
        Mario.shift_up(HEIGHT-8,WIDTH-14)
        Mario.shift_down(HEIGHT-10,WIDTH-14)
        assert Mario.map_mario[HEIGHT-10][WIDTH-14]=="@" or Mario.map_mario[HEIGHT-11][WIDTH-14]=="$"
        assert not Mario.map_mario[HEIGHT-11][WIDTH-14]=="@" or not Mario.map_mario[HEIGHT-11][WIDTH-14]=="$"

    def test_appearance_coin(self):
        Mario.make_wall(HEIGHT-8,WIDTH-24,WIDTH-12,config.char,0)
        Mario.make_wall(HEIGHT-9,WIDTH-24,WIDTH-12,config.char,0)

        Coin.set_position(HEIGHT-8,WIDTH-24,10,Mario.boundary[0])
        Coin.show(Mario.map_mario,HEIGHT-10,WIDTH-14)
        assert Mario.map_mario[HEIGHT-10][WIDTH-14]=="*"
        assert Mario.map_mario[HEIGHT-9][WIDTH-14]=="#"
        assert Mario.map_mario[HEIGHT-8][WIDTH-14]=="#"
     
        Coin.change_brick(Mario.map_mario,HEIGHT-9,WIDTH-14,"&")
        Coin.change_brick(Mario.map_mario,HEIGHT-8,WIDTH-14,"&")
        assert Mario.map_mario[HEIGHT-9][WIDTH-14]=="&"
        assert Mario.map_mario[HEIGHT-8][WIDTH-14]=="&"
        assert Mario.map_mario[HEIGHT-10][WIDTH-14]=="*"

    def test_bullet(self):
        bullets = bulletclass.Bullet(HEIGHT-4,WIDTH-10)
        bullets.update_pos(HEIGHT-4,WIDTH-9,Mario.map_mario)
        assert (bullets.x_original,bullets.y_original+1)==(bullets.get_x(),bullets.get_y())

    def test_score(self):
        score_original = config.score
        Coin.set_position(HEIGHT-8,WIDTH-24,10,Mario.boundary[0])
        Coin.show(Mario.map_mario,HEIGHT-10,WIDTH-14)
        score_after = Coin.disappear_coin(Mario.map_mario,HEIGHT-10,WIDTH-14,config.score)
        assert score_after == score_original+1

    def test_clouds(self):
        cloud = clouds.Clouds(Mario.map_mario)
        cloud.draw(HEIGHT-4,WIDTH-10)
        assert Mario.map_mario[HEIGHT-4][WIDTH-10]=="("
        assert Mario.map_mario[HEIGHT-4][WIDTH-9]==")"     
        assert Mario.map_mario[HEIGHT-4][WIDTH-8]=="("     
        assert Mario.map_mario[HEIGHT-4][WIDTH-7]==")"     
        assert Mario.map_mario[HEIGHT-4][WIDTH-6]=="("     
        assert Mario.map_mario[HEIGHT-4][WIDTH-5]==")"         
        assert Mario.map_mario[HEIGHT-3][WIDTH-13]=="."
        assert Mario.map_mario[HEIGHT-3][WIDTH-12]=="."
        assert Mario.map_mario[HEIGHT-3][WIDTH-11]=="("
        assert Mario.map_mario[HEIGHT-3][WIDTH-10]==")"
        assert Mario.map_mario[HEIGHT-3][WIDTH-9]=="("
        assert Mario.map_mario[HEIGHT-3][WIDTH-8]==")"
        assert Mario.map_mario[HEIGHT-3][WIDTH-7]=="("
        assert Mario.map_mario[HEIGHT-3][WIDTH-6]==")"

    def test_poles(self):
        pole = poles.Poles(Mario.map_mario)
        pole.draw(WIDTH-24,HEIGHT-8)
        assert Mario.map_mario[HEIGHT-8][WIDTH-24]=="#"
        assert Mario.map_mario[HEIGHT-8][WIDTH-23]=="#"
        assert Mario.map_mario[HEIGHT-8][WIDTH-22]=="#"
        
        



        










reload(sys)




