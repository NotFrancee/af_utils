import time
from typing import Callable, TypeVar, ParamSpec, Literal
import numpy as np
import numpy.typing as npt

# TODO implement memory usage

type TimeUnit = Literal['millis', 's']

class PerformanceMetrics:
    """Class to process time data into performance metrics and display them to the user"""

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


def performance_test(iters: int = 1000, time_unit: TimeUnit=None):
    """Decorator to get the time performance of a function. Repeats the function `iters` times
    and then averages the results.

    Args:
        iters (int, optional): Number of iterations. Defaults to 1000.
        time_unit (TimeUnit, optional): time unit in which to calculate the metrics. Choices: millis
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
