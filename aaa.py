import numpy as np
import array
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots() 
sq, = plt.plot([], [])

edge = 7
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


x0 = []
y0 = []

def move(t, a):
    x =[0, 0, a, a, 0]
    x0 = np.asarray (x)
    y = [0, a, a, 0, 0]
    y0 = np.asarray (y)
    print(x0)
    x = x0*np.cos(t)-y0*np.sin(t)
    print(x)
    y = y0*np.cos(t)+x0*np.sin(t)
    return x, y

def anim(i):
    sq.set_data(move(t=i, a=5))
    
ani = FuncAnimation(fig, anim, frames=np.arange(0, 4*np.pi, 0.1), interval=100)
ani.save('anim4.gif')