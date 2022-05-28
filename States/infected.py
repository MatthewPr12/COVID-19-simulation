from state import State
from confirmed import Confirmed

class Infected(State):
    def tick(self):
        super().tick()

        if self.time >= self.data["T1"]:
            self.human.setState(Confirmed(self.human, self.data))
