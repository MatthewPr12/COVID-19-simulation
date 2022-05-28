import random

from state import State


class Uninfected(State):
    def tick(self):
        super().tick()

        if random.random() < self.data["q"]:
            pass
            
