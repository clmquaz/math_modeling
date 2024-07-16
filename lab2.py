import matplotlib.pyplot as plt
import numpy as np

k = 1
xs = -1
xe = 1
N = 100

x = np.linspace(xs, xe, N)


if xs<0 or xe<0:
    y1=[]
    y2 = []
    x1=[]
    x2 = []
    for x in x:
        if x<0:
            y = k/x
            x1.append(x)
            y1.append(y)
        elif x>0:
            y = k/x
            x2.append(x)
            y2.append(y)
        else:
            x=x
    plt.plot(x1, y1)
    plt.plot(x2, y2)
else:
    x = np.linspace(xs, xe, N)
    y = k/x
    plt.plot(x, y)

plt.savefig('p2')