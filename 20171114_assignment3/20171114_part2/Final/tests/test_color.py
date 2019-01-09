import os
import sys
import pytest
from importlib import reload
if 'tests' in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), '../'))
elif 'Final' not in os.getcwd():
	sys.path.insert(0, os.path.join(os.getcwd(), './Final/'))

import color

class Test_color:

    def test_color(self):
        assert 'Light Red' in color.COLORS
        assert 'Brown' in color.COLORS 
        assert 'Blue' in color.COLORS 
        assert 'Light Blue' in color.COLORS 
        assert 'Purple' in color.COLORS 
        assert 'Yellow' in color.COLORS 
        assert 'Red' in color.COLORS 
        assert 'White' in color.COLORS 


     
    def test_char(self):
        assert color.getcolor("m") == color.COLORS['Light Red']+'m'+'\x1b[0m'
        assert color.getcolor("#") == color.COLORS['Brown']+'#'+'\x1b[0m'
        assert color.getcolor("-") == color.COLORS['Blue']+'-'+'\x1b[0m'
        assert color.getcolor(")") == color.COLORS['Light Blue']+')'+'\x1b[0m'
        assert color.getcolor("(") == color.COLORS['Light Blue']+'('+'\x1b[0m'
        assert color.getcolor("$") == color.COLORS['Purple']+'$'+'\x1b[0m'
        assert color.getcolor("e") == color.COLORS['Yellow']+'e'+'\x1b[0m'
        assert color.getcolor("&") == color.COLORS['Red']+'&'+'\x1b[0m'
        assert color.getcolor("M") == color.COLORS['White']+'M'+'\x1b[0m'
        assert color.getcolor("S") == color.COLORS['Yellow']+'S'+'\x1b[0m'
        assert color.getcolor(".") == color.COLORS['Purple']+'.'+'\x1b[0m'
        assert color.getcolor("*") == color.COLORS['White']+'*'+'\x1b[0m'
reload(sys)        