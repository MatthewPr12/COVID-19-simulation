"""
Recovered State
"""
from States.state import State


class Recovered(State):
    """
    Recovered class
    """
    def __init__(self, human, data):
        """
        constructor
        @param human:
        @param data:
        """
        super().__init__(human, data)

        self.human.society.recovered += 1

    def tick(self):
        """
        after a certain period of time
        an individual becomes vulnerable again
        which means that s/he is susceptible
        @return:
        """
        super().tick()

        if self.time >= self.data["T5"]:
            from susceptible import Susceptible
            self.human.setState(Susceptible(self.human, self.data))
            self.human.society.recovered -= 1
