
import numpy as np
def ggg (*args, **kw):
  pass
  if kw['figure'] == 'circle':
    S = 2*args[0]*np.pi
    print(S)
  elif kw['figure'] == 'rectangle':
    S = args[0]*args[1]
    print(S)
  else:
    S = 1/2*args[0]*args[1] 
    print(S)
print(ggg(2, 3, figure='circle'))       