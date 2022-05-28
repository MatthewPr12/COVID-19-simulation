from state import State


class Dead(State):
    def __init__(self, human, data):
        super().__init__(human, data)

        self.human.society.dead += 1
