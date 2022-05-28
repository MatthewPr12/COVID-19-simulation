"""Human Class"""
from numpy import random as np_random

class Sosiety:
    pass
class Human(Society):

    def __init__(self):
        super.__init__()
        self.current_state = Susceptible(self, Society.data)
        self.set_State(self.current_state)
        self.immunity_coeff = self.imunity_coeficient()
        self.curr_state.human = self
        self.age = np_random.normal(1)[0]
        self.gender = random.choice['male','female']

    def setState(self, state):
        self.curr_state = state
        self.curr_state.human = self

    def tick(self):
        self.current_state.tick()

    def get_age():
        np_random.normal(0,1) * 40


    def imunity_coeficient():
            return np_random.normal(0,1)  * (self.data['young'] if self.age < 60 else self.data['old']) *\
                  (self.data['male'] if self.gender = 'male' else self.data['female']) 









