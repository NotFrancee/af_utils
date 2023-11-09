from matplotlib.axes import Axes
import numpy as np
import sys
import os
import matplotlib.pyplot as plt

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")
from mpl_bsic import apply_BSIC_style

x = np.linspace(0, 5, 100)
y = np.sin(x)

fig, ax = plt.subplots(1, 1)
ax: Axes
apply_BSIC_style(fig, ax, "Sin(x)")

ax.plot(x, y)

plt.show()
