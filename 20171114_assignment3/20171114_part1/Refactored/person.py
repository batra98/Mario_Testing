"""gaurav"""
class Person(object):
    """gaurav"""
    def __init__(self, xarg, yawn):
        self.xarg = xarg
        self.yawn = yawn
        self.char = "m"

    def draw(self, map_mario):
        """gaurav"""
        map_mario[self.xarg][self.yawn] = self.char

    def get_x(self):
        """gaurav"""
        return self.xarg

    def get_y(self):
        """gaurav"""
        return self.yawn

    def update_pos(self, map_mario, x_new, y_new):
        """gaurav"""
        map_mario[x_new][y_new] = self.char
        map_mario[self.xarg][self.yawn] = " "
        self.xarg = x_new
        self.yawn = y_new
