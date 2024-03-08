import pandas as pd 
import matplotlib.pyplot as plt
import scipy as sp
import numpy as np


df = pd.read_csv("suiciderates.csv");
theYear = df["Year"];
print(df.columns);

print(f"The median year is {np.median(theYear)}")