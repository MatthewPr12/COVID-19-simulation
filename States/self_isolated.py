from state import State

from susceptible import Susceptible


class SelfIsolated(State):
    def tick(self):
        if self.time >= self.data["T4"]:
            self.human.setState(Susceptible(self.human, self.data))
