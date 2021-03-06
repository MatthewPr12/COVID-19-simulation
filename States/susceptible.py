"""
Susceptible state
"""
import random
from math import sqrt

from States.asymptomatic import Asymptomatic
from States.infected import Infected
from States.self_isolated import SelfIsolated
from States.state import State


class Susceptible(State):
    """
    Susceptible class
    """

    def __init__(self, human, data):
        """
        constructor
        @param human:
        @param data:
        """
        super().__init__(human, data)

        self.p_a = 0.95 if human.age <= 4 else 0.8 if 5 <= human.age <= 14 else 0.7 \
            if 15 <= human.age <= 29 else 0.5 if 30 <= human.age <= 59 else 0.4 \
            if 60 <= human.age <= 69 else 0.3 if 70 <= human.age <= 79 else 0.2

    def tick(self):
        """
        if q-condition is True individual becomes self-isolated
        if p*p_a condition is True individual becomes infected but
        asymptomatically
        if p*(1-p_a) condition is True individual becomes Infected
        @return:
        """
        super().tick()

        p = self.calculate_p()
        if random.random() < self.data['q']:
            self.human.setState(SelfIsolated(self.human, self.data))
        elif random.random() < p * self.p_a:
            self.human.setState(Asymptomatic(self.human, self.data))
        elif random.random() < p * (1 - self.p_a):
            self.human.setState(Infected(self.human, self.data))

    def calculate_p(self):
        """
        p coefficient calculator
        @return:
        """
        straight, diag = self.human.society.get_neighbors(self.human.coords)
        p = 0

        for nb in straight:
            p += (1 / 8) * nb.immunity_coefficient()

        for nb in diag:
            p += (1 / (8 * sqrt(2))) * nb.immunity_coefficient()
        return p
