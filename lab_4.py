import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()

anim_object, = plt.plot([], [], '-', lw=2)
xdata, ydata = [], []



def apdate(n, xy0, C, D ):
    x = np.zeros((1, n))
    y = np.zeros((1, n))
    x[1,0] = 
    y[1,0] = 
    xdata.append(x)
    ydata.append(y)
    return xdata, ydata
