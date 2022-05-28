"""Human Class"""
import math
import random
from random import choice

from States.susceptible import Susceptible
from normal_distrubution import get_normal_distribution

distribution = get_normal_distribution()


class Human:
    def __init__(self, data):
        self.current_state = Susceptible(self, data)
        self.setState(self.current_state)
        self.immunity_coeff = self.immunity_coefficient()
        self.current_state.human = self
        self.age = self.get_normal_distribution_value() * 90
        self.gender = choice(['male', 'female'])

        self.data = data

    def setState(self, state):
        self.current_state = state
        self.current_state.human = self

    def tick(self):
        self.current_state.tick()

    def get_normal_distribution_value(self):
        return random.choice(distribution)

    def immunity_coefticient(self):
        return math.sqrt(1 - (self.data['young'] if self.age < 60 else self.data['old']) *
                         (self.data['male'] if self.gender == 'male' else self.data[
                             'female']) * self.get_normal_distribution_value())
