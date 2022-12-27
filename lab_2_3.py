import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
star, = plt.plot([], [], '-', color='r')

edge = 40
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def star_move(t):
    alpha = np.arange(-25, 25, 0.1)
    x = 12*np.cos(alpha)+8*np.cos(1.5*alpha)
    y = 12*np.sin(alpha)-8*np.sin(1.5*alpha)
    
    X = x*np.cos(t)+y*np.sin(t)
    Y = y*np.cos(t)-x*np.sin(t)
    return X, Y

def animate(i):
    star.set_data(star_move(t=i))
    
ani = FuncAnimation(fig, animate, frames=np.arange(0, 4*np.pi, 0.1), interval=20) 

ani.save('lpoop.gif')