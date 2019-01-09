"""gaurav"""
class Flag(object):
    """gaurav"""
    def __init__(self, map_mario):
        self.map_mario = map_mario
        self.flag = ["  ++-----", "  ++-----", "  ++-----", "  ++     ", "  ++     ",
                     "  ++     ", "  ++     ", "  ++     ", "  ++     ", "  ++     ", "++++++   "]

    def draw(self, i, yawn, xarg):
        """gaurav"""
        sleep = list(self.flag[i])
        for j in range(4, 9):
            sleep[j] = " "
        for j in range(0, 9):
            self.map_mario[yawn+i][xarg+j] = sleep[j]

        sleep = list(self.flag[i+3])
        for j in range(4, 9):
            sleep[j] = "-"
        for j in range(0, 9):
            self.map_mario[yawn+i+3][xarg+j] = sleep[j]

    def draw_2(self, yawn, xarg):
        """gaurav"""
        for i in range(0, len(self.flag)):
            sleep = list(self.flag[i])
            for j in range(0, 9):
                self.map_mario[yawn+i][xarg+j] = sleep[j]
