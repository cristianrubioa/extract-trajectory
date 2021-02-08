#!/usr/bin/env python

import matplotlib.pyplot as plt
import numpy as np
import sys

trajectory = np.loadtxt(sys.argv[1])
plt.plot(trajectory[:, 1], trajectory[:, 3])
plt.show()
