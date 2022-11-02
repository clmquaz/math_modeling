import numpy as np
a = np.zeros((1, 5))
for i in range(0, 4, 1):
  a[0, i] = input(f'Укажите значение элемента {i} - ')
print(a)
b = int(input('Какое число дабавить - '))
c = int(input('Укажите позицию значения - '))
for i in range(4, c, -1):
  a[0,i] = a[0,i-1]
a[0,c] = b
print(a)