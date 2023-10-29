import time
from typing import Callable, TypeVar, ParamSpec, Literal
import numpy as np

# TODO implement memory usage

type TimeUnit = Literal['millis', 's']

class PerformanceMetrics:
    """Class to process time data into performance metrics and display them to the user"""

    def __init__(
        self, dt_arr: np.ndarray[float, float], time_unit: TimeUnit = None
    ) -> None:
        if time_unit == "millis":
            dt_arr *= 1000

        self.dt_arr = dt_arr

    def summary(self):

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

        def wrapper():
            for i in range(iters):
                t0 = time.time()
                response = func()
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
            return responses, metrics

        return wrapper

    return time_test_decorator


@performance_test(1000, "millis")
def test():
    """test docstring"""
    return (np.random.rand(100000) * 5).sum()


# res, m = test()
# m.summary()
