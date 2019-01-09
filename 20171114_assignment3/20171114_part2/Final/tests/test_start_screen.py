import os
import sys
import pytest
from importlib import reload
if 'tests' in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), '../'))
elif 'Final' not in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), './Final/'))

import StartScreen
import color
HEIGHT, WIDTH = 37,168
#WIDTH = (int(WIDTH)-4)
#HEIGHT = (int(HEIGHT)-4)

Screen = StartScreen.Start(HEIGHT, WIDTH)
Screen.initialize()
Screen.label() 

class Test_Start_Screen:
     
    def test_temp(self):
        assert True

    def test_object(self):
        '''test objectifying'''
        #print(Screen.height)
        assert isinstance(Screen,object) 
        assert isinstance(Screen.start_screen,list)
        assert isinstance(Screen.mario_start,list)  

    def test_dimensions(self):
        '''test dimensions of start screen'''
        assert (Screen.height,Screen.width)==(37,168)

    def test_initialization(self):
        assert " ____       ___  ___  ___" in Screen.start_screen
        assert "|     |   ||   ||    |   |                            Instructions:" in Screen.start_screen        
        assert "|____ |   ||___||___ |___|" in Screen.start_screen        
        assert "     ||   ||    |    | \\                         1) Press E to start the Easy modeor H to start the Hard mode" in Screen.start_screen        
        assert " ____||___||    |___ |  \\                        2) Press R to restart the Game" in Screen.start_screen
        assert "                                                 3) Press Q to quit the Game" in Screen.start_screen 
        assert "       ___  ___  ___  ___" in Screen.start_screen 
        assert "|\\  /||   ||   |  |  |   |                            Controls:" in Screen.start_screen 
        assert "| \\/ ||___||___|  |  |   |" in Screen.start_screen 
        assert "|    ||   || \\    |  |   |                       1) Use WAD to move the player" in Screen.start_screen 
        assert "|    ||   ||  \\  _|_ |___|                       2) Use F to shoot"+ \
        "(can be used in super mode)" in Screen.start_screen

reload(sys)        
        



    

