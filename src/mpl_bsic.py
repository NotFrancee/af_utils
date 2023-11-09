"""``mpl_bsic`` helps you style matplotlib plots in BSIC style.
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

    title = ax.get_title()

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
