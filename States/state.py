"""
State design patter base module
"""
from abc import ABC


class State(ABC):
    """
    State parent class
    """
    def __init__(self, human, data):
        """
        constructor
        @param human:
        @param data:
        """
        self.human = human
        self.data = data
        self.time = 0

    def tick(self):
        """
        clock function
        @return:
        """
        self.time += 1
