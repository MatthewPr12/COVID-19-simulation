from abc import ABC


class State(ABC):
    def __init__(self, data):
        self.data = data
        self.time = 0

    def tick(self):
        self.time += 1
