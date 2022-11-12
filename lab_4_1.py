import numpy as np

s = int(input('jj'))
a = np.zeros((1,s))

for i in range(0,s,1):
  d = int(input('i = '))
  a[0,i] = d
  
def middle(d):
    l = np.zeros((1,s))
  c = 0
  for i in range(0,d.size ,1):
    h = c+d[0,i]
    z = h/d.size
    l[0,i]=z
    c = h
  j = l[0,d.size-1]
  print(f'среднее арифметическое {d} равно {j}')

print(middle(a))  