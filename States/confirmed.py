"""
Confirmed state
"""
from random import random

from hospitalized import Hospitalized
from recovered import Recovered
from state import State


class Confirmed(State):
    """
    Confirmed class
    """
    def __init__(self, human, data):
        """
        constructor
        @param human:
        @param data:
        """
        super().__init__(human, data)
        self.human.society.confirmed += 1

    def tick(self):
        """
        after the certain period if condition
        consisting u coefficient is True - individual becomes Hospitalized
        otherwise, individual is considered Recovered
        @return:
        """
        super().tick()
        if self.time == self.data['T2']:
            if random() <= self.data['u']:
                self.human.setState(Hospitalized(self.human, self.data))
            else:
                self.human.setState(Recovered(self.human, self.data))
            self.human.society.confirmed -= 1
