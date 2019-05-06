import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from linearRegressor import *

d = pd.read_csv("ArbejdsData.csv", sep=";")

# Load data 
time = d.loc[:, 'Kvartal efter 2010'].values
ledighedsData = d.loc[:, 'Ledige'].values

model = linearRegressor(time, ledighedsData)

plt.style.use("ggplot")

# PLot the no work data
plt.scatter(time, ledighedsData, color = 'green', label = 'Datapunkter')
plt.plot(time, model.f(time), ls = "--", color = 'black', label = 'Tendens linje')
plt.title("Arbejdsløshed over tid (siden 2010)")
plt.xlabel("Kvartal siden 2010")
plt.ylabel("Arbejdsløshed i tusind")
plt.legend(loc="best")
plt.show()