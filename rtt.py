import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

rt, = plt.plot([], [], '-', lw=2)
xdata, ydata = [], []
ball, = plt.plot([], [], '-', color='r')

edge = 40
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def astr(R,t):
    xdata.append(R*np.cos(t)**3)
    ydata.append(R*np.sin(t)**3)
    return xdata, ydata


def circle_move(R,t):
    x0 = 16*np.cos(t)**3
    y0 = 16*np.sin(t)**3
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = y0+R*np.sin(alpha)
    return x, y


def animate(i):
    ball.set_data(circle_move(R=4, t=i))
    rt.set_data(astr(R=8, t=i))
    
ani = FuncAnimation(fig, animate, frames=np.arange(0, 2*np.pi, 0.1), interval=20) 

ani.save('lpopr.gif')