import a from lab_4
import m from lab_4
f = int(input('Столбец 1 - '))
g = int(input('Столбец 2 - '))
for i in range(0, m, 1):
  h = a[i,f]
  a[i,f] = a[i,g]
  a[i,g] = h
print(a)

u = slice = a[::, f]
w = slice = a[::, g]
for i in range(0, m, 1):
  a[i,f] = u[i]
  a[i,g] = w[i]
print(a)