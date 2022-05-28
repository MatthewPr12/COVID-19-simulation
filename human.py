"""Human Class"""
from numpy import random as np_random
from random import choice
import math

import scipy.stats


N = 10000


scipy.stats.truncnorm.rvs((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma,)) * 90

class Sosiety:
    pass
class Human(Society):

    def __init__(self):
        super.__init__()
        self.current_state = Susceptible(self, Society.data)
        self.set_State(self.current_state)
        self.immunity_coeff = self.immunity_coefficient()
        self.curr_state.human = self
        self.age = self.get_age(self)
        self.gender = choice(['male','female'])

    def setState(self, state):
        self.curr_state = state
        self.curr_state.human = self

    def tick(self):
        self.current_state.tick()

    def get_age():
        lower = 0
        upper = 1
        mu = 0.5
        sigma = 0.2
        scipy.stats.truncnorm.rvs((lower - mu) / sigma, (upper - mu) / sigma, loc=mu, scale=sigma,)) * 90


    def immunity_coefticient(self):
            return math.sqrt(1- (self.data['young'] if self.age < 60 else self.data['old']) *\
                  (self.data['male'] if self.gender == 'male' else self.data['female']))




