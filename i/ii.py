import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots()
line, = plt.plot([], [], '-', color='r', label='Ball')
 
o = (3*np.pi/2-np.pi)/2+np.pi
p = (np.pi/2)/2+2*np.pi
l = np.arange(p, o, -0.05)
r = np.arange(o, p, 0.05)
TLr = []

def TT(l, r):
    for i in range(len(l)-1, 0, -1):
        h = l[i]
        TLr.append(h)
    for i in range(len(r)-1, 0, -1):
        j = r[i]
        TLr.append(j)
    return TLr
TT(l, r)


def line_move(R, t):
    alpha = np.arange(0, np.pi/2, 0.1)
    x = R*np.cos(alpha)
    y = R*np.cos(alpha)

    X = y*np.sin(t)+x*np.cos(t)
    Y = x*np.sin(t)-y*np.cos(t)
    return X, Y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
def animater(i):
    line.set_data(line_move(R=1, t=i))
    	
ani = FuncAnimation(fig, animater, frames=TLr, interval=30)
 
ani.save('ii2.gif')

