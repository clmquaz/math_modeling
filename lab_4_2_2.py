import numpy as np
def sss (n=10, t=0):
  l = np.ones((1,n-1))
  if t == 0:
    for i in range(2,n-1,1):
      l[0,i] = l[0,i-1]+l[0,i-2]
    print(l)
  else:
    for i in range(2,n-1,1):
        l[0,i] = l[0,i-2]-l[0,i-1]
    print(l)  
print(sss())
