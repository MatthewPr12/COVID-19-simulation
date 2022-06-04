import random
import sys

import matplotlib.pyplot as plt
import numpy as np

from visualization import display

sys.path.insert(0, "States")

from States.infected import Infected
from States.confirmed import Confirmed
from States.asymptomatic import Asymptomatic
from human import Human


class Society:
    EMPTY = None

    def __init__(self, num_rows, num_cols, coef_people, data):
        self.data = data

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
                    h = Human(self.data, self, (i, j))
                    if random.random() < self.data['init_infected']:
                        h.setState(Infected(h, self.data))
                    self.grid[i, j] = h
                else:
                    self.grid[i, j] = Society.EMPTY
        return counter

    def get_neighbors(self, coord):

        list1, list2 = [], []
        for (i,j) in {(-1,-1), (-1, 0), (0,-1), (1,0), (0,1), (1,1), (-1, 1), (1, -1)}:
            if 0 <= i + coord[0] < self.grid.shape[0] and \
                    0 <= j + coord[1] < self.grid.shape[1]:
                if self.is_ill(i + coord[0], j + coord[1]):
                    if i == 0 or j == 0:
                        list1.append(self.grid[i + coord[0], j + coord[1]])
                    else:
                        list2.append(self.grid[i + coord[0], j + coord[1]])
        return list1, list2

    def count_q(self, yesterday):
        q = 0.7 - 0.1 * (self.confirmed - yesterday) / (yesterday or 0.001) / 0.025
        return q

    def is_ill(self, row, col):
        return isinstance(self.grid[row, col], Human) and\
                str(self.grid[row, col].current_state.__class__.__name__) in  {'Infected', 'Confirmed', 'Asymptomatic'}


    def is_human(self, row, col):
        return isinstance(self.grid[row, col], Human)

    def main(self):
        for day in range(100):
            self.data["q"] = 0

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
