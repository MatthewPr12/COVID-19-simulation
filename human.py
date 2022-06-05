"""
module which deals with Human class
"""
import sys

import math
import random
from random import choice
# import numpy as np

from States.susceptible import Susceptible
from normal_distrubution import get_normal_distribution

sys.path.append("States")
distribution = get_normal_distribution()


class Human:
    """
    Human class
    """
    def __init__(self, data, society, coords):
        """
        constructor
        @param data:
        @param society:
        @param coords:
        """
        self.data = data
        self.society = society
        self.coords = coords
        self.gender = choice(['male', 'female'])

        self.age = self.get_normal_distribution_value() * 90
        self.immunity_coeff = self.immunity_coefficient()
        self.setState(Susceptible(self, data))

    def setState(self, state):
        """
        State setter
        @param state:
        @return:
        """
        self.current_state = state
        self.current_state.human = self

    def getState(self):
        """
        State getter
        @return:
        """
        return self.current_state

    def tick(self):
        """
        move to next period of time
        @return:
        """
        self.current_state.tick()

    def get_normal_distribution_value(self):
        """
        normal distribution
        @return:
        """
        return random.choice(distribution)

    def immunity_coefficient(self):
        """
        count A(i, j) for each individual based on his/her age, gender
        @return:
        """
        return math.sqrt(1 - (self.data['young'] if self.age < 60 else self.data['old']) *
                         (self.data['male'] if self.gender == 'male' else self.data[
                             'female']) * self.get_normal_distribution_value())
        # a = np.random.uniform()
        # print(a)
        # return math.sqrt(1 - (self.data['young'] if self.age < 60 else self.data['old']) *
        #                  (self.data['male'] if self.gender == 'male' else self.data[
        #                      'female']) * a)
    #
    # def __repr__(self):
    #     return self.current_state.__class__.__name__[0]
