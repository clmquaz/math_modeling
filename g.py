import math
import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

fig, ax = plt.subplots()
line, = plt.plot([], [], '-', color='r', label='Ball')

ax.set_xlim(2.5,np.pi*2+0.5)
ax.set_ylim(-2, 1)

F = 100
m = 15
g = 9.81
l = 1

d = F/m/g
k = math.asin(d)
LR = k*(180/np.pi)
print(LR)

L = 3*np.pi/2 - ((np.pi/2)/90)*LR
R = 3*np.pi/2 + ((np.pi/2)/90)*LR
s = np.arange(R, L, -0.05)
v = np.arange(L, R, 0.05)
T = []

n = (2*np.pi-(3*np.pi/2))/2+(3*np.pi/2)
p = (np.pi/2)/2+2*np.pi
m = ((p-n)/90)*LR
g = n+m
f = n-m
l = np.arange(g, f, -0.05)
r = np.arange(f, g, 0.05)
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

def line_move(t):
    alpha = np.arange(np.pi, 3*np.pi/2, 0.1)
    R = 0.7
    x = R*np.cos(alpha)
    y = R*np.cos(alpha)

    X = y*np.sin(t)+x*np.cos(t)+3*np.pi/2
    Y = x*np.sin(t)-y*np.cos(t)
    return X, Y

def animater(i):
    line.set_data(line_move(t=i))

ani = FuncAnimation(fig, animater, frames=TLr, interval=30)
 
ani.save('g.gif')