"""``mpl_bsic`` helps you style matplotlib plots in BSIC style.

Guidelines
------------------
.. rubric:: Plotting Yield Curves

When plotting yield curves, to make the x ticks the same distance regardless of time:

.. code:: python

    data.index = data.index.astype(str)

.. rubric:: Saving the figure

When saving the figure, you should use ``bbox_inches='tight'`` to make sure the figure is not cropped.

.. code:: python

    fig, ax = plt.subplots(1,1)

    ... # plot your data and apply the style

    fig.savefig("your_filename.svg", dpi=1200, bbox_inches="tight")

Module Components
-----------------
"""

import matplotlib.pyplot as plt
from matplotlib.figure import Figure
from matplotlib.axes import Axes
from cycler import cycler
import pandas as pd
from typing import Literal
import matplotlib.dates as mdates

DEFAULT_TITLE_STYLE = {
    "fontname": "Gill Sans MT",
    "color": "black",
    "fontweight": "bold",
    "fontstyle": "italic",
    "fontsize": 12,
}
"""Default Title Style. Used in ``apply_BSIC_style``.

Details: 

* ``fontname``: ``Gill Sans MT``
* ``color``: ``black``
* ``fontweight``: ``bold``
* ``fontstyle``: ``italic``
* ``fontsize``: ``12``

See Also 
--------
mpl_bsic.apply_BSIC_style : The function that applies the style to the plot.
mpl_bsic.DEFAULT_COLOR_CYCLE : The default color cycler that gets applied to the plot.
mpl_bsic.DEFAULT_FONT_SIZE : The default font size that gets applied to the plot.

Examples
--------
This is the examples section. WIP.
"""

DEFAULT_COLOR_CYCLE = cycler(
    color=["#38329A", "#8EC6FF", "#601E66", "#2F2984", "#0E0B54"]
)
"""Default Color Style.

Cycle: 

* ``#38329A`` 
* ``#8EC6FF`` 
* ``#601E66`` 
* ``#2F2984`` 
* ``#0E0B54``

See Also 
--------
mpl_bsic.apply_BSIC_style : The function that applies the style to the plot.
mpl_bsic.DEFAULT_TITLE_STYLE : The default title style that gets applied to the plot.
mpl_bsic.DEFAULT_FONT_SIZE : The default font size that gets applied to the plot.

Examples
--------
This is the examples section. WIP.
"""

DEFAULT_FONT_SIZE = 10
"""Default Font Size for the plot (text, labels, ticks).

The default font size used for the plots is 10.

See Also 
--------
mpl_bsic.apply_BSIC_style : The function that applies the style to the plot.
mpl_bsic.DEFAULT_TITLE_STYLE : The default title style that gets applied to the plot.
mpl_bsic.DEFAULT_COLOR_CYCLE : The default color cycler that gets applied to the plot.

Examples
--------
This is the examples section. WIP.
"""

BSIC_FONT_FAMILY = "Garamond"
"""Default Font Family for the plot (text, labels, ticks).

The default font family used for the plots is ``Garamond``.

See Also 
--------
mpl_bsic.apply_BSIC_style : The function that applies the style to the plot.
mpl_bsic.DEFAULT_TITLE_STYLE : The default title style that gets applied to the plot.
mpl_bsic.DEFAULT_FONT_SIZE : The default font size that gets applied to the plot.

Examples
--------
This is the examples section. WIP.
"""


def preprocess_dataframe(df: pd.DataFrame):
    """Handle and preprocess the DataFrame before plotting.

    Handle and preprocess the DataFrame before plotting. It sets all the columns to lowercase and sets the index as the dates (converting to datetime).

    Parameters
    ----------
    df : pd.DataFrame
        The DataFrame to preprocess.

    See Also
    --------
    mpl_bsic.apply_BSIC_style : The function that applies the style to the plot.

    Examples
    --------
    This is the examples section. WIP.
    """

    df.columns = [col.lower() for col in df.columns]

    if "date" in df.columns:
        df.set_index("date", inplace=True, drop=True)
        df.index = pd.to_datetime(df.index)


def apply_BSIC_style(fig: Figure, ax: Axes, title: str | None = None):
    r"""Apply the BSIC Style to an existing matplotlib plot.

    Apply the BSIC Style to the plot. First, it sets the font family and size for the overall plot and the color cycle to use.
    Then, if the plot has a title, then it applies the default title style.

    Should be called *before* plotting, to make sure the right color cycle gets applied.

    Warning: if you want to specify and set a title to the plot, you can either set it before or give it to the function.
    Otherwise, the correct style won't be applied. This is forced by matplotlib and must be done to make sure the fuction works.

    Parameters
    ----------
    fig : matplotlib.figure.Figure
        Matplotlib Figure instance.
    ax : matplotlib.axes.Axes
        Matplotlib Axes instance.
    title : str | None
        Title of the plot. If None, it will try to get the title from the Axes instance.

    See Also
    --------
    mpl_bsic.DEFAULT_TITLE_STYLE : The default title style that gets applied to the plot.
    mpl_bsic.DEFAULT_COLOR_CYCLE : The default color cycler that gets applied to the plot.
    mpl_bsic.DEFAULT_FONT_SIZE : The default font size that gets applied to the plot.

    Examples
    --------
    .. plot::

        from mpl_bsic import apply_BSIC_style

        x = np.linspace(0, 5, 100)
        y = np.sin(x)

        fig, ax = plt.subplots(1, 1)
        apply_BSIC_style(fig, ax, 'Sin(x)') # apply right after creating the Figure and Axes instances

        ax.plot(x,y)

    .. plot::

        from mpl_bsic import apply_BSIC_style

        x = np.linspace(0, 5, 100)
        y = np.cos(x)

        fig, ax = plt.subplots(1, 1)
        # ax.set_title('Cos(x)') # set the title before applying the style
        apply_BSIC_style(fig, ax) # the function will re-set the title with the correct style

        ax.plot(x,y)
    """
    plt.rcParams["font.sans-serif"] = BSIC_FONT_FAMILY
    plt.rcParams["font.size"] = DEFAULT_FONT_SIZE
    plt.rcParams["axes.prop_cycle"] = DEFAULT_COLOR_CYCLE
    ax.set_prop_cycle(DEFAULT_COLOR_CYCLE)

    if title is None:
        title = ax.get_title()
        if title == "":
            print("warning: you did not specify a title")

    ax.set_title(title, **DEFAULT_TITLE_STYLE)


def check_figsize(
    width: float, height: float | None, aspect_ratio: float | None
) -> tuple[float, float]:
    r"""Check the validity of the figsize.

    Checks the validity of the figsize parameters and returns the width and height to use.

    Parameters
    ----------
    width : float
        Width of the Figure, in inches.
    height : float | None
        Height of the Figure, in inches.
    aspect_ratio : float | None
        Aspect Ratio of the figure, as a float. E.g. 16/9 for 16:9 aspect ratio.

    Returns
    -------
    tuple[float, float]
        The width and height to use for the Figure.

    See Also
    --------
    mpl_bsic.apply_BSIC_style : The function that applies the style to the plot.
    mpl_bsic.preprocess_dataframe : The function that preprocesses the DataFrame before plotting.

    Examples
    --------
    This is the examples section. WIP.
    """
    if width > 7.32:
        print("--- Warning ---")
        print(
            """Width is greater than 7.32 inches. 
This is the width of a word document available for figures. 
If you set the width > 7.32, the figure will be resized in word and the font sizes will not be consistent across the article and the graph"""
        )

    if width is None:
        print(
            "you did not specify width. Defaulting to 7.32 inches (width of a word document))"
        )

    if height is None:
        if aspect_ratio is None:
            raise Exception("You must specify either height or aspect_ratio")

        height = width * aspect_ratio

    return width, height


def format_timeseries_axis(
    ax: Axes, time_unit: Literal["Y", "M", "D"], freq: int, fmt: str | None
):
    """Format the x-axis of a timeseries plot.

    It sets the major locator and formatter for the x-axis.
    Note that this function does not take as an input the figure, but just the matplotlib Axes instance.

    Parameters
    ----------
    ax : matplotlib.axes.Axes
        Matplotlib Axes instance.
    time_unit : Literal['Y', 'M', 'D']
        Time unit to use. Can be "Y" for years, "M" for months, or "D" for days.
    freq : int
        Time Frequency. For example, if time_unit is "M" and freq is 3, then the x-axis will have a tick every 3 months.
    fmt : str | None
        Date Format which will be fed to matplotlib.dates.DateFormatter. If None, the default format will be used (`%b-%y`).

    Raises
    ------
    Exception
        If the time frequency is not supported.

    See Also
    --------
    mpl_bsic.apply_BSIC_style : The function that applies the style to the plot.

    Examples
    --------
    Examples will come soon.
    """

    match time_unit:
        case "Y":
            ax.xaxis.set_major_locator(mdates.YearLocator(freq))
        case "M":
            ax.xaxis.set_major_locator(mdates.MonthLocator(interval=freq))
        case "D":
            ax.xaxis.set_major_locator(mdates.DayLocator(freq))
        case _:
            raise Exception("this time frequency is not supported.")

    date_format = fmt if fmt else "%b-%y"
    ax.xaxis.set_major_formatter(mdates.DateFormatter(date_format))
    ax.tick_params(axis="x", rotation=45)
