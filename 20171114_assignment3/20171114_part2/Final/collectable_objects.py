"""gaurav"""
class Collectables(object):
    """gaurav"""
    def __init__(self):
        self.char = "*"
        self.xarg = 0
        self.yawn = 0

    def update_pos(self, y_new, x_new, map_mario, y_old, x_old):
        """gaurav"""
        map_mario[y_new][x_new] = self.char
        map_mario[y_old][x_old] = " "

    def get_x(self):
        """gaurav"""
        return self.xarg

    def get_y(self):
        """gaurav"""
        return self.yawn

    def draw(self, map_mario, yawn, xarg):
        """gaurav"""
        map_mario[yawn][xarg] = self.char
