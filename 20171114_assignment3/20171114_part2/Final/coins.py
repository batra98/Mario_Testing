"""gaurav"""


class Coins(object):
    """gaurav"""

    def __init__(self):
        self.coin_position = []
        self.temp = 0

    def set_position(self, kar, arg, game, index):
        """gaurav"""
        self.coin_position.append([kar, arg+game+index])

    def show(self, map_mario, xarg, yawn):
        """gaurav"""
        map_mario[xarg][yawn] = "*"
        self.temp = 1

    def disappear_coin(self, map_mario, xarg, yawn, score):
        """gaurav"""
        map_mario[xarg][yawn] = " "
        score = score+1
        self.temp = 0
        return score

    def change_brick(self, map_mario, xarg, yawn, char_changed):
        """gaurav"""
        self.temp = 1
        self.temp = char_changed
        map_mario[xarg][yawn] = "&"
