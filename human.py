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
    def __init__(self, data):
        self.immunity_coeff = None
        self.age = self.get_normal_distribution_value() * 90
        self.gender = choice(['male', 'female'])
        self.setState(Susceptible(self, data))

        self.data = data

    def setState(self, state):
        self.current_state = state
        self.current_state.human = self

    def tick(self):
        self.current_state.tick()

    def get_normal_distribution_value(self):
        return random.choice(distribution)

    def immunity_coefficient(self):
        return math.sqrt(1 - (self.data['young'] if self.age < 60 else self.data['old']) *
                         (self.data['male'] if self.gender == 'male' else self.data[
                             'female']) * self.get_normal_distribution_value())
