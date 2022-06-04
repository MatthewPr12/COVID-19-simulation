from state import State


class SelfIsolated(State):
    def tick(self):
        if self.time >= self.data["T4"]:
            from susceptible import Susceptible
            self.human.setState(Susceptible(self.human, self.data))
