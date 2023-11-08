import matplotlib.pyplot as plt
from matplotlib.axes import Axes
from matplotlib.figure import Figure
from cycler import cycler
import pandas as pd
import numpy as np
import matplotlib.dates as mdates
from typing import Literal


# class MonthLocatorArgs(TypedDict):
#     bymonth: Optional[int]
#     bymonthday: Optional[int]  # defaults to 1
#     interval: int  # defaults to 1
#     tz: any


class BSICPlotter:
    """BSICPlotter is a class that provides a consistent style for graphs and plots."""

    title_style = {
        "fontname": "Gill Sans MT",
        "color": "black",
        "fontweight": "bold",
        "fontstyle": "italic",
        "fontsize": 12,
    }
    color_cycle = cycler(color=["#38329A", "#8EC6FF", "#601E66", "#2F2984", "#0E0B54"])

    general_font_size = 10
    general_font_family = "Garamond"

    def __init__(self) -> None:  # TODO let the user override the default styles
        plt.rcParams["font.sans-serif"] = self.general_font_family
        plt.rcParams["font.size"] = self.general_font_size
        plt.rcParams["axes.prop_cycle"] = self.color_cycle

    def _check_figsize(
        self, width: float, height: float | None, aspect_ratio: float | None
    ):
        """
        Checks the validity of the figsize parameters and returns the width and height to use.

        :param width: width
        :type width: float
        :param height: height
        :type height: float
        :param aspect_ratio: aspect ratio
        :type aspect_ratio: float
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

    def preprocess_dataframe(self, df: pd.DataFrame):
        """
        Preprocesses the dataframe by (i) converting all column names to lowercase and (ii) setting the index to date if it exists, and converting it to datetime.

        :param df: the dataframe to preprocess
        :type df: pd.DataFrame
        """

        df.columns = [col.lower() for col in df.columns]

        if "date" in df.columns:
            df.set_index("date", inplace=True, drop=True)
            df.index = pd.to_datetime(df.index)

    # 7.32in is the width of a word article
    def plot(
        self,
        data: pd.DataFrame,
        width: float = 7.32,
        height: float | None = None,
        aspect_ratio: float | None = None,
        title: str = "",
        y_label: str = "",
        x_label: str = "",
        constant_time_distance: bool = False,
        zero_line: bool = False,
        timeseries_ticks_unit: Literal["Y", "M", "D"] | None = None,
        timeseries_ticks_frequency: int = 1,
        timeseries_date_format: str | None = None,
        legend: bool = False,
        legend_labels: list[str] | None = None,
        filename: str | None = None,
        *args,
        **kwargs,
    ):
        width, height = self._check_figsize(width, height, aspect_ratio)

        fig, ax = plt.subplots(1, 1)
        ax: Axes

        fig.set_size_inches(width, height)
        ax.set_xlabel(x_label)
        ax.set_ylabel(y_label)
        ax.set_title(title, **self.title_style)

        if zero_line:
            ax.axhline(y=0, color="black", linestyle="-", linewidth=1)
        if constant_time_distance:
            data = data.copy()
            data.index = data.index.astype(str)
        if timeseries_ticks_unit:
            match timeseries_ticks_unit:
                case "Y":
                    ax.xaxis.set_major_locator(
                        mdates.YearLocator(timeseries_ticks_frequency)
                    )
                case "M":
                    ax.xaxis.set_major_locator(
                        mdates.MonthLocator(interval=timeseries_ticks_frequency)
                    )
                case "D":
                    ax.xaxis.set_major_locator(
                        mdates.DayLocator(timeseries_ticks_frequency)
                    )
                case _:
                    raise Exception("this time frequency is not supported.")

            date_format = timeseries_date_format if timeseries_date_format else "%b-%y"
            ax.xaxis.set_major_formatter(mdates.DateFormatter(date_format))
            # fig.autofmt_xdate(rotation=45, ha="center")
            ax.tick_params(axis="x", rotation=45)

        lines = ax.plot(data, *args, **kwargs)

        if legend:
            if not legend_labels:
                print(
                    "You did not specify legend labels. Using column names as legend labels"
                )
                legend_labels = list(data.columns)
            ax.legend(lines, legend_labels)

        if filename is None:
            fig.tight_layout()  # changes font sizes so should not use when saving, only when displaying
        else:
            # using bbox_inches = tight changes the size of the figure exported
            fig.savefig(filename, dpi=1200, bbox_inches="tight")
            # fig.savefig(
            #     filename,
            #     dpi=1200,
            # )

        return fig, ax
