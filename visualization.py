import numpy as np
import matplotlib.pyplot as plt
#add graphics
class Human:

    def __init__(self, state):
        self.state = state
        
    def get_state(self):
        return self.state

# self.fig, self.ax=plt.subplots()
fig, ax = plt.subplots()

def show_day(array, day_number):
    GREY = (0.78, 0.78, 0.78)  # uninfected
    RED = (0.96, 0.15, 0.15)  # infected
    GREEN = (0, 0.86, 0.03)  # recovered
    BLACK = (0, 0, 0) #dead
    WHITE=(1., 1., 1.) #empty position
    colors=np.asarray([[get_human_color(human) if isinstance(human, Human) else WHITE for human in arr] for arr in array])
    ax.cla()
    ax.imshow(colors)
    ax.set_title("{}".format('Day '+str(day_number))) #add additional info
    plt.pause(3)

def get_human_color(human):
    states={'uninfected': (0.78, 0.78, 0.78), 'empty_pos': (1, 1, 1), 'self_isolated': (0.78, 0.78, 0.78),'infected': (0.96, 0.15, 0.15), 'confirmed':(0.96, 0.15, 0.15), 'recovered': (0, 0.86, 0.03), 'hospitalized': (0.96, 0.15, 0.15), 'dead': (0, 0, 0), 'asymptomatic': (0.96, 0.15, 0.15)}
    return states[human.get_state()]


if __name__=='__main__':
    grid=np.array([[None, Human('uninfected')], [Human('empty_pos'), Human('infected')]])
    show_day(grid, 1)
    grid=np.array([[None, Human('recovered')], [Human('confirmed'), Human('self_isolated')]])
    show_day(grid, 2)
