import numpy as np 

class linearRegressor:

   def __init__ (self, Xs, Ys):
      """ Initalise the regressor """
      self.Xs = Xs
      self.Ys = Ys

      self.means = [self.calcMean(Xs), self.calcMean(Ys)]

      self.a = self.CalcAhat()
      self.b = self.CalcBhat()

      print("f(x) = {0}x + {1}".format(self.a, self.b))

   def f(self, x):
      """ Interface for using the model """
      return (self.a * x + self.b)

   def calcMean (self, data):
      """ Returns the mean of a dataset """
      total = 0
      for n in data:
         total += n
      print(len(data))
      return (total / len(data))

   def CalcAhat (self):
      """ Calculate the slope of the regression line """
      top = 0
      for x, y in zip(self.Xs, self.Ys):
         # Calculate the top portion of the division
         top += (y - self.means[1]) * (x - self.means[0])
      print("Top: {0}".format(top))
      bottom = 0
      for x in self.Xs:
         # Calculate the bottom portion of the division 
         bottom += np.power((x - self.means[0]), 2)
      print("Bottom: {0}".format(bottom))
      return (top / bottom)
   
   def CalcBhat (self):
      """ Calculate the interception of the line """
      return (self.means[1] - (self.a * self.means[0]))
