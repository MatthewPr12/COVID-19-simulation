import matplotlib.pyplot as plt
import numpy as np

from human import Human


def display(array, day_number, ax):
    GREY = (0.78, 0.78, 0.78)  # uninfected
    RED = (0.96, 0.15, 0.15)  # infected
    GREEN = (0, 0.86, 0.03)  # recovered
    BLACK = (0, 0, 0)  # dead
    WHITE = (1., 1., 1.)  # empty position
    colors = np.asarray(
        [[get_human_color(human) if isinstance(human, Human) else WHITE for human in arr] for arr in
         array])
    ax.cla()
    ax.set_title("{}".format('Day ' + str(day_number)))  # add additional info
    ax.imshow(colors)
    plt.pause(0.6)


def get_human_color(human):
    GREY = (0.78, 0.78, 0.78)  # uninfected
    RED = (0.96, 0.15, 0.15)  # infected
    GREEN = (0, 0.86, 0.03)  # recovered
    BLACK = (0, 0, 0)  # dead
    WHITE = (1., 1., 1.)  # empty position
    states = {'Susceptible': GREY, 'SelfIsolated': (0.2, 0.78, 0.78),
              'Infected': RED, 'Confirmed': (0.96, 0.45, 0.45),
              'Recovered': GREEN, 'Hospitalized': (0.96, 0.8, 0.15), 'Dead': (0, 0, 0),
              'Asymptomatic': (0.96, 0.15, 0.15)}
    return states[str(human.getState().__class__.__name__)]
