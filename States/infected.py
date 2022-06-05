"""
Infected state
"""
from confirmed import Confirmed
from state import State


class Infected(State):
    """
    Infected class
    """
    def __init__(self, human, data):
        """
        constructor
        @param human:
        @param data:
        """
        super().__init__(human, data)

        self.human.society.infected += 1

    def tick(self):
        """
        after a certain period of time
        an individual is considered to be confirmed by a doctor
        @return:
        """
        super().tick()

        if self.time >= self.data["T1"]:
            self.human.society.infected -= 1
            self.human.setState(Confirmed(self.human, self.data))
