"""
SelfIsolated state
"""
from state import State


class SelfIsolated(State):
    """SelfIsolated class"""
    def tick(self):
        """
        after a certain period of time
        individual neglects isolation
        and becomes vulnerable and susceptible
        @return:
        """
        super().tick()

        if self.time >= self.data["T4"]:
            from susceptible import Susceptible
            self.human.setState(Susceptible(self.human, self.data))
