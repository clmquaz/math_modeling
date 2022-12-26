import numpy as np
import matplotlib.pyplot as plt
 

def cicle(R=2, t1=0, t2=8*np.pi):
    t = np.arange(t1, t2, 0.1)
    x = R*(t-np.sin(t))
    y = R*(1-np.cos(t))
    plt.plot(x, y)
    plt.savefig('d.png')


def astr(R=2, t1=0, t2=2*np.pi):
    t = np.arange(t1, t2, 0.1)
    x = R*np.cos(t)**3
    y = R*np.sin(t)**3
    plt.plot(x, y)
    plt.savefig('f.png')
    
astr()