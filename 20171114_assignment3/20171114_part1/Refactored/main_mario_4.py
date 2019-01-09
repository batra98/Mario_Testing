"""gaurav"""
import os
import time
from random import randint
import NonBlockingInput as hack
import config
import scene
import mario_player
import coins
import small_enemy
import clouds
import poles
import cake
import pistol
import bulletclass
import ending
import flag_1


def init_game(height, width, level):
    """gaurav"""
    config.mario = scene.Mario_map(height, width)

    config.mario.initialize()
    config.ENEMY = []

    config.coin = coins.Coins()
    config.cake = cake.Cakes()
    config.pistol = pistol.Pistol()
    config.flagger = flag_1.Flag(config.mario.map_mario)

    if level == 1:
        counter = 3
    elif level == 2:
        counter = 4

    # initialize enemies
    for j in range(0, counter-2):
        for i in config.mario.boundary:
            enemy_original_y = i+randint(int(width/2), width-15)
            enemy_original_x = height-4
            config.ENEMY.append(small_enemy.enemy_1(
                enemy_original_x, enemy_original_y))
    for i in config.mario.boundary:
        number = randint(counter, counter+2)
        for count in range(0, number):
            cloud = clouds.Clouds(config.mario.map_mario)
            cloud_x, cloud_y = randint(30, 140)+i, randint(3, 5)
            cloud.update(number, cloud_y, cloud_x)
            config.CLOUDS.append(cloud)

    # initialize pillars
    for i in config.mario.boundary:
        for count in range(0, counter):
            pole = poles.Poles(config.mario.map_mario)
            pole_x, pole_y = randint(int(width/2), width-15)+i, height-4
            pole.draw(pole_x, pole_y)
            config.POLES.append(pole)

    # initialize stairs
    for count in range(0, 3):
        config.ending = ending.End(config.mario.map_mario)
        stair_x, stair_y = width*6+20+count*21, height-10
        config.ending.draw_left(stair_x, stair_y, height, width)
        stair_x, stair_y = width*6+31+count*21, height-10
        config.ending.draw_right(stair_x, stair_y, height, width)
        config.STAIR_COORDINATES.append([stair_x, stair_y])

    # initialize coins
    for j in range(0, 4):
        for i in range(0, 6):
            j = j
            temp = randint(height-14, height-8)
            air = randint(int(width/12), width-24)
            boom = air+12
            config.coin.set_position(temp, air, randint(
                0, 13), config.mario.boundary[i])
            config.coin.set_position(temp, air, randint(
                0, 13), config.mario.boundary[i])
            config.mario.make_wall(temp, air, boom, config.CHAR, i)
            config.mario.make_wall(temp-1, air, boom, config.CHAR, i)
            if i % 3 == 0:
                cake_y, cake_x = temp, air + \
                    randint(1, 11)+config.mario.boundary[i]
                config.cake.set_position(cake_y, cake_x)
            if i % 3 == 1:
                pistol_y, pistol_x = temp, air + \
                    randint(1, 11)+config.mario.boundary[i]
                config.pistol.set_position(pistol_y, pistol_x)

    # initialize variables
    config.X_FLAG = width*6+int(width/2)+30
    config.Y_FLAG = height-14
    config.flagger.draw_2(config.Y_FLAG, config.X_FLAG)
    config.DISTANCE = 0
    config.SCORE = 0
    config.INDEX = 0
    config.COUNTER = 0
    config.COUNTER_BACK = 0
    config.START_X = 0
    os.system('clear')
    print("score- "+str(config.SCORE)+" "+"distance- "+str(config.DISTANCE))
    config.player = mario_player.Mario(int(height-4), 0)
    config.player.draw(config.mario.map_mario)
    for items in config.ENEMY:
        items.draw(config.mario.map_mario)
        config.ENEMY_COUNT.append(1)
    config.mario.print_map(int(width), int(height), config.START_X)
    config.FINAL_HEIGHT = height-4
    config.LIMIT = 0
    config.FLAG = 1
    config.follow_coefficient = -1
    config.GAME_OVER = False
    config.BIG_MARIO = False
    os.system('aplay -qN ./sound/theme.wav &')

# function to update map


def update_map(height, width, verify, steps):
    """gaurav"""
    os.system('clear')
    print("score- "+str(config.SCORE)+" "+"distance- "+str(config.DISTANCE))
    if config.player.get_y() < int(width/2):
        config.mario.print_map(int(width), int(height), config.START_X)
    else:
        if verify is True:
            config.COUNTER_BACK = config.COUNTER_BACK+steps
        config.mario.print_map(int(width)+config.COUNTER_BACK,
                               int(height), config.START_X+config.COUNTER_BACK)


def main(level=1):
    """gaurav"""
    height, width = os.popen('stty size', 'r').read().split()
    width = (int(width)-4)
    height = (int(height)-4)
    kick = hack.KBHit()

    init_game(height, width, level)

    start_time = time.time()

    while 1:

        if time.time()-start_time > 89:
            os.system('aplay -qN ./sound/theme.wav &')
            start_time = time.time()

        if config.BIG_MARIO is False:
            while config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                != '#' and config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                    != '&':

                if kick.kbhit() and config.FLAG == 1:
                    text_2 = kick.getch()
                    config.FLAG = 0
                else:
                    text_2 = 'p'

                if text_2 == 'd':
                    config.DISTANCE += 1
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y()+3)
                    if config.player.get_y() > int(width/2):
                        config.COUNTER_BACK = config.COUNTER_BACK

                elif text_2 == 'a':
                    config.DISTANCE -= 1
                    config.player.update_pos(
                        config.mario.map_mario,
                        config.player.get_x(),
                        max(config.player.get_y()-3, 0))
                    if config.player.get_y() > int(width/2):
                        config.COUNTER_BACK = config.COUNTER_BACK
                else:
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x()+1, config.player.get_y())
                    update_map(height, width, False, 1)
                    time.sleep(0.02)

            config.FLAG = 1
            xarg = -1
            yawn = -1
            coin_show = False
            for enemies in config.ENEMY:
                if config.player.get_y() == enemies.get_y() \
                        and config.player.get_x() == enemies.get_x():
                    if config.GAME_OVER is False:
                        os.system('pkill -kill aplay')
                        os.system('aplay -qN ./sound/mariodie.wav &')
                    config.mario.end_game(config.player.get_y(
                    ), config.player.get_x(), config.SCORE, config.DISTANCE)
                    update_map(height, width, False, 1)
                    config.GAME_OVER = True
                    break

            if kick.kbhit():
                text = kick.getch()
            else:
                text = 'p'

            if text == 'r':
                os.system('pkill -kill aplay')
                os.system('aplay -qN ./sound/reset.wav &')
                init_game(height, width, level)

            if text == 'q':
                os.system('pkill -kill aplay')
                break
            if config.GAME_OVER is False:

                if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] == "@":
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.SCORE = config.SCORE+5
                    config.player.char = "M"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y()+1)
                    update_map(height, width, True, 1)
                    config.BIG_MARIO = True

                if config.mario.map_mario[config.player.get_x()][config.player.get_y()] == "@":
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.SCORE = config.SCORE+5
                    config.player.char = "M"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y())
                    update_map(height, width, True, 1)
                    config.BIG_MARIO = True

                if config.mario.map_mario[config.player.get_x()][config.player.get_y()-1] == "@":
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.SCORE = config.SCORE+5
                    config.player.char = "M"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y()-1)
                    update_map(height, width, True, -1)
                    config.BIG_MARIO = True

                if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "@":
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.SCORE = config.SCORE+5
                    config.player.char = "M"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y())
                    update_map(height, width, False, 1)
                    config.BIG_MARIO = True

                if config.mario.map_mario[config.player.get_x()-1][config.player.get_y()] == "@":
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.SCORE = config.SCORE+5
                    config.player.char = "M"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y())
                    update_map(height, width, False, 1)
                    config.BIG_MARIO = True

                if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] == "+":
                    os.system('pkill -kill aplay')
                    return 1
                if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()+1] == "+":
                    os.system('pkill -kill aplay')
                    return 1
                if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "+":
                    os.system('pkill -kill aplay')
                    return 1
                if config.mario.map_mario[config.player.get_x()][config.player.get_y()] == "+":
                    os.system('pkill -kill aplay')
                    return 1

                if text == 'd':
                    config.DISTANCE += 1
                    if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] \
                            != "#":
                        config.player.update_pos(
                            config.mario.map_mario, config.player.get_x(), config.player.get_y()+1)
                        update_map(height, width, True, 1)

                    else:
                        update_map(height, width, False, 1)

                elif text == 'a':
                    config.DISTANCE -= 1
                    config.COUNTER = config.COUNTER-1
                    if config.mario.map_mario[config.player.get_x()][config.player.get_y()-1] \
                            != "#":
                        config.player.update_pos(
                            config.mario.map_mario,
                            config.player.get_x(),
                            max(config.player.get_y()-1, 0))
                        update_map(height, width, True, -1)

                    else:
                        update_map(height, width, False, 1)

                elif text == 'w':
                    os.system('clear')
                    print("score- "+str(config.SCORE)+" " +
                          "distance- "+str(config.DISTANCE))
                    os.system('aplay -qN ./sound/jump.wav &')
                    while config.mario.map_mario[config.player.get_x()-1][config.player.get_y()] \
                        != '#' and config.player.get_x() > config.FINAL_HEIGHT-14 \
                        and config.mario.map_mario[config.player.get_x()-1][config.player.get_y()] \
                            != '&':
                        config.player.update_pos(
                            config.mario.map_mario, config.player.get_x()-1, config.player.get_y())
                        update_map(height, width, False, 1)
                        time.sleep(0.02)

                    if config.mario.map_mario[config.player.get_x()-1][config.player.get_y()] \
                            == '#':
                        config.mario.shift_up(
                            config.player.get_x()-1, config.player.get_y())
                        xarg = config.player.get_x()-3
                        yawn = config.player.get_y()
                        if [xarg+2, yawn] in config.coin.coin_position or [xarg+1, yawn] \
                                in config.coin.coin_position:
                            config.coin.show(
                                config.mario.map_mario, xarg-1, yawn)
                            coin_show = True
                            os.system('aplay -qN ./sound/coin.wav &')
                        if [xarg+2, yawn, False] in config.cake.cake_position \
                                or [xarg+1, yawn, False] in config.cake.cake_position:
                            os.system('aplay -qN ./sound/powerup_appear.wav &')
                            config.cake.draw(
                                config.mario.map_mario, xarg-1, yawn)
                            try:
                                config.cake.cake_position.remove(
                                    [xarg+2, yawn, False])
                            except Exception:
                                pass
                            try:
                                config.cake.cake_position.remove(
                                    [xarg+1, yawn, False])
                            except Exception:
                                pass
                            config.cake.cake_position.append(
                                [xarg-1, yawn, True])

                    flag = 1
                    while config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                            != '#' and config.mario.map_mario[config.player.get_x()+1] \
                            [config.player.get_y()] != '&':
                        if kick.kbhit() and flag == 1:
                            text_2 = kick.getch()
                            flag = 0
                        else:
                            text_2 = 'p'

                        if text_2 == 'd':
                            config.DISTANCE += 2
                            if config.mario.map_mario[config.player.get_x()] \
                                [config.player.get_y()+1] != '#':
                                config.player.update_pos(
                                    config.mario.map_mario,
                                    config.player.get_x(),
                                    config.player.get_y()+2)
                                if config.player.get_y() > int(width/2):
                                    config.COUNTER_BACK = config.COUNTER_BACK+2

                            else:
                                config.player.update_pos(
                                    config.mario.map_mario,
                                    config.player.get_x()+1,
                                    config.player.get_y())
                        elif text_2 == 'a':
                            config.DISTANCE -= 2
                            config.player.update_pos(
                                config.mario.map_mario,
                                config.player.get_x(),
                                max(config.player.get_y()-2, 0))
                            if config.player.get_y() > int(width/2):
                                config.COUNTER_BACK = config.COUNTER_BACK-2
                        else:
                            config.player.update_pos(
                                config.mario.map_mario,
                                config.player.get_x()+1,
                                config.player.get_y())
                        update_map(height, width, False, 1)
                        time.sleep(0.02)

                        if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                                == "e":
                            os.system('aplay -qN ./sound/stomp.wav &')
                            config.mario.smash_enemy(
                                config.player.get_y(), config.player.get_x())
                            config.SCORE = config.SCORE+10
                            config.ENEMY_COUNT.remove(1)
                            for items in config.ENEMY:
                                if items.get_x() == config.player.get_x()+1 \
                                        and items.get_y() == config.player.get_y():
                                    config.ENEMY.remove(items)
                                    break
                            update_map(height, width, False, 1)

                        if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                                == "@":
                            os.system('aplay -qN ./sound/powerup_take.wav &')
                            if config.SUPER_MARIO is False:
                                config.SCORE = config.SCORE+5
                                config.player.char = "M"
                            config.player.update_pos(
                                config.mario.map_mario,
                                config.player.get_x(),
                                config.player.get_y())
                            update_map(height, width, False, 1)
                            config.BIG_MARIO = True

                if xarg != -1 and yawn != -1:
                    config.mario.shift_down(xarg, yawn)
                    if coin_show is True:
                        config.SCORE = config.coin.disappear_coin(
                            config.mario.map_mario, xarg-1, yawn, config.SCORE)
                        if [xarg+1, yawn] in config.coin.coin_position:
                            config.coin.coin_position.remove([xarg+1, yawn])

                        if [xarg+2, yawn] in config.coin.coin_position:
                            config.coin.coin_position.remove([xarg+2, yawn])

                        config.coin.change_brick(
                            config.mario.map_mario, xarg+1, yawn, "&")
                        config.coin.change_brick(
                            config.mario.map_mario, xarg+2, yawn, "&")

                for positions in config.cake.cake_position:
                    if positions[2] is True and config.INDEX % (1000) == 0:

                        while config.mario.map_mario[positions[0]+1][positions[1]] \
                            != "#" and config.mario.map_mario[positions[0]+1][positions[1]] \
                                != "&":
                            config.cake.update_pos(
                                positions[0]+1,
                                positions[1],
                                config.mario.map_mario,
                                positions[0],
                                positions[1])
                            positions[0] = positions[0]+1

                for enemies in config.ENEMY:

                    if enemies.get_y() < enemies.y_original-width/6:
                        enemies.follow_coefficient = 1
                    elif enemies.get_y() > enemies.y_original+width/6:
                        enemies.follow_coefficient = -1

                    if abs(config.player.get_y()-enemies.get_y()) <= 10:
                        enemies.follow_coefficient = enemies.follow(
                            config.player.get_y(), enemies.get_y())
                    try:
                        enemies.detect_collision(config.mario.map_mario)
                    except Exception:
                        config.ENEMY.remove(enemies)
                    if config.INDEX % (10999) == 0:

                        try:
                            enemies.update_pos(config.mario.map_mario, enemies.get_x(
                            ), enemies.get_y()+enemies.follow_coefficient)
                        except Exception:
                            config.ENEMY.remove(enemies)

                if config.INDEX % (10999) == 0:

                    update_map(height, width, False, 1)
                config.INDEX = config.INDEX+1

                if config.COUNTER_BACK <= 0:
                    config.COUNTER_BACK = 0
                if config.COUNTER_BACK > width*7:
                    print("You won")
                    break
                config.FINAL_HEIGHT = config.player.get_x()
            else:
                time.sleep(0.02)

        elif config.BIG_MARIO is True:
            while config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                != '#' and config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                    != '&':
                if kick.kbhit() and config.FLAG == 1:
                    text_2 = kick.getch()
                    config.FLAG = 0
                else:
                    text_2 = 'p'
                if text_2 == 'd':
                    config.DISTANCE += 1
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y()+3)
                    if config.player.get_y() > int(width/2):
                        config.COUNTER_BACK = config.COUNTER_BACK

                elif text_2 == 'a':
                    config.DISTANCE -= 1
                    config.player.update_pos(
                        config.mario.map_mario,
                        config.player.get_x(),
                        max(config.player.get_y()-3, 0))
                    if config.player.get_y() > int(width/2):
                        config.COUNTER_BACK = config.COUNTER_BACK
                else:
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x()+1, config.player.get_y())
                    update_map(height, width, False, 1)
                    time.sleep(0.02)

            config.FLAG = 1
            xarg = -1
            yawn = -1
            coin_show = False
            for enemies in config.ENEMY:

                if config.player.get_y() == enemies.get_y() \
                        and config.player.get_x() == enemies.get_x():
                    os.system('aplay -qN ./sound/collision.wav &')
                    if config.SUPER_MARIO is False:
                        config.BIG_MARIO = False
                        config.player.char = "m"
                    elif config.SUPER_MARIO is True:
                        config.SUPER_MARIO = False
                        config.player.char = "M"
                    enemies.undo(config.mario.map_mario,
                                 enemies.get_y(), enemies.get_x())
                    config.ENEMY.remove(enemies)
                    update_map(height, width, False, 1)

            if kick.kbhit():
                text = kick.getch()
            else:
                text = 'p'

            if text == 'r':
                os.system('pkill -kill aplay')
                os.system('aplay -qN ./sound/reset.wav &')
                init_game(height, width, level)

            if text == 'q':
                os.system('pkill -kill aplay')
                break
            if config.GAME_OVER is False:

                if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] == "@":
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.SCORE = config.SCORE+5
                    if config.SUPER_MARIO is False:
                        config.player.char = "M"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y()+1)
                    update_map(height, width, True, 1)

                if config.mario.map_mario[config.player.get_x()][config.player.get_y()] == "@":
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.SCORE = config.SCORE+5
                    if config.SUPER_MARIO is False:
                        config.player.char = "M"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y())
                    update_map(height, width, True, 1)

                if config.mario.map_mario[config.player.get_x()][config.player.get_y()-1] == "@":
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.SCORE = config.SCORE+5
                    if config.SUPER_MARIO is False:
                        config.player.char = "M"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y()-1)
                    update_map(height, width, True, -1)

                if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "@":
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.SCORE = config.SCORE+5
                    if config.SUPER_MARIO is False:
                        config.player.char = "M"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y())
                    update_map(height, width, False, 1)

                if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] == "$":
                    config.SCORE = config.SCORE+5
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.player.char = "S"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y()+1)
                    update_map(height, width, True, 1)
                    config.SUPER_MARIO = True

                if config.mario.map_mario[config.player.get_x()][config.player.get_y()] == "$":
                    config.SCORE = config.SCORE+5
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.player.char = "S"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y())
                    update_map(height, width, True, 1)
                    config.SUPER_MARIO = True

                if config.mario.map_mario[config.player.get_x()][config.player.get_y()-1] == "$":
                    config.SCORE = config.SCORE+5
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.player.char = "S"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y()-1)
                    update_map(height, width, True, -1)
                    config.SUPER_MARIO = True

                if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "$":
                    config.SCORE = config.SCORE+5
                    os.system('aplay -qN ./sound/powerup_take.wav &')
                    config.player.char = "S"
                    config.player.update_pos(
                        config.mario.map_mario, config.player.get_x(), config.player.get_y())
                    update_map(height, width, False, 1)
                    config.SUPER_MARIO = True

                if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] == "+":
                    os.system('pkill -kill aplay')
                    return 1
                if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()+1] == "+":
                    os.system('pkill -kill aplay')
                    return 1
                if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] == "+":
                    os.system('pkill -kill aplay')
                    return 1
                if config.mario.map_mario[config.player.get_x()][config.player.get_y()] == "+":
                    os.system('pkill -kill aplay')
                    return 1

                if text == 'd':
                    config.DISTANCE += 1

                    if config.mario.map_mario[config.player.get_x()][config.player.get_y()+1] \
                            != "#":
                        config.player.update_pos(
                            config.mario.map_mario, config.player.get_x(), config.player.get_y()+1)
                        update_map(height, width, True, 1)

                    else:
                        update_map(height, width, False, 1)

                elif text == 'a':
                    config.DISTANCE -= 1
                    config.COUNTER = config.COUNTER-1
                    if config.mario.map_mario[config.player.get_x()][config.player.get_y()-1] \
                            != "#":
                        config.player.update_pos(
                            config.mario.map_mario,
                            config.player.get_x(),
                            max(config.player.get_y()-1, 0))
                        update_map(height, width, True, -1)

                    else:
                        update_map(height, width, False, 1)

                elif text == 'w':
                    os.system('clear')
                    print("score- "+str(config.SCORE)+" " +
                          "distance- "+str(config.DISTANCE))
                    os.system('aplay -qN ./sound/jump.wav &')
                    while config.mario.map_mario[config.player.get_x()-1][config.player.get_y()] \
                        != '#' and config.player.get_x() > config.FINAL_HEIGHT-14 \
                        and config.mario.map_mario[config.player.get_x()-1][config.player.get_y()] \
                            != '&':
                        config.player.update_pos(
                            config.mario.map_mario, config.player.get_x()-1, config.player.get_y())

                        update_map(height, width, False, 1)
                        time.sleep(0.02)

                    if config.mario.map_mario[config.player.get_x()-1][config.player.get_y()] \
                            == '#':
                        os.system('aplay -qN ./sound/breakblock.wav &')
                        config.mario.shift_up_big(
                            config.player.get_x()-1, config.player.get_y())
                        xarg = config.player.get_x()-3
                        yawn = config.player.get_y()
                        if [xarg+2, yawn] in config.coin.coin_position \
                                or [xarg+1, yawn] in config.coin.coin_position:
                            config.coin.show(
                                config.mario.map_mario, xarg-1, yawn)
                            coin_show = True
                            os.system('aplay -qN ./sound/coin.wav &')
                        if [xarg+2, yawn, False] in config.cake.cake_position \
                                or [xarg+1, yawn, False] in config.cake.cake_position:
                            os.system('aplay -qN ./sound/powerup_appear.wav &')
                            config.cake.draw(
                                config.mario.map_mario, xarg-1, yawn)
                            try:
                                config.cake.cake_position.remove(
                                    [xarg+2, yawn, False])
                            except Exception:
                                pass
                            try:
                                config.cake.cake_position.remove(
                                    [xarg+1, yawn, False])
                            except Exception:
                                pass
                            config.cake.cake_position.append(
                                [xarg-1, yawn, True])
                        if [xarg+2, yawn, False] in config.pistol.pistol_position \
                                or [xarg+1, yawn, False] in config.pistol.pistol_position:
                            os.system('aplay -qN ./sound/powerup_appear.wav &')
                            config.pistol.draw(
                                config.mario.map_mario, xarg-1, yawn)
                            try:
                                config.pistol.pistol_position.remove(
                                    [xarg+2, yawn, False])
                            except Exception:
                                pass
                            try:
                                config.pistol.pistol_position.remove(
                                    [xarg+1, yawn, False])
                            except Exception:
                                pass
                            config.pistol.pistol_position.append(
                                [xarg-1, yawn, True])

                    flag = 1
                    while config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                        != '#' and \
                        config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                            != '&':
                        if kick.kbhit() and flag == 1:
                            text_2 = kick.getch()
                            flag = 0
                        else:
                            text_2 = 'p'

                        if text_2 == 'd':
                            config.DISTANCE += 4
                            if config.mario.map_mario[config.player.get_x()] \
                                [config.player.get_y()+1] != '#':
                                config.player.update_pos(
                                    config.mario.map_mario,
                                    config.player.get_x(),
                                    config.player.get_y()+4)
                                if config.player.get_y() > int(width/2):
                                    config.COUNTER_BACK = config.COUNTER_BACK+4

                            else:
                                config.player.update_pos(
                                    config.mario.map_mario,
                                    config.player.get_x()+1,
                                    config.player.get_y())

                        elif text_2 == 'a':
                            config.DISTANCE -= 4
                            config.player.update_pos(
                                config.mario.map_mario,
                                config.player.get_x(),
                                max(config.player.get_y()-4, 0))
                            if config.player.get_y() > int(width/2):
                                config.COUNTER_BACK = config.COUNTER_BACK-4
                        else:
                            config.player.update_pos(
                                config.mario.map_mario,
                                config.player.get_x()+1,
                                config.player.get_y())

                        update_map(height, width, False, 1)
                        time.sleep(0.02)

                        if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                                == "e":
                            os.system('aplay -qN ./sound/stomp.wav &')
                            config.mario.smash_enemy(
                                config.player.get_y(), config.player.get_x())
                            config.SCORE = config.SCORE+10
                            config.ENEMY_COUNT.remove(1)
                            for items in config.ENEMY:
                                if items.get_x() == config.player.get_x()+1 \
                                        and items.get_y() == config.player.get_y():
                                    config.ENEMY.remove(items)
                                    break
                            update_map(height, width, False, 1)

                        if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                                == "@":
                            os.system('aplay -qN ./sound/powerup_take.wav &')
                            config.SCORE = config.SCORE+5
                            config.player.char = "M"
                            config.player.update_pos(
                                config.mario.map_mario,
                                config.player.get_x(),
                                config.player.get_y())
                            update_map(height, width, False, 1)
                            config.BIG_MARIO = True

                        if config.mario.map_mario[config.player.get_x()+1][config.player.get_y()] \
                                == "$":
                            config.SCORE = config.SCORE+5
                            os.system('aplay -qN ./sound/powerup_take.wav &')
                            config.player.char = "S"
                            config.player.update_pos(
                                config.mario.map_mario,
                                config.player.get_x(),
                                config.player.get_y())
                            update_map(height, width, False, 1)
                            config.SUPER_MARIO = True

                if xarg != -1 and yawn != -1:
                    config.mario.shift_down_big(xarg, yawn)
                    if coin_show is True:
                        config.SCORE = config.coin.disappear_coin(
                            config.mario.map_mario, xarg-1, yawn, config.SCORE)
                        if [xarg+1, yawn] in config.coin.coin_position:
                            config.coin.coin_position.remove([xarg+1, yawn])

                        if [xarg+2, yawn] in config.coin.coin_position:
                            config.coin.coin_position.remove([xarg+2, yawn])

                        config.coin.change_brick(
                            config.mario.map_mario, xarg+1, yawn, "&")
                        config.coin.change_brick(
                            config.mario.map_mario, xarg+2, yawn, "&")

                for positions in config.cake.cake_position:
                    if positions[2] is True and config.INDEX % (1000) == 0:

                        while config.mario.map_mario[positions[0]+1][positions[1]] \
                                != "#" and config.mario.map_mario[positions[0]+1] \
                                [positions[1]] != "&":
                            config.cake.update_pos(
                                positions[0]+1, positions[1],
                                config.mario.map_mario,
                                positions[0], positions[1])
                            positions[0] = positions[0]+1

                for positions in config.pistol.pistol_position:
                    if positions[2] is True and config.INDEX % (1000) == 0:

                        while config.mario.map_mario[positions[0]+1][positions[1]] \
                            != "#" and config.mario.map_mario[positions[0]+1][positions[1]] \
                                != "&":
                            config.pistol.update_pos(
                                positions[0]+1,
                                positions[1],
                                config.mario.map_mario,
                                positions[0],
                                positions[1])
                            positions[0] = positions[0]+1
                for enemies in config.ENEMY:

                    if enemies.get_y() < enemies.y_original-width/6:
                        enemies.follow_coefficient = 1
                    elif enemies.get_y() > enemies.y_original+width/6:
                        enemies.follow_coefficient = -1

                    if abs(config.player.get_y()-enemies.get_y()) <= 10:
                        enemies.follow_coefficient = enemies.follow(
                            config.player.get_y(), enemies.get_y())
                    try:
                        enemies.detect_collision(config.mario.map_mario)
                    except Exception:
                        config.ENEMY.remove(enemies)
                    if config.INDEX % (10999) == 0:

                        try:
                            enemies.update_pos(config.mario.map_mario, enemies.get_x(
                            ), enemies.get_y()+enemies.follow_coefficient)
                        except Exception:
                            config.ENEMY.remove(enemies)
                for bullets in config.BULLETS:

                    if bullets.get_y() > bullets.y_original+width/6:
                        config.mario.map_mario[bullets.get_x(
                        )][bullets.get_y()] = " "
                        config.BULLETS.remove(bullets)
                    else:

                        if config.INDEX % (1099) == 0:
                            if config.mario.map_mario[bullets.get_x()][bullets.get_y()+1] == "e":
                                config.ENEMY_COUNT.remove(1)
                                for items in config.ENEMY:
                                    if items.get_x() == bullets.get_x() \
                                            and items.get_y() == bullets.get_y()+1:
                                        config.ENEMY.remove(items)
                                        break

                            if config.mario.map_mario[bullets.get_x()][bullets.get_y()] != "S":
                                config.mario.map_mario[bullets.get_x(
                                )][bullets.get_y()] = " "

                            if config.mario.map_mario[bullets.get_x()][bullets.get_y()+1] == "#":
                                config.mario.map_mario[bullets.get_x(
                                )][bullets.get_y()] = " "
                                config.BULLETS.remove(bullets)
                                continue

                            try:

                                bullets.update_pos(
                                    bullets.get_x(), bullets.get_y()+1, config.mario.map_mario)
                            except Exception:

                                config.BULLETS.remove(bullets)
                            update_map(height, width, False, 1)

                if config.SUPER_MARIO is True:
                    if text == "f":
                        os.system('aplay -qN ./sound/fireball.wav &')
                        bullet = bulletclass.Bullet(
                            config.player.get_x(), config.player.get_y())
                        config.BULLETS.append(bullet)

                if config.INDEX % (10999) == 0:
                    update_map(height, width, False, 1)
                config.INDEX = config.INDEX+1

                if config.COUNTER_BACK <= 0:
                    config.COUNTER_BACK = 0
                if config.COUNTER_BACK > width*7:

                    break
                config.FINAL_HEIGHT = config.player.get_x()

            else:
                break

    return 0


if __name__ == '__main__':
    main()
