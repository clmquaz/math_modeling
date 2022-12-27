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

def cicle(R, t):
    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))
    plt.plot(x, y)
cicle(R=2, t=np.arange(0, 8*np.pi, 0.1))
 
def circle_move(R,y0 ,time):
    x0 = R*(time-np.sin(time)) 
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = x0 + R*np.cos(alpha)-2
    y = y0+R*np.sin(alpha)
    return x, y


def animate(i):
    ball.set_data(circle_move(R=2, y0=2 , time=i))
    	
ani = FuncAnimation(fig, animate, frames=np.arange(0, 8*np.pi, 0.1), interval=20)
 
ani.save('lpo.gif')