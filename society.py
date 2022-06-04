import random
import sys

import matplotlib.pyplot as plt
import numpy as np

from visualization import display

sys.path.insert(0, "States")

from States.infected import Infected
from States.asymptomatic import Asymptomatic
from States.confirmed import Confirmed
from human import Human
from States.recovered import Recovered


class Society:
    EMPTY = None

    def __init__(self, num_rows, num_cols, coef_people):
        self.infected = 0
        self.recovered = 0
        self.dead = 0
        self.confirmed = 0
        self.yesterday_confirmed = 0

        self.grid = np.array([[None] * num_cols for i in range(num_rows)])
        self.residents = self.add_people(coef_people, num_rows, num_cols)

        self.fig, self.ax = plt.subplots()

        self.main()

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
                    h = Human(data, self, (i, j))
                    # if random.random() < 0.1:
                    if (i == 10 and j == 10) or (i == 90 and j == 90) or (i == 10 and j == 90):
                        h.setState(Infected(h, data))
                    self.grid[i, j] = h
                else:
                    self.grid[i, j] = Society.EMPTY
        return counter

    def get_neighbors(self, coord):
        list1, list2 = [], []
        for i in range(-1, 2):
            for j in range(-1, 2):
                if 0 <= i + coord[0] < self.grid.shape[0] and \
                        0 <= j + coord[1] < self.grid.shape[1]:
                    if i == j == 0:
                        continue
                    elif self.is_ill(i + coord[0], j + coord[1]):
                        if i == 0 or j == 0:
                            list1.append(self.grid[i + coord[0], j + coord[1]])
                        else:
                            list2.append(self.grid[i + coord[0], j + coord[1]])
        return list1, list2

    def count_q(self, yesterday):
        q = 0.7 - 0.1 * (self.confirmed - yesterday) / (yesterday or 0.001) / 0.025
        return q

    def is_ill(self, row, col):
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
        for day in range(365):
            data["q"] = 0

            for i in range(self.grid.shape[0]):
                for j in range(self.grid.shape[1]):
                    if self.grid[i, j]:
                        self.grid[i, j].tick()

            self.yesterday_confirmed = self.confirmed
            display(self.grid, day, self.ax)

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

data["T1"] = 10
data["T2"] = 4
data["T3"] = 4

data["u"] = 0.2
data["k"] = 0.33

soc = Society(100, 100, 0.9)
