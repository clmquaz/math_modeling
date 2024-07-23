import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
def butt (n=5):
    fig, ax = plt.subplots()
    
    anim_object, = plt.plot([], [], '-', lw=2) 

    xdata, ydata = [], [] 
    
    edge = n
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    def update(t):
        xdata.append(np.sin(t)*(math.e**(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5)) 
        ydata.append( np.cos(t)*(math.e**(np.cos(t))-2*np.cos(4*t)+np.sin(t/12)**5))
        anim_object.set_data(xdata, ydata)
        return anim_object,
    
    ani = FuncAnimation(fig, update, frames=np.linspace(0, 12*np.pi, 600),interval=100,)           
    
    ani.save('a3.gif')

def heart (n=25):
    fig, ax = plt.subplots()
    
    anim_object, = plt.plot([], [], '-', lw=2) 

    xdata, ydata = [], [] 
    
    edge = n
    plt.axis('equal')
    ax.set_xlim(-edge, edge)
    ax.set_ylim(-edge, edge)

    def update(t):
        xdata.append(16*np.sin(t)**3) 
        ydata.append(13*np.cos(t)-5*np.cos(2*t)-2*np.cos(3*t)-np.cos(4*t))
        anim_object.set_data(xdata, ydata)
        return anim_object,
    
    ani = FuncAnimation(fig, update, frames=np.linspace(0, 2*np.pi, 100),interval=100,)           
    
    ani.save('a3_2.gif')