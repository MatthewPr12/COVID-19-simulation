from abc import ABC
from random import random


class State(ABC):
    def __init__(self, data):
        self.data = data
        self.time = 0

    def tick(self):
        self.time += 1


class Confirmed(State):
    def tick(self):
        self.time += 1
        if self.time == self.data['T2']:
            if random() <= self.data['u']:
                self.
