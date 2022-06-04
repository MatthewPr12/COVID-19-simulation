import matplotlib.pyplot as plt
import numpy as np

from human import Human


def display(array, day_number, ax1, ax2, infected, recovered, dead, inf, rec, de):
    GREY = (0.78, 0.78, 0.78)  # uninfected
    RED = (0.96, 0.15, 0.15)  # infected
    GREEN = (0, 0.86, 0.03)  # recovered
    BLACK = (0, 0, 0)  # dead
    WHITE = (1., 1., 1.)  # empty position
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
    plt.pause(0.1)


def get_human_color(human):
    GREY = (0.78, 0.78, 0.78)  # uninfected
    RED = (0.96, 0.15, 0.15)  # infected
    GREEN = (0, 0.86, 0.03)  # recovered
    BLACK = (0, 0, 0)  # dead
    WHITE = (1., 1., 1.)  # empty position
    states = {'Susceptible': GREY, 'SelfIsolated': (0.2, 0.78, 0.78),
              'Infected': RED, 'Confirmed': (0.96, 0.45, 0.45),
              'Recovered': GREEN, 'Hospitalized': (0.96, 0.8, 0.15), 'Dead': BLACK,
              'Asymptomatic': (0.96, 0.15, 0.15)}
    return states[str(human.getState().__class__.__name__)]
