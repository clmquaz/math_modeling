
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)
xdata, ydata = [], []

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)

def apdate(t):
    x = np.sin(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5)
    y = np.cos(t)*(np.exp(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5)
    xdata.append(x)
    ydata.append(y)
    return xdata, ydata

def animate(i):
    anim_object.set_data(apdate(t=i))

ani = FuncAnimation(fig, animate, frames=np.arange(0, 12*np.pi, 0.1), interval=100) 

#ani.save('lon.gif')


heart, = plt.plot([], [], '-', lw=2)
xdata, ydata = [], []

ax.set_xlim(-20, 20)
ax.set_ylim(-20, 20)

def hearter(t):
    x = 16*np.sin(t)**3
    y = 13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t)
    xdata.append(x)
    ydata.append(y)
    return xdata, ydata

def animater(i):
    anim_object.set_data(hearter(t=i))

anier = FuncAnimation(fig, animater, frames=np.arange(0, 2*np.pi, 0.1), interval=100) 

anier.save('loner.gif')