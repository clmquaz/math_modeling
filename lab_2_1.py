import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

rt, = plt.plot([], [], '-', lw=2)
xdata, ydata = [], []
ball, = plt.plot([], [], '-', color='r')

edge = 50
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def cicle(t):
    R=2
    xdata.append(R*(t-np.sin(t)))
    ydata.append(R*(1-np.cos(t)))
    return xdata, ydata


 
def circle_move(R,vx0 ,time):
    x0 = vx0 * time
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)
    y = R + R*np.sin(alpha)
    return x, y


def animate(i):
    ball.set_data(circle_move(R=2, vx0=2 , time=i))
    rt.set_data(cicle(t=i))
    
ani = FuncAnimation(fig, animate, frames=np.arange(0, 8*np.pi, 0.1), interval=20) 

ani.save('lpop.gif')


