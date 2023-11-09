"""Lorem ipsum dolor sit amet
"""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from cycler import cycler

DEFAULT_TITLE_STYLE = {
    "fontname": "Gill Sans MT",
    "color": "black",
    "fontweight": "bold",
    "fontstyle": "italic",
    "fontsize": 12,
}
"""TODO"""

DEFAULT_COLOR_CYCLE = cycler(
    color=["#38329A", "#8EC6FF", "#601E66", "#2F2984", "#0E0B54"]
)

DEFAULT_FONT_SIZE = 10
BSIC_FONT_FAMILY = "Garamond"
"""TODO"""


def apply_BSIC_style(fig: Figure, ax: Axes):
    """
    Apply the BSIC Style to the plot. Sets the title style to the correct format.

    Parameters
    ----------
    fig : ``matplotlib.figure.Figure``
        Matplotlib Figure instance.
    ax : ``matplotlib.axes.Axes``
        Matplotlib Axes instance.
    """
    plt.rcParams["font.sans-serif"] = BSIC_FONT_FAMILY
    plt.rcParams["font.size"] = DFT_FONT_SIZE
    plt.rcParams["axes.prop_cycle"] = DFT_COLOR_CYCLE

    title = ax.get_title()

    ax.set_title(title, **DFT_TITLE_STYLE)
