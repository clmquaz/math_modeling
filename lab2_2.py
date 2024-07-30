import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots() 
 
line1, = plt.plot([], [], '-', lw=2)
ball1, = plt.plot([], [], '-', color='r', label='Ball')

line2, = plt.plot([], [], '-', lw=2)
ball2, = plt.plot([], [], '-', color='r', label='Ball')
 
xdata1, ydata1 = [], [] 
xdata2, ydata2 = [], [] 

edge = 26
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)


def circle_move1(t, A, f):
    R = 1
    x0 = t
    y0 = A*np.sin(f*t)
    alpha = np.arange(0, 2*np.pi, 0.1)
    R = 0.1
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y

def line_move1(t, A, f):
    xdata1.append(t)
    ydata1.append(A*np.sin(f*t))
    return xdata1, ydata1


def circle_move2(t, A, f):
    R = 1
    x0 = t
    y0 = A*np.sin(f*t)
    alpha = np.arange(0, 2*np.pi, 0.1)
    R = 0.1
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y

def line_move2(t, A, f):
    xdata2.append(t)
    ydata2.append(A*np.sin(f*t))
    return xdata2, ydata2


def update(i):
    print(i)
    line1.set_data(line_move1(t=i, A=2, f=1)) 
    ball1.set_data(circle_move1(t=i, A=2, f=1))
    line2.set_data(line_move2(t=i, A=3, f=0.5)) 
    ball2.set_data(circle_move2(t=i, A=3, f=0.5))
    return line1, ball1, line2, ball2
 
 
ani = FuncAnimation(fig, update, frames=np.arange(-8*np.pi, 8*np.pi, 0.1), interval=100)            



#ani = FuncAnimation(fig, animate, frames=np.arange(-2*np.pi, 2*np.pi, 0.1), interval=100)   


ani.save('anim2.gif')