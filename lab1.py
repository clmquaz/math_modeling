import numpy as np
import matplotlib.pyplot as plt

def a1(R):

    t = np.arange(-2*np.pi, 2*np.pi, 0.1)

    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))

    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('p1_1')

def a2(R):

    t = np.arange(-2*np.pi, 2*np.pi, 0.1)

    y = R*np.sin(t)**3
    x = R*np.cos(t)**3

    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('p1_2')

