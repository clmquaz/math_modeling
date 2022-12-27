import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

rt, = plt.plot([], [], '-', lw=2)
xdata, ydata = [], []

edge = 40
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def cicle(t):
    R=2
    xdata.append(R*(t-np.sin(t)))
    ydata.append(R*(1-np.cos(t)))
    rt.set_data(xdata, ydata)
    return rt

ani = FuncAnimation(fig, cicle, frames=np.arange(0, 8*np.pi, 0.1), interval=20) 

ani.save('lop.gif') 
