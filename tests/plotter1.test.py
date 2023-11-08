import sys
import os
import pandas as pd

sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../src")

from bsicplotter import BSICPlotter

plotter = BSICPlotter()

data = pd.read_csv("tests/data/usyieldsdata.csv")

print(data)
plotter.preprocess_dataframe(data)
print(data)
