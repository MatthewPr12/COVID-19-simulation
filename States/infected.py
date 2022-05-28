from confirmed import Confirmed
from state import State


class Infected(State):
    def tick(self):
        super().tick()

        if self.time >= self.data["T1"]:
            self.human.setState(Confirmed(self.human, self.data))
