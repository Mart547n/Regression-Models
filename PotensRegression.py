import numpy as np  

class potensRegressor: 

   def __init__(self, xs, ys):
      self.Xs = np.array(xs)
      self.Ys = np.array(ys)
      self.aHat, self.bHat = 0, 0
      self.fitData()
      print("f(x) = {0} * x^{1}".format(self.bHat, self.aHat))
   
   def fitData (self):
      """ Fits the paramitors to the data """
      # Fits aHat
      top = 0
      sumLogY = np.sum(np.log10(self.Ys) / len(self.Ys))
      sumLogX = np.sum(np.log10(self.Xs) / len(self.Xs))
      for x, y in zip (self.Xs, self.Ys):
         yPart = np.log10(y) - sumLogY
         #print(yPart)
         xPart = np.log10(x) - sumLogX
         #print(xPart)
         top += xPart * yPart
      bottom = 0 
      for x in self.Xs:
         bottom += np.power((np.log10(x) - sumLogX), 2)
      self.aHat = top / bottom
      # Fits bHat 
      logB = sumLogY - (self.aHat * sumLogX)
      self.bHat = np.power(10, logB)

   def f(self, x):
      """ Return bx^a """
      return self.bHat * np.power(x, self.aHat)

if (__name__ == "__main__"):
   Xs, Ys = [1, 2, 3, 4], [2, 8, 20, 40]
   model = potensRegressor(Xs, Ys)


 