from state import State
from random import random
from dead import Dead
from recovered import Recovered


class Hospitalized(State):
    def tick(self):
        super().tick()
        if self.time == self.data['T3']:
            if random() <= self.data['k']:
                self.human.setState(Dead())
            else:
                self.human.setState(Recovered())