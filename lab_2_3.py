import numpy as np
y = int(input('Количество значений в строчке массива - '))
x = int(input('Количество строк массива - '))
a = np.zeros((x, y))
s = 0
for i in range(0, x, 1):
  for c in range(0, y, 1):
    a[i,c] = int(input(f'введите значение ячейки с координатами: ячейка номер {c}, строка номер {i} -'))
for i in range(0, y, 1):
  s = a[0,i]
  for c in range(0, x-1, 1):
   if a[c,i] < a[c+1,i]:
     s = a[c+1,i]
   else:
     s = s
  print(f'Максимальный элемент столбца {i} = {s}')
print(a)