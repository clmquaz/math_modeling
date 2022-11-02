

import numpy as np
x0 = 0
y0 = 0
g = 10
v = 15
alpha = 30
vx0=v*np.sin(np.pl/180*alpha)
vy0=v*np.cos(np.pl/180*alpha)

t = np.arrange(0, 5, 0.01)
x = x0+vx0*t
y = y0+vy0*t-g*t**2/2

coords_time = np.zeros((len(t),3))
for l in range(len(t)):
               coords_time[l, 0]=t[l]
               coords_time[l, 1]=x[l]
               coords_time[l, 2]=y[l]
print( coords_time)

