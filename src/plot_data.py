#!/usr/bin/env python

import sys
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation


def func(num, dataSet, line):
    """Animation function. """
    line.set_data(dataSet[0:2, :num])
    return line


def axes_plot(data, axes='xz'):
    """Choose axes to plot."""
    position = {'x': data[:, 1], 'y': data[:, 2], 'z': data[:, 3]}
    for key, value in position.items():
        if axes[0] == key:
            axe_ind = value
        if axes[1] == key:
            axe_dep = value
    return axe_ind, axe_dep


trajectory = np.loadtxt(sys.argv[1])  # Load trajectory

# Data points
ax1, ax2 = axes_plot(trajectory)
numDataPoints = len(trajectory)
dataSet = np.array([ax1, ax2])

# matplotlib objects
plt.plot(ax1, ax2)  # plot trajectory
fig = plt.figure()
ax = plt.axes()
line = plt.plot(dataSet[0], dataSet[1],
                lw=2, c='tab:red')[0]  # For line plot

# Animation object
line_ani = animation.FuncAnimation(
    fig, func, frames=numDataPoints, fargs=(dataSet, line), interval=1, blit=False)

plt.show()
