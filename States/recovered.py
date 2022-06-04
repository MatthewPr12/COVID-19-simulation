from state import State


class Recovered(State):
    def __init__(self, human, data):
        super().__init__(human, data)

        self.human.society.recovered += 1

    def tick(self):
        super().tick()

        if self.time >= self.data["T5"]:
            from susceptible import Susceptible
            self.human.setState(Susceptible(self.human, self.data))
            self.human.society.recovered -= 1
