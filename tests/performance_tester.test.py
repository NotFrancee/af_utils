import sys
import os
import pandas as pd
import numpy as np

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from performance_tester import performance_test


@performance_test(1000, "millis")
def test():
    """test docstring"""
    return (np.random.rand(100000) * 5).sum()


test()
