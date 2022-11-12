import numpy as np

def ttt (a=0,b=0,c=0):
  print('После нужной фигуры напишите - 1, в противном случае поставьте 0.')
  a = int(input('Круг'))
  b = int(input('Прямоугольник'))
  c = int(input('Треугольник'))
  if a==1 and b == 0 and c ==0:
      r = int(input('r = '))
      S = 2*r*np.pi
      print(f'Площадь круга равна {S}')
  if a==0 and b == 1 and c ==0:    
      a = int(input('a = '))
      b = int(input('b = '))
      S = a*b
      print(f'Площадь прямоугольника равна {S}')
  if a==0 and b == 0 and c ==1:
      a = int(input('a = '))
      h = int(input('h = '))
      S = (1/2)*a*h
      print(f'Площадь треугольника равна {S}')
print(ttt())
  