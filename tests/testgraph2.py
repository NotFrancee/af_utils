import numpy as np
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from bsicplotter import BSICPlotter


x = np.linspace(0, 5, 100)
y = np.sin(x)

fig, ax = plt.subplots(1, 1)

ax.plot(x, y)
ax.set_title("Sin, cosin")
plotter = BSICPlotter()
plotter.apply_BSIC_style(fig, ax)

plt.show()
