import os
import sys
import pytest
from importlib import reload
if 'tests' in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), '../'))
elif 'Refactored' not in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), './Refactored/'))

import color

class Test_color:

    def test_color(self):
        assert 'Light Red' in color.colors
        assert 'Brown' in color.colors 
        assert 'Blue' in color.colors 
        assert 'Light Blue' in color.colors 
        assert 'Purple' in color.colors 
        assert 'Yellow' in color.colors 
        assert 'Red' in color.colors 
        assert 'White' in color.colors 


     
    def test_char(self):
        assert color.getcolor("m") == color.colors['Light Red']+'m'+'\x1b[0m'
        assert color.getcolor("#") == color.colors['Brown']+'#'+'\x1b[0m'
        assert color.getcolor("-") == color.colors['Blue']+'-'+'\x1b[0m'
        assert color.getcolor(")") == color.colors['Light Blue']+')'+'\x1b[0m'
        assert color.getcolor("(") == color.colors['Light Blue']+'('+'\x1b[0m'
        assert color.getcolor("$") == color.colors['Purple']+'$'+'\x1b[0m'
        assert color.getcolor("e") == color.colors['Yellow']+'e'+'\x1b[0m'
        assert color.getcolor("&") == color.colors['Red']+'&'+'\x1b[0m'
        assert color.getcolor("M") == color.colors['White']+'M'+'\x1b[0m'
        assert color.getcolor("S") == color.colors['Yellow']+'S'+'\x1b[0m'
        assert color.getcolor(".") == color.colors['Purple']+'.'+'\x1b[0m'
        assert color.getcolor("*") == color.colors['White']+'*'+'\x1b[0m'
reload(sys)        