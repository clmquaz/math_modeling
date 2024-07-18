import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation



def circle_move(aa, R):
    t = np.linspace(0, 10, 100)
    al = np.linspace(0, 2*np.pi, 100)
    x = R*np.cos(al)*aa*t
    y = R*np.sin(al)*aa*t
    return x, y


def animate(i):
    ball.set_data(circle_move(R=0.5))
 
 
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], 'o', color='r', label='Ball')
 
edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
    
ani = FuncAnimation(fig, animate, frames=100, interval=30)
 
ani.save('a.gif') 