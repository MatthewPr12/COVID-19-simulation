from confirmed import Confirmed
from state import State


class Infected(State):
    def __init__(self, human, data):
        super().__init__(human, data)

        self.human.society.num_of_infected += 1

    def tick(self):
        super().tick()

        if self.time >= self.data["T1"]:
            self.human.society.num_of_infected -= 1
            self.human.setState(Confirmed(self.human, self.data))
