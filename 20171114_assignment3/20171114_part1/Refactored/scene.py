"""gaurav"""
import color


class Mario_map:
    """gaurav"""
    def __init__(self, height, width):
        self.height = height
        self.width = width
        self.map_mario = []
        self.boundary = [0, width, width*2, width*3, width*4, width*5]
        self.start_x = 0

    def initialize(self):
        """gaurav"""
        temp = []
        temp_2 = []
        for i in range(0, self.height-1):
            for j in range(0, self.width*8):
                j = j
                if i == 0:
                    temp.append("*")
                elif i >= self.height-3:
                    temp.append("#")
                else:
                    temp.append(" ")

            self.map_mario.append(temp)
            temp = []

        for i in range(0, self.width*8):
            temp_2.append("*")
        self.map_mario.append(temp_2)

    def print_map(self, max_x, max_y, start_x):
        """gaurav"""
        self.start_x = start_x
        try:
            if max_y >= self.height and max_x >= self.width:
                for gaurav in range(0, max_y):
                    print(color.getcolor("*"), end="")
                    for helper in range(start_x, max_x):
                        print(color.getcolor(self.map_mario[gaurav][helper]), end="")
                    print(color.getcolor("*"))
            else:
                self.print_map(self.width, self.height, 0)
        except Exception:
            print(Exception)
            self.print_map(self.width, self.height, 0)
        print('\x1b[1;37;40m')

    def make_wall(self, keeper, apple, ball, char, index):
        """gaurav"""
        for i in range(self.boundary[index]+apple, self.boundary[index]+ball):
            self.map_mario[keeper][i] = char

    def shift_up(self, xarg, yawn):
        """gaurav"""
        self.map_mario[xarg][yawn] = " "
        if self.map_mario[xarg-2][yawn] == "@":
            self.map_mario[xarg-3][yawn] = "@"
        elif self.map_mario[xarg-2][yawn] == "$":
            self.map_mario[xarg-3][yawn] = "$"
        self.map_mario[xarg-2][yawn] = "#"

    def shift_down(self, xarg, yawn):
        """gaurav"""
        self.map_mario[xarg][yawn] = " "
        if self.map_mario[xarg-1][yawn] == "@":
            self.map_mario[xarg-1][yawn] = " "
            self.map_mario[xarg][yawn] = "@"
        self.map_mario[xarg+2][yawn] = "#"

    def end_game(self, width, height, score, distance):
        """gaurav"""
        image_game_over = \
        ["  ___   _   __  __ ___    _____   _____ ___ ", \
        " / __| /_\\ |  \\/  | __|  / _ \\ \\ / / __| _ \\", \
        "| (_ |/ _ \\| |\\/| | _|  | (_) \\ V /| _||   /", \
        " \\___/_/ \\_\\_|  |_|___|  \\___/ \\_/ |___|_|_\\", \
        "Press 'r' Key to Restart or 'q' to Quit"]
        final_score = ["Final Score: "+str(score)+" Distance= "+str(distance)]
        coor_x = max(int(height-20), int(self.height/4))
        coor_y = max(int(width-20), int(self.width/4))

        for i in range(0, 4):
            for j in range(0, len(image_game_over[i])):
                self.map_mario[coor_x+i][coor_y+j] = image_game_over[i][j]

        for j in range(0, len(final_score)):
            self.map_mario[coor_x+5][coor_y+j] = final_score[j]

        for j in range(0, len(image_game_over[4])):
            self.map_mario[coor_x+7][coor_y+j] = image_game_over[4][j]

    def smash_enemy(self, xarg, yawn):
        """gaurav"""
        self.map_mario[yawn+1][xarg] = "."

    def shift_up_big(self, xarg, yawn):
        """gaurav"""
        self.map_mario[xarg][yawn] = " "

    def shift_down_big(self, xarg, yawn):
        """gaurav"""
        self.map_mario[xarg][yawn] = " "
