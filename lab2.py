import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')


def circle_move(R):
    T = np.linspace(1, 100, 100)
    al = np.linspace(0, 2*np.pi, 100)
    for t in T:
        x = R*np.cos(al)*t
        y = R*np.sin(al)*t
    return x, y


def animate(i):
    ball.set_data(circle_move(R=1))


edge = 150
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
    
ani = FuncAnimation(fig, animate, frames=100, interval=30)

ani.save('a2.gif') 
