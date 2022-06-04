"""Human Class"""
import sys

sys.path.append("States")

import math
import random
from random import choice

from States.susceptible import Susceptible
from normal_distrubution import get_normal_distribution

distribution = get_normal_distribution()


class Human:
    def __init__(self, data, society, coords):
        self.data = data
        self.society = society
        self.coords = coords
        self.gender = choice(['male', 'female'])

        self.age = self.get_normal_distribution_value() * 90
        self.immunity_coeff = self.immunity_coefficient()
        self.setState(Susceptible(self, data))

    def setState(self, state):
        self.current_state = state
        self.current_state.human = self

    def getState(self):
        return self.current_state

    def tick(self):
        self.current_state.tick()

    def get_normal_distribution_value(self):
        return random.choice(distribution)

    def immunity_coefficient(self):
        return math.sqrt(1 - (self.data['young'] if self.age < 60 else self.data['old']) *
                         (self.data['male'] if self.gender == 'male' else self.data[
                             'female']) * self.get_normal_distribution_value())
    #
    # def __repr__(self):
    #     return self.current_state.__class__.__name__[0]
