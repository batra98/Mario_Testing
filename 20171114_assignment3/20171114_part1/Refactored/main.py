"""GAURAV"""
import os
from random import randint
import NonBlockingInput as hack
import config
import main_mario_4
import start_screen

HEIGHT, WIDTH = os.popen('stty size', 'r').read().split()
WIDTH = (int(WIDTH)-4)

HEIGHT = (int(HEIGHT)-4)
START = start_screen.Start(HEIGHT, WIDTH)

START.initialize()
START.label()
os.system('clear')
START.draw()

KB = hack.KBHit()
TEXT = "f"
while 1:
    if KB.kbhit():
        TEXT = KB.getch()

    if TEXT == "e":
        BACK = main_mario_4.main(1)
        break
    elif TEXT == "h":
        BACK = main_mario_4.main(2)
        break
    elif TEXT == "q":
        BACK = 0
        break


if BACK == 0:
    print("Game exited normally")
else:
    print("You won")
    print("score- "+str(config.SCORE)+" "+"distance- "+str(config.DISTANCE))
    while config.DROP >= 0:

        if config.DROP % (109999) == 0:

            config.mario.map_mario[config.Y_FLAG -
                                   randint(3, 6)][config.X_FLAG+randint(-9, +9)] = "*"

        if config.DROP % (1099999) == 0:
            os.system('clear')
            os.system('aplay -qN ./sound/fireworks.wav &')
            config.flagger.draw(config.G, config.Y_FLAG, config.X_FLAG)
            main_mario_4.update_map(HEIGHT, WIDTH, False, 1)
            config.G = config.G+1

        config.DROP += 1
        if config.G > 6:
            break

    print("You won")
    print("score- "+str(config.SCORE)+" "+"distance- "+str(config.DISTANCE))
