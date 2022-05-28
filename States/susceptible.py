import random

from asymptomatic import Asymptomatic
from infected import Infected
from self_isolated import SelfIsolated
from state import State


class Susceptible(State):
    def __init__(self, human, data):
        super().__init__(human, data)

        self.p_a = 0.95 if human.age <= 4 else 0.8 if 5 <= human.age <= 14 else 0.7 if 15 <= human.age <= 29 else 0.5 if 30 <= human.age <= 59 else 0.4 if 60 <= human.age <= 69 else 0.3 if 70 <= human.age <= 79 else 0.2


    def tick(self):
        super().tick()

        if random.random() < self.data['q']:
            self.human.setState(SelfIsolated(self.human, self.data))
        elif random.random() < self.human.COEFF1:
            self.human.setState(Asymptomatic(self.human, self.data))
        elif random.random() < self.human.COEFF2:
            self.human.setState(Infected(self.human, self.data))

def get_random_age():
    rand = random.randint(0,)