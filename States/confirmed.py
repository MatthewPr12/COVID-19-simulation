from random import random
from state import State
from hospitalized import Hospitalized
from recovered import Recovered

class Confirmed(State):
    def tick(self):
        super().tick()
        if self.time == self.data['T2']:
            if random() <= self.data['u']:
                self.human.setState(Hospitalized())
            else:
                self.human.setState(Recovered())