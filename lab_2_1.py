import numpy as np
import matplotlib.pyplot as plt

def figrs(u=2/np.pi, A=1, a=1, B=10): 
    s = np.arange(1, B, 1)
    t = 1/a
    b = a/s
    x = A * np.sin(a * t + u)
    y = B * np.sin(b * t)
    plt.plot(x, y)
    plt.axis('equal')
    plt.savefig('sw.png')

figrs()