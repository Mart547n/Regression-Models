import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score as r2
from linearRegressor import *
from PotensRegression import *

d = pd.read_csv("ArbejdsData.csv", sep=";")

# Load data 
time = d.loc[:, 'Kvartal efter 2010'].values
ledighedsData = d.loc[:, 'Ledige'].values

model = linearRegressor(time, ledighedsData)
print(r2)

# Gennerate data with the model
data = []
for t in time:
   data.append(model.f(t))

print("R2: {0}".format(r2(ledighedsData, data)))
plt.style.use("ggplot")

# PLot the no work data
plt.plot(time, ledighedsData, color = 'green', label = 'Datapunkter')
#plt.plot(time, model.f(time), ls = "--", color = 'black', label = 'Tendens linje')
plt.title("Arbejdsløshed over tid (siden 2010)")
plt.xlabel("Kvartal siden 2010")
plt.ylabel("Arbejdsløshed i tusind")
plt.legend(loc="best")
plt.show()

model = potensRegressor(time, ledighedsData)

# Gennerate data with the model
data = []
for t in time:
   data.append(model.f(t))

print("R2: {0}".format(r2(ledighedsData, data)))
plt.style.use("ggplot")

# PLot the no work data
plt.scatter(time, ledighedsData, color = 'green', label = 'Datapunkter')
plt.plot(time, model.f(time), ls = "--", color = 'black', label = 'Tendens linje')
plt.title("Arbejdsløshed over tid (siden 2010)")
plt.xlabel("Kvartal siden 2010")
plt.ylabel("Arbejdsløshed i tusind")
plt.legend(loc="best")
plt.show()