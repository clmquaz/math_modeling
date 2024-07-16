import matplotlib.pyplot as plt
import numpy as np


δ = np.pi/2
a = 1 
b = a/2
A = 1
B = 1
N = 100

x=[]
y=[]

for t in np.linspace(0, 10, N):
    xx = A * np.sin(a *t + δ)
    yy = B * np.sin(b * t)
    x.append(xx)
    y.append(yy)

plt.plot(x, y)
plt.savefig('p11')