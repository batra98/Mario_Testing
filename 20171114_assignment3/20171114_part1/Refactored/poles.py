"""gaurav"""
class Poles(object):
    """gaurav"""
    def __init__(self, map_mario):
        self.map_mario = map_mario
        self.poles = ['###', '###', '###', '###']
        self.temp = 1

    def draw(self, xarg, yawn):
        """gaurav"""
        for j in range(0, len(self.poles)):
            for i in range(0, len(self.poles[j])):
                self.map_mario[yawn-j][xarg+i] = self.poles[j][i]

    def tempfunction(self):
        """gaurav"""
        self.temp = 0
