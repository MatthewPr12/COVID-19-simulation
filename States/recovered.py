from state import State


class Recovered(State):
    def __init__(self, human, data):
        super().__init__(human, data)

        self.human.society.recovered += 1
