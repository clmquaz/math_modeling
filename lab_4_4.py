import numpy as np
def yyy (a=0, b=4, N=3):
  y = np.zeros((1, N))
  x = np.linspace(a+1,b-1,N)
  for i in range (0,b-1,1):
    y[0,i] = x[i]**2
  print(y)  
print(yyy())