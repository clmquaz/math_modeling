import numpy as np
import lab1 as l


x0 = int(input('x0 '))
vx0 = int(input('vx0 '))
y0 = int(input('y0 '))
vy0 = int(input('vy0 '))

b = np.zeros((6, 3))

for t in range(0, 6, 1):
    b[t, 0] = t
    x = x0 + vx0*t
    b[t, 1] = x
    y = y0 + vy0*t - l.g*t**2/2
    b[t, 2] = y

print(b)

