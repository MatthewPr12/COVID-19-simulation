"""
Terminal Dead state
"""
from state import State


class Dead(State):
    """
    Dead class
    """
    def __init__(self, human, data):
        """
        constructor
        @param human:
        @param data:
        """
        super().__init__(human, data)

        self.human.society.dead += 1
