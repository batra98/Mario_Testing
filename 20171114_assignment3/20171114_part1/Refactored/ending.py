"""gaurav"""
class End():
    """gaurav"""
    def __init__(self, map_mario):
        self.map_mario = map_mario
        self.stair_right = ["##       ", "####     ", "####     ",
                            "######   ", "######   ", "#########", "#########"]
        self.stair_left = ["       ##", "     ####", "     ####",
                           "   ######", "   ######", "#########", "#########"]
        self.castle = []

    def draw_left(self, xarg, yawn, height, width):
        """gaurav"""
        self.castle.append(height)
        self.castle.append(width)
        for i in range(0, 9):
            for j in range(0, len(self.stair_left)):
                self.map_mario[yawn+j][xarg+i] = self.stair_left[j][i]

    def draw_right(self, xarg, yawn, height, width):
        """gaurav"""
        self.castle.append(height)
        self.castle.append(width)
        for i in range(0, 9):
            for j in range(0, len(self.stair_right)):
                self.map_mario[yawn+j][xarg+i] = self.stair_right[j][i]
