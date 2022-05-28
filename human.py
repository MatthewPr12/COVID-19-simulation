"""Human Class"""
import math
from random import choice

from numpy import random as np_random

from States.susceptible import Susceptible
from society import Society


class Human:
    def __init__(self, data):
        self.current_state = Susceptible(self, Society.data)
        self.setState(self.current_state)
        self.immunity_coeff = self.immunity_coefficient()
        self.curr_state.human = self
        self.age = self.get_age(self)
        self.gender = choice(['male', 'female'])

        self.data = data

    def setState(self, state):
        self.curr_state = state
        self.curr_state.human = self

    def tick(self):
        self.current_state.tick()

    def get_age(self):
        np_random.normal(0, 1) * 40

    def immunity_coefticient(self):
        return math.sqrt(1 - (self.data['young'] if self.age < 60 else self.data['old']) * \
                         (self.data['male'] if self.gender == 'male' else self.data['female']))
