import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation
 
fig, ax = plt.subplots()
ball, = plt.plot([], [], '-', color='r', label='Ball')
 
def circle_move(R):
    alpha = np.arange(0, 2*np.pi, 0.1)
    x = R*np.cos(alpha)
    y = R*np.sin(alpha)
    return x, y

edge = 3
plt.axis('equal')
ax.set_xlim(-edge, edge)
ax.set_ylim(-edge, edge)
 
def animate(R):
    ball.set_data(circle_move(R=R))
    	
ani = FuncAnimation(fig, animate, frames=np.arange(0, 3, 0.1), interval=20)
 
ani.save('lec_7_complex_animation2.gif')



