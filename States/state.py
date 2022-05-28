from abc import ABC
from random import random


class State(ABC):
    def __init__(self, human, data):
        self.human = human
        self.data = data
        self.time = 0

    def tick(self):
        self.time += 1


class Confirmed(State):
    def tick(self):
        super().tick()
        if self.time == self.data['T2']:
            if random() <= self.data['u']:
                self.human.setState(Hospitalized())
            else:
                self.human.setState(Recovered())


class Hospitalized(State):
    def tick(self):
        super().tick()
        if self.time == self.data['T3']:
            if random() <= self.data['k']:
                self.human.setState(Dead())
            else:
                self.human.setState(Recovered())


class Recovered(State):
    pass


class Dead(State):
    pass
