import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots() 

edge = 25
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ball, = plt.plot([], [], '-', color='r', label='Ball')


def ball_move(t):
    T=np.arange(0, 4*np.pi, 0.1)
    x0 = 12*np.cos(T)+8*np.cos(1.5*T)
    y0 = 12*np.sin(T)-8*np.sin(1.5*T)

    x = x0*np.cos(t)-y0*np.sin(t)
    y = y0*np.cos(t)+x0*np.sin(t)
    return x, y

def update(i):
    ball.set_data(ball_move(t=i))

ani = FuncAnimation(fig, update, frames=np.arange(0, 4*np.pi, 0.1), interval=100)
ani.save('anim3.gif')