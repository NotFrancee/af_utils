import time
import functools
from typing import Callable, TypeVar, ParamSpec
import numpy as np

# match func.__annotations__["return"]:


class PerformanceMetrics:
    """TODO DOCSTRING"""

    def __init__(self, dt_arr) -> None:
        self.dt_arr = dt_arr

    def summary(self):
        """TODO DOCSTRING"""
        dt_arr = self.dt_arr
        print(f"Mean of running times: {dt_arr.mean()}")
        print(f"Stdev: {dt_arr.std()}")


def performance_test(iters: int = 1000):
    """Decorator to get the time performance of a function. Repeats the function `iters` times
    and then averages the results.

    Args:
        iters (int, optional): Number of iterations. Defaults to 1000.
    """

    dt_arr = np.zeros(iters)
    responses = np.zeros(iters)

    # R = TypeVar("R")
    # P = ParamSpec("P")

    # TODO: now assumes that the return type is an integer
    def time_test_decorator(func: Callable) -> Callable:
        # wrapper gets called when you call the function you are applying the decorator to
        # @functools.wraps(func)
        def wrapper():
            for i in range(iters):
                t0 = time.time()
                response = func()
                t1 = time.time()

                dt_arr[i] = t1 - t0
                responses[i] = response

            metrics = PerformanceMetrics(dt_arr)

            return responses, metrics

        return wrapper

    return time_test_decorator


@performance_test(1000)
def test() -> int:
    """test docstring"""
    return 999


res, m = test()

print(res)
metrics.summary()
