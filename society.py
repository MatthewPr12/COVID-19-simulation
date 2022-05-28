from math import sqrt
from random import uniform

from arrays import Array2D
from human import Human

data = dict()


class Society:
    EMPTY = None

    def __init__(self, num_rows, num_cols, coef_people):
        self.grid = Array2D(num_rows, num_cols)
        self.num_of_residents = self.add_people(coef_people)
        self.num_of_infected = 0
        self.num_of_recovered = 0
        self.num_of_dead = 0
        self.confirmed = 0
        self.yesterday_confirmed = 0

    def add_people(self, coef):
        counter = 0
        for i in range(self.grid.num_rows()):
            for j in range(self.grid.num_cols()):
                if uniform(0, 1) < coef:
                    counter += 1
                    self.grid[i, j] = Human(data)
                else:
                    self.grid[i, j] = Society.EMPTY
        return counter

    def get_neighbors(self, row, col):
        counter = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if self.is_human(i + row, j + col):
                        if i == 0 or j == 0:
                            counter += sqrt(2)
                        else:
                            counter += 1
                except AssertionError:
                    pass
        if self.is_human(row, col):
            counter -= 1
        return counter

    def count_q(self, before):
        q = 0.7 - 0.1 * (self.confirmed - before) / before / 0.025
        return q

    def is_human(self, row, col):
        return isinstance(self.grid[row, col], Human)

    def time_flow(self):
        # for i in range(100):

        # 1-second cycle

        # counting new

        # confirmed = count_confirmed()
        # self.yesterday_confirmed = self.confirmed
        # self.comfirmed = confimed()
        # q = self.count_q(self.yesterday_confirmed)
        pass

    def __str__(self):
        sstr = ''
        for i in range(self.grid.num_rows()):
            for j in range(self.grid.num_cols()):
                sstr += "1" if self.is_human(i, j) else "0"
            sstr += "\n" if i != self.grid.num_rows() - 1 else ""
        return sstr


soc = Society(10, 10, 0.5)
print(soc)

# 1100001000
# 1010001001
# 1110101111
# 0001010000
# 1001111111
# 1100010000
# 0101100001
# 1101111011
