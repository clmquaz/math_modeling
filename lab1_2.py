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
 

def update(t):
    R = 1
    xdata.append(R*(t-np.sin(t))) 
    ydata.append(R*(1-np.cos(t))) 
    line.set_data(xdata, ydata) 
    return line,
 
#ani = FuncAnimation(fig, update, frames=np.arange(-2*np.pi, 2*np.pi, 0.1), interval=100)            
 




ball, = plt.plot([], [], '-', color='r', label='Ball')

def circle_move(t):
    R = 1
    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))
    return x, y
    
def animate(i):
    ball.set_data(circle_move(t=i))

ani = FuncAnimation(fig, animate, frames=np.arange(-2*np.pi, 2*np.pi, 0.1), interval=100)   


ani.save('anim1.gif')