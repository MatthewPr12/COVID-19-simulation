from random import random

from dead import Dead
from recovered import Recovered
from state import State


class Hospitalized(State):
    def __init__(self, human, data):
        super().__init__(human, data)

        self.human.society.infected += 1

    def tick(self):
        super().tick()
        if self.time == self.data['T3']:
            if random() <= self.data['k']:
                self.human.setState(Dead(self.human, self.data))
                self.human.society.infected -= 1
            else:
                self.human.setState(Recovered(self.human, self.data))
                self.human.society.infected -= 1
