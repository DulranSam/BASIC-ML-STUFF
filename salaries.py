import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import scipy as sp
import statsmodels.formula.api as smf

df = pd.read_csv("salary.csv")
df.dropna(axis=0, inplace=True)
print(df.columns)

x = df["experience_level"]
y = df["salary"]


model = smf.ols("salary ~ experience_level", data=df)
results = model.fit()
print(results.summary())

plt.plot(x, y, "o")
plt.xlabel("Experience")
plt.ylabel("Salary")
plt.title("DS Salaries")
plt.show()
