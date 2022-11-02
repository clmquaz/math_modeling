import numpy as np
y = int(input('Количество значений в строчке массива - '))
x = int(input('Количество строк массива - '))
a = np.zeros((x, y))
for i in range(0, x, 1):
  for c in range(0, y, 1):
    a[i,c] = int(input(f'введите значение ячейки с координатами: ячейка номер {c}, строка номер {i} -'))
b = np.zeros((x, y))
for i in range(0, x, 1):
  for c in range(0, y, 1):
    b[i,c] = int(input(f'введите значение ячейки с координатами: ячейка номер {c}, строка номер {i} -'))
d = np.zeros((x, y))
for i in range(0, x, 1):
  for c in range(0, y, 1):
    if a[i,c] >= b[i,c]:
      d[i,c] = a[i,c]
    else:
      d[i,c] = b[i,c]
print(a)
print(b)
print(d)