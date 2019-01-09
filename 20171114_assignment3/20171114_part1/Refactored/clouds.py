"""gaurav"""
class Clouds(object):
    """gaurav"""
    def __init__(self, map_mario):
        self.cloud = ["()()()", "..()()()()...."]
        self.map_mario = map_mario
        self.temp = 1

    def draw(self, yawn, xarg):
        """gaurav"""
        for j in range(0, len(self.cloud[0])):
            try:
                self.map_mario[yawn][xarg+j] = self.cloud[0][j]
            except Exception:
                pass
        for j in range(0, len(self.cloud[1])):
            try:
                self.map_mario[yawn+1][xarg-3+j] = self.cloud[1][j]
            except Exception:
                pass

    def update(self, new, yawn, xarg):
        """"gaurav"""
        self.temp = new
        self.draw(yawn, xarg)
