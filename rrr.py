import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

rt, = plt.plot([], [], '-', lw=2)
ball, = plt.plot([], [], '-', color='r')

edge = 5
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def cicle(R, t):
    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))
    plt.plot(x, y)
cicle(R=2, t=np.arange(0, 2*np.pi, 0.1))
 
def circle_move(R, alpha):
    x =  R*np.cos(alpha)
    y = R*np.sin(alpha)
    return x, y

def animatet(i):
    ball.set_data(circle_move(R=20, alpha=i))
    	
ani = FuncAnimation(fig, animatet, frames=np.arange(0, 4*np.pi, 0.1), interval=200)
 
ani.save('lro.gif')