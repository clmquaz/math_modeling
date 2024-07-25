import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots() 
 
line, = plt.plot([], [], '-', lw=2)
 
xdata, ydata = [], [] 

edge = 7
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ball1, = plt.plot([], [], '-', color='r', label='Ball')
ball2, = plt.plot([], [], '-', color='r', label='Ball')

def circle_move(t):
    R = 1
    x0 = R*(t-np.sin(t))
    y0 = R*(1-np.cos(t))
    alpha = np.arange(0, 2*np.pi, 0.1)
    R = 0.1
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y

def ball_move(t):
    R = 1
    x0 = R*(t-np.sin(t))-R*(t-np.sin(t))/2
    y0 = R/2
    alpha = np.arange(0, 2*np.pi, 0.1)
    R = R*(np.pi-np.sin(np.pi))/2
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y

def line_move(t):
    R = 1
    xdata.append(R*(t-np.sin(t)))
    ydata.append(R*(1-np.cos(t)))
    return xdata, ydata

def update(i):
    line.set_data(line_move(t=i)) 
    ball1.set_data(circle_move(t=i))
    ball2.set_data(ball_move(t=i))
    return line, ball1, ball2
 
ani = FuncAnimation(fig, update, frames=np.arange(-2*np.pi, 2*np.pi, 0.1), interval=100)            
 


#ani = FuncAnimation(fig, animate, frames=np.arange(-2*np.pi, 2*np.pi, 0.1), interval=100)   


ani.save('anim3.gif')
