"""Summary for the performance_tester module. This module contains a decorator to test the performance of a function. The decorator runs the function for a set number of times (given by iters), then collects the results in a PerformanceMetrics class which is returned to the user."""

import time
from typing import Callable, TypeVar, ParamSpec, Literal
import numpy as np
import numpy.typing as npt

# TODO implement memory usage


"""Type for Time Unit. Can be either "millis", "ms" or "s" """
type TimeUnit = Literal["millis", "ms", "s"]


class PerformanceMetrics:
    """Class to store and display the performance metrics of a function. The metrics calculated are: mean, stdev, min, max, quantiles (10th and 90th)"""

    def __init__(
        self, dt_arr: npt.NDArray[np.float_], time_unit: TimeUnit = "s"
    ) -> None:
        if time_unit in ["millis", "ms"]:
            dt_arr *= 1000

        self.dt_arr = dt_arr
        self.time_unit = time_unit

        self.mean = dt_arr.mean()
        self.stdev = dt_arr.std()

        self.min_time = dt_arr.min()
        self.max_time = dt_arr.max()
        self.quantiles = np.quantile(dt_arr, [0.1, 0.9])

    def summary(self):
        """
        Prints the summary of the performances
        """

        text = "\n".join(
            [
                f"Performance Summary ({self.time_unit})",
                f"Mean of running times: {self.mean}",
                f"Stdev: {self.stdev}",
                f"Min - Max Time: {self.min_time} - {self.max_time}",
                f"Quantiles (10th - 90th): {self.quantiles}",
            ]
        )

        print(text)


def performance_test(iters: int = 1000, time_unit: TimeUnit = "ms"):
    """
    Performance Test Decorator. Put before functions to test their performance.
    The decorator runs the function for a set number of times (given by iters),
    then collects the results in a PerformanceMetrics class which is returned to the user.

    How to use: you have to actually call this function, because it returns the actual decorator.


    Parameters
    ----------
    iters : int, optional
        Number of iterations, by default 1000
    time_unit : TimeUnit, optional
        Time unit to use in the ``PerformanceMetrics`` instance, by default "ms"

    Returns
    -------
    decorator
        The decorator that will then be applied to the function

    Raises
    ------
    Exception
        If the return type is not supported (as of now, only ``int`` and ``float`` are supported)
    """

    dt_arr = np.zeros(iters)
    responses = np.zeros(iters)

    R = TypeVar("R")
    P = ParamSpec("P")

    # TODO: now assumes that the return type is an integer
    def time_test_decorator(
        func: Callable[P, R]
    ) -> Callable[P, tuple[R, PerformanceMetrics]]:
        def wrapper(*args: P.args, **kwargs: P.kwargs):
            for i in range(iters):
                t0 = time.time()
                response = func(*args, **kwargs)
                t1 = time.time()

                dt_arr[i] = t1 - t0

                match response:
                    case int() | float():
                        responses[i] = response
                    case _:
                        raise Exception(
                            "This type is not supported yet. The currently supported types are ints and floats"
                        )

                responses[i] = response

            metrics = PerformanceMetrics(dt_arr, time_unit)
            return responses[0], metrics

        return wrapper

    return time_test_decorator


@performance_test(1000, "millis")
def test():
    """test docstring"""
    return (np.random.rand(100000) * 5).sum()


# res, m = test()
# m.summary()
