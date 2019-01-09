"""gaurav"""
from random import randint
import config
import person


class enemy_1(person.Person):
    """gaurav"""
    def __init__(self, xarg, yawn):
        person.Person.__init__(self, xarg, yawn)
        self.char = "e"
        self.x_original = xarg
        self.y_original = yawn
        self.follow_coefficient = -1
        self.velocity = randint(10999, 11099)
        self.temp = 0

    def get_x(self):
        """gaurav"""
        if len(config.ENEMY_COUNT) > 0:
            return self.xarg
        else:
            return -100

    def get_y(self):
        """gaurav"""
        if len(config.ENEMY_COUNT) > 0:
            return self.yawn
        else:
            return -100

    def follow(self, x_player, xarg):
        """gaurav"""
        self.temp = 1
        if x_player < xarg:
            return -1
        else:
            return 1

    def detect_collision(self, map_mario):
        """gaurav"""
        if map_mario[self.get_x()][self.get_y()-1] == "#" \
            or map_mario[self.get_x()][self.get_y()+1] == "#":
            self.follow_coefficient = self.follow_coefficient*(-1)

    def undo(self, map_mario, yawn, xarg):
        """gaurav"""
        self.temp = 1
        map_mario[xarg][yawn] = " "
