"""gaurav"""


class Bullet(object):
    """gaurav"""

    def __init__(self, xarg, yawn):
        self.xarg = xarg
        self.yawn = yawn
        self.char = "-"
        self.x_original = xarg
        self.y_original = yawn

    def update_pos(self, x_new, y_new, map_mario):
        """gaurav"""
        if map_mario[x_new][y_new] == "@" \
                or map_mario[x_new][y_new+1] == "e" or map_mario[x_new][y_new] == "$":
            map_mario[x_new][y_new] = " "
        else:
            map_mario[x_new][y_new] = self.char

        self.xarg = x_new
        self.yawn = y_new

    def get_x(self):
        """gaurav"""
        return self.xarg

    def get_y(self):
        """gaurav"""
        return self.yawn
