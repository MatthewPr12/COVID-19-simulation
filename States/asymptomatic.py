from state import State
# from recovered import Recovered


class Asymptomatic(State):
    def tick(self):
        super().tick()

        if self.time >= self.data["T1"] + self.data["T2"]:
            self.human.setState(Recovered(self.human, self.data))
