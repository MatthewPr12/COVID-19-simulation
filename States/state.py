from abc import ABC


class State(ABC):
    def __init__(self, human, data):
        self.human = human
        self.data = data
        self.time = 0

    def tick(self):
        self.time += 1
