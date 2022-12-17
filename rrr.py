import numpy as np
import matplotlib.pyplot as plt

def func(xa=1, xb=10, N=10, a=1, b=0, c=0, label='purubola'):
    if a < 0 or a > 0:
        x = np.linspace(-xa, xa, N)
        y = x**2

        
    else:
        x = np.linspace(xa, xb, N)
        y = -x**2
    plt.plot(x, y)
    plt.savefig('ppp.png')

print(func())