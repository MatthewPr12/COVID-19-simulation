import random

from self_isolated import SelfIsolated
from asymptomatic import Asymptomatic
from infected import Infected
from state import State


class Susceptible(State):
    def tick(self):
        super().tick()

        if random.random() < self.human.COEFF1:
            self.human.setState(SelfIsolated(self.human, self.data))
        elif random.random() < self.human.COEFF1:
            self.human.setState(Asymptomatic(self.human, self.data))
        elif random.random() < self.human.COEFF2:
            self.human.setState(Infected(self.human, self.data))
