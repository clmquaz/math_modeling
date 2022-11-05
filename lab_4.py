import numpy as np

import math
n = int(input('Количество значений в строчке массива - '))
m = int(input('Количество строк массива - '))
a = np.zeros((m, n))
s = int(input('Если вычисления производить при индексации с единицы напишите 1; если при индексации с нуля, напишите 0 - '))
if s == 1:
  for i in range(m-1, 0, -1):
    for j in range(n-1, 0, -1):
      a[i,j] = math.sin(n*i+m*j)
      if a[i,j]<0:
        a[i,j] = 0
else:
  for i in range(0, m, 1):
    for j in range(0, n, 1):
      a[i, j] = math.sin(n*(i+1)+m*(j + 1))
      if a[i, j]<0:
        a[i, j] = 0
print(a)