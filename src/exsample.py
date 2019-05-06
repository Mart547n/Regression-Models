from src.linearRegressor import *
from matplotlib import pyplot as plt

Xs = [1.2, 2, 2.8, 4.1]
Ys = [2.1, 4.1, 6, 8.4]

model = linearRegressor(Xs, Ys)

# Plot the stuff
plt.scatter(Xs, Ys, c = "green", label = "Data")

modelYs = []

for x in Xs:
   modelYs.append(model.f(x))

plt.plot(Xs, modelYs, c = 'black', ls = '--', label = 'Regression')

plt.title("Eksempel")
plt.ylabel("Y værdi")
plt.xlabel("X værdi")
plt.legend(loc='best')
plt.show()