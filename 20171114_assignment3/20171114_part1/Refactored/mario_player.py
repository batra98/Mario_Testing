"""gaurav"""
import person


class Mario(person.Person):
    """gaurav"""
    def __init__(self, xarg, yawn):
        person.Person.__init__(self, xarg, yawn)
        self.bullet = "-"

    def update_pos(self, map_mario, x_new, y_new):
        """gaurav"""
        previous = map_mario[x_new][y_new]
        map_mario[x_new][y_new] = self.char
        map_mario[self.xarg][self.yawn] = previous
        if previous == 'e' or previous == "#" \
            or previous == "@" or previous == "$"or previous == "-":
            map_mario[self.xarg][self.yawn] = " "
        self.xarg = x_new
        self.yawn = y_new
