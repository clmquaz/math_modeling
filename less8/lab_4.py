import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

rr, = plt.plot([], [], '-', lw=2)
xdata, ydata = [], []

x0 = 0.1
y0 = 0.1
C = 0.3
D = 0.33

for i in range(30):
    xdata.append(x0)
    ydata.append(y0)

    x1 = x0**2-y0+C
    y1 = 2*x0*y0+D

    x0 = x1
    y0 = y1
    


edge = 1
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def animate(i):
    rr.set_data(xdata[:i], ydata[:i])

anim = FuncAnimation(fig, animate, frames=30, interval=100) 

anim.save('lrr.gif')