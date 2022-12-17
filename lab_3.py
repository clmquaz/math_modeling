import numpy as np
import matplotlib.pyplot as plt

def elps(a=2, b=1.5, n=100):
    x = np.linspace(-2*a, 2*a, n)
    y = np.linspace(-2*a, 2*a, n)
    X, Y = np.meshgrid(x, y)
    fxy = X**2/a**2 + Y**2/b**2 - 1
    plt.contour(X, Y, fxy, levels=[0])
    plt.axis('equal')
    plt.savefig('soow.png')

elps()