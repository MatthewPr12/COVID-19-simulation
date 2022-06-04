import matplotlib.pyplot as plt
import numpy as np

from human import Human


def display(array, day_number, ax1, ax2, infected, recovered, dead, inf, rec, de):
    WHITE = (1, 1, 1)  # empty position
    colors = np.asarray(
        [[get_human_color(human) if isinstance(human, Human) else WHITE for human in arr] for arr in
         array])
    ax1.cla()
    ax1.set_title("{}".format('Day ' + str(day_number)))
    ax1.imshow(colors)
    t = np.arange(0, len(infected), 1)
    ax2.plot()
    ax2.plot(t, infected, color='red')
    ax2.plot(t, recovered, color='green')
    ax2.plot(t, dead, color='black')
    ax2.legend(['infected = ' + str(inf), 'recovered = ' + str(rec), 'dead = ' + str(de)],
               loc='upper left')
    ax2.set_xlabel('Day ' + str(day_number))
    ax2.set_ylabel('Number of people')
    plt.pause(0.01)


def get_human_color(human):
    GREY = (220,220,220)  # susceptible
    RED = (255,0,0)  # infected
    GREEN = (124,252,0)  # recovered
    BLACK = (0, 0, 0)  # dead
    WHITE = (1, 1, 1)  # empty position
    BLUE = (240, 248, 255) #self isolated
    YELLOW = (234, 221, 202) #asymptomatic
    ORANGE = (255, 140, 0) #hospitalized
    PURPLE = (230, 230, 250) #confirmed
    states = {'Susceptible': GREY, 'SelfIsolated': BLUE,
              'Infected': RED, 'Confirmed': PURPLE,
              'Recovered': GREEN, 'Hospitalized': ORANGE, 'Dead': BLACK,
              'Asymptomatic': YELLOW}
    return states[str(human.getState().__class__.__name__)]
