from cProfile import label
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from sklearn import linear_model
from sklearn import datasets
from sklearn.preprocessing import StandardScaler
from sklearn.cluster import KMeans
scale = StandardScaler()


df = pd.read_csv("death.csv")
print(df.head)
print(df.columns)

year = df["Year"]
country = df["Code"]
age = df["Age-standardized suicide rate - Sex: both sexes"]\

print(f"The countries are {country}")


HighestYear = np.percentile(year, 75)
print(f"{HighestYear} was 75%")

scaledX = scale.fit_transform(year)


plt.plot(year, age, c=label)
plt.xlabel("age")
plt.ylabel("year")
plt.title("Deaths!")
plt.show()
