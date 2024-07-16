import matplotlib.pyplot as plt
import numpy as np


N = 100
a = 4
b = 2

x = np.linspace(-a, a, N)
y = np.linspace(-b, b, N)

X, Y = np.meshgrid(x, y)
fxy = X**2/a**2 + Y**2/b**2 - 1

plt.contour(X, Y, fxy, levels=[0])
plt.axis('equal')

plt.savefig('p3')