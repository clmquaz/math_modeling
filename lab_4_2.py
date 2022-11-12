import numpy as np

q = int(input('num'))
a = np.zeros((1,q))

for i in range(0,q,1):
  d = int(input('i = '))
  a[0,i] = d
  
def middle(d):
  l = np.zeros((1,q))
  c = 1
  for i in range(0, d.size, 1):
    h = c*d[0,i]
    l[0,i]=h
    c = h
  j = l[0,d.size-1]
  print(f'произведение {d} равно {j}')
print(middle(a))