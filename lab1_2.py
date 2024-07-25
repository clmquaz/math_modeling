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

ball, = plt.plot([], [], '-', color='r', label='Ball')

def circle_move(t):
    R = 1
    x0 = R*(t-np.sin(t))
    y0 = R*(1-np.cos(t))
    alpha = np.arange(0, 2*np.pi, 0.1)
    R = 0.1
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
    ball.set_data(circle_move(t=i))
    return line, ball
 
ani = FuncAnimation(fig, update, frames=np.arange(-2*np.pi, 2*np.pi, 0.1), interval=100)            
 


#ani = FuncAnimation(fig, animate, frames=np.arange(-2*np.pi, 2*np.pi, 0.1), interval=100)   


ani.save('anim1.gif')


fig, ax = plt.subplots() 
 
line, = plt.plot([], [], '-', lw=2)
 
xdata, ydata = [], [] 



edge = 7
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)

ball, = plt.plot([], [], '-', color='r', label='Ball')

def circle_move(t):
    R = 1
    x0 = R*np.cos(t)**3
    y0 = R*np.sin(t)**3
    alpha = np.arange(0, 2*np.pi, 0.1)
    R = 0.1
    x = x0 + R*np.cos(alpha)
    y = y0 + R*np.sin(alpha)
    return x, y

def line_move(t):
    R = 1
    xdata.append(R*np.cos(t)**3)
    ydata.append(R*np.sin(t)**3)
    return xdata, ydata

def update(i):
    line.set_data(line_move(t=i)) 
    ball.set_data(circle_move(t=i))
    return line, ball
 
ani = FuncAnimation(fig, update, frames=np.arange(-2*np.pi, 2*np.pi, 0.1), interval=100)            
 


#ani = FuncAnimation(fig, animate, frames=np.arange(-2*np.pi, 2*np.pi, 0.1), interval=100)   


ani.save('anim2.gif')