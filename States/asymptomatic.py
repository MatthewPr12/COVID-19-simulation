"""
asymptomatic state
"""
from States.recovered import Recovered
from States.state import State


class Asymptomatic(State):
    """
    Asymptomatic class
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
        after the certain period individual becomes Recovered from virus disease
        @return:
        """
        super().tick()

        if self.time >= self.data["T1"] + self.data["T2"]:
            self.human.setState(Recovered(self.human, self.data))
            self.human.society.infected -= 1
