import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
s, = plt.plot([], [], '-', color='r')

edge = 40
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

def s_move(t, a):
    x = 
    y = 
    
    X = x*np.cos(t)+y*np.sin(t)
    Y = y*np.cos(t)-x*np.sin(t)
    return X, Y

def animate(i):
    s.set_data(s_move(t=i, a=2))
    
ani = FuncAnimation(fig, animate, frames=np.arange(0, 4*np.pi, 0.1), interval=20) 

ani.save('loopr.gif')