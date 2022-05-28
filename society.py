import random
import sys

import numpy as np

sys.path.insert(0, "States")

from States.infected import Infected
from States.asymptomatic import Asymptomatic
from States.confirmed import Confirmed
from human import Human


class Society:
    EMPTY = None

    def __init__(self, num_rows, num_cols, coef_people):
        self.grid = np.array([[None] * num_cols for i in range(num_rows)])
        self.num_of_residents = self.add_people(coef_people, \
                                                num_rows, num_cols)
        self.num_of_infected = 0
        self.num_of_recovered = 0
        self.num_of_dead = 0
        self.confirmed = 0
        self.yesterday_confirmed = 0

    def num_rows(self):
        return len(self.grid)

    def num_cols(self):
        return len(self.grid[0])

    def add_people(self, coef, rows, cols):
        counter = 0
        for i in range(rows):
            for j in range(cols):
                if random.random() < coef:
                    counter += 1
                    h = Human(data, self, (rows, cols))
                    if random.random() < 0.3:
                        h.setState(Infected(h, data))
                    self.grid[i, j] = h
                else:
                    self.grid[i, j] = Society.EMPTY
        return counter

    def get_neighbors(self, row, col):
        list1, list2 = [], []
        for i in range(-1, 2):
            for j in range(-1, 2):
                try:
                    if i == j == 0:
                        continue
                    elif self.is_normal_human(i + row, j + col):
                        if i == 0 or j == 0:
                            list1.append((i + row, j + col))
                        else:
                            list2.append((i + row, j + col))
                except AssertionError:
                    pass
        return list1, list2

    def count_q(self, yesterday):
        q = 0.7 - 0.1 * (self.confirmed - yesterday) / yesterday / 0.025
        return q

    def is_normal_human(self, row, col):
        if isinstance(self.grid[row, col], Human) and \
                (isinstance(self.grid[row, col].current_state, Infected) or
                 isinstance(self.grid[row, col].current_state, Asymptomatic) or
                 isinstance(self.grid[row, col].current_state, Confirmed)):
            return True
        return False

    def is_human(self, row, col):
        if isinstance(self.grid[row, col], Human):
            return True
        return False

    def main(self):
        for _ in range(100):
            data["q"] = self.count_q(self.yesterday_confirmed)

            for i in range(self.grid.size()[0]):
                for j in range(self.grid.size()[1]):
                    self.grid[i, j].tick()

            self.yesterday_confirmed = self.confirmed

    def __str__(self):
        sstr = ''
        for i in range(self.num_rows()):
            for j in range(self.num_cols()):
                sstr += "1" if (self.is_human(i, j)) else "0"
            sstr += "\n" if i != self.num_rows() - 1 else ""
        return sstr


data = dict()
data["young"] = 1
data["old"] = 0.75
data["female"] = 1
data["male"] = 0.8

soc = Society(20, 40, 0.97)
print(soc)
