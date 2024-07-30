import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
fig, ax = plt.subplots() 
 
line, = plt.plot([], [], '-', lw=2)
xdata, ydata = [0.1], [0.1] 


edge = 1
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(0, edge)



def line_move(n, C, D):
    xdata.append(xdata[n]**2-ydata[n]**2+C)
    ydata.append(2*xdata[n]*ydata[n]+D)
    return xdata, ydata

def update(i):
    line.set_data(line_move(n=i, C=0.3, D=0.33))
    return line
 
 
ani = FuncAnimation(fig, update, frames=np.arange(0, 100, 1), interval=100)            

ani.save('a4.gif')