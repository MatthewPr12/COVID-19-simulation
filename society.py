"""
module for controlling the whole system a.k.a society
"""
import random
import sys

import matplotlib.pyplot as plt
import numpy as np

from visualization import display

from States.infected import Infected
from human import Human
sys.path.insert(0, "States")


class Society:
    """
    Society class
    """
    EMPTY = None

    def __init__(self, num_rows, num_cols, coef_people, data):
        """
        constructor
        @param num_rows:
        @param num_cols:
        @param coef_people:
        @param data:
        """
        self.data = data

        self.infected_array = []
        self.recovered_array = []
        self.dead_array = []

        self.infected = 0
        self.recovered = 0
        self.dead = 0
        self.confirmed = 0
        self.yesterday_confirmed = 0

        self.grid = np.array([[None] * num_cols for _ in range(num_rows)])
        self.residents = self.add_people(coef_people, num_rows, num_cols)

        fig = plt.figure(figsize=(14, 7))
        self.ax1 = fig.add_subplot(121)
        self.ax2 = fig.add_subplot(122)

        self.main()

    def num_rows(self):
        """
        return height of the system
        @return:
        """
        return len(self.grid)

    def num_cols(self):
        """
        return width of the system
        @return:
        """
        return len(self.grid[0])

    def add_people(self, coef, rows, cols):
        """
        fill the grid with people
        @param coef:
        @param rows:
        @param cols:
        @return:
        """
        counter = 0
        for i in range(rows):
            for j in range(cols):
                if random.random() < coef:
                    counter += 1
                    the_human = Human(self.data, self, (i, j))
                    if random.random() < self.data["init_infected"]:
                        the_human.setState(Infected(the_human, self.data))
                    self.grid[i, j] = the_human
                else:
                    self.grid[i, j] = Society.EMPTY
        return counter

    def get_neighbors(self, coord):
        """
        get eight neighbors of a specific cell(Human)
        @param coord:
        @return:
        """
        list1, list2 = [], []
        for (i, j) in {(-1, -1), (-1, 0), (0, -1), (1, 0), (0, 1), (1, 1), (-1, 1), (1, -1)}:
            if 0 <= i + coord[0] < self.grid.shape[0] and \
                    0 <= j + coord[1] < self.grid.shape[1]:
                if self.is_ill(i + coord[0], j + coord[1]):
                    if i == 0 or j == 0:
                        list1.append(self.grid[i + coord[0], j + coord[1]])
                    else:
                        list2.append(self.grid[i + coord[0], j + coord[1]])
        return list1, list2

    def count_q(self, yesterday):
        """
        count q coefficient which is common for everyone
        @param yesterday:
        @return:
        """
        return -0.3 - (yesterday - self.confirmed) / (self.residents or 0.001) * 600

    def is_ill(self, row, col):
        """
        check whether human in a specific cell is Infected or Confirmed or Asymptomatic
        @param row:
        @param col:
        @return:
        """
        return isinstance(self.grid[row, col], Human) and \
               str(self.grid[row, col].current_state.__class__.__name__) in {'Infected',
                                                                             'Confirmed',
                                                                             'Asymptomatic'}

    def is_human(self, row, col):
        """
        check whether cell is not empty
        @param row:
        @param col:
        @return:
        """
        return isinstance(self.grid[row, col], Human)

    def main(self):
        """
        basically main wrapper
        @return:
        """
        self.yesterday_confirmed = 3
        for day in range(365):
            # if day < 20:
            #     self.data['q'] = 0
            # else:
            self.data["q"] = self.count_q(self.yesterday_confirmed)
            self.yesterday_confirmed = self.confirmed

            for i in range(self.grid.shape[0]):
                for j in range(self.grid.shape[1]):
                    if self.grid[i, j]:
                        self.grid[i, j].tick()

            self.infected_array.append(self.infected)
            self.recovered_array.append(self.recovered)
            self.dead_array.append(self.dead)

            display(self.grid, day, self.ax1, self.ax2, self.infected_array, self.recovered_array,
                    self.dead_array, self.infected, self.recovered, self.dead)
