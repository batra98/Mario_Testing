import os
import sys
import pytest
from importlib import reload
if 'tests' in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), '../'))
elif 'Final' not in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), './Final/'))

import scene
import mario_player

HEIGHT, WIDTH = 37,168


class Test_Mario:

    def test_init(self):
        '''test initial postion of player'''
        Mario = scene.Mario_map(HEIGHT,WIDTH)
        Mario.initialize()
        Player = mario_player.Mario(HEIGHT-4,0)
        Player.draw(Mario.map_mario)
        assert (HEIGHT-4,0)==(Player.get_x(),Player.get_y())
        assert Mario.map_mario[Player.get_x()][Player.get_y()]=="m"


    def test_right(self):
        '''pressing d once'''
        Mario = scene.Mario_map(HEIGHT,WIDTH)
        Mario.initialize()
        Player = mario_player.Mario(HEIGHT-4,0)
        Player.draw(Mario.map_mario)
        x_initial = Player.get_x()
        y_initial = Player.get_y()            
        Player.update_pos(Mario.map_mario,Player.get_x(),Player.get_y()+1)
        assert (Player.get_x(),Player.get_y())==(x_initial,y_initial+1)
        assert Mario.map_mario[Player.get_x()][Player.get_y()]=="m"
        assert Mario.map_mario[x_initial][y_initial]==" "

    def test_left(self):
        '''pressing a once'''
        Mario = scene.Mario_map(HEIGHT,WIDTH)
        Mario.initialize()
        Player = mario_player.Mario(HEIGHT-4,12)
        Player.draw(Mario.map_mario)
        x_initial = Player.get_x()
        y_initial = Player.get_y()
        Player.update_pos(Mario.map_mario,Player.get_x(),Player.get_y()-1)
        assert (Player.get_x(),Player.get_y())==(x_initial,y_initial-1)
        assert Mario.map_mario[Player.get_x()][Player.get_y()]=="m"
        assert Mario.map_mario[x_initial][y_initial]==" "

    def test_up_only(self):
        '''pressing w'''
        Mario = scene.Mario_map(HEIGHT,WIDTH)
        Mario.initialize()
        Player = mario_player.Mario(HEIGHT-4,12)
        Player.draw(Mario.map_mario)
        x_initial = Player.get_x()
        y_initial = Player.get_y()
        while Player.get_x() > HEIGHT-14:
            Player.update_pos(Mario.map_mario,Player.get_x()-1,Player.get_y())
            assert Mario.map_mario[Player.get_x()][Player.get_y()]=="m"
            assert Mario.map_mario[x_initial][y_initial]==" "
        
        assert (Player.get_x(),Player.get_y())==(x_initial-10,y_initial)
        
    def test_up_right(self):
        '''pressing w and d'''
        Mario = scene.Mario_map(HEIGHT,WIDTH)
        Mario.initialize()
        Player = mario_player.Mario(HEIGHT-4,12)
        Player.draw(Mario.map_mario)
        x_initial = Player.get_x()
        y_initial = Player.get_y()
        flag = 1
        while Player.get_x() > HEIGHT-14:
            Player.update_pos(Mario.map_mario,Player.get_x()-1,Player.get_y())
            if flag == 1:
                flag = 0
                Player.update_pos(Mario.map_mario,Player.get_x(),Player.get_y()+4)

        assert (Player.get_x(),Player.get_y())==(x_initial-10,y_initial+4)

    def test_up_left(self):
        '''pressing w and a'''
        Mario = scene.Mario_map(HEIGHT,WIDTH)
        Mario.initialize()
        Player = mario_player.Mario(HEIGHT-4,12)
        Player.draw(Mario.map_mario)
        x_initial = Player.get_x()
        y_initial = Player.get_y()
        flag = 1
        while Player.get_x() > HEIGHT-14:
            Player.update_pos(Mario.map_mario,Player.get_x()-1,Player.get_y())
            if flag == 1:
                flag = 0
                Player.update_pos(Mario.map_mario,Player.get_x(),Player.get_y()-4)

        assert (Player.get_x(),Player.get_y())==(x_initial-10,y_initial-4)

    def test_down_right(self):
        '''falling and pressing d'''
        Mario = scene.Mario_map(HEIGHT,WIDTH)
        Mario.initialize()
        Player = mario_player.Mario(HEIGHT-14,12)
        Player.draw(Mario.map_mario)
        x_initial = Player.get_x()
        y_initial = Player.get_y()
        flag = 1
        while Player.get_x() < HEIGHT-4:
            Player.update_pos(Mario.map_mario,Player.get_x()+1,Player.get_y())
            if flag == 1:
                flag = 0
                Player.update_pos(Mario.map_mario,Player.get_x(),Player.get_y()+4)

        assert (Player.get_x(),Player.get_y())==(x_initial+10,y_initial+4)

    def test_down_left(self):
        '''falling and pressing a'''
        Mario = scene.Mario_map(HEIGHT,WIDTH)
        Mario.initialize()
        Player = mario_player.Mario(HEIGHT-14,12)
        Player.draw(Mario.map_mario)
        x_initial = Player.get_x()
        y_initial = Player.get_y()
        flag = 1
        while Player.get_x() < HEIGHT-4:
            Player.update_pos(Mario.map_mario,Player.get_x()+1,Player.get_y())
            if flag == 1:
                flag = 0
                Player.update_pos(Mario.map_mario,Player.get_x(),Player.get_y()-4)

        assert (Player.get_x(),Player.get_y())==(x_initial+10,y_initial-4)

    

reload(sys)            

        




