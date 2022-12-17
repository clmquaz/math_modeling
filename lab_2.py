import numpy as np
import matplotlib.pyplot as plt

def gip(x=2, n=10):
    x = np.arange(1, n, 0.1)
    y = 1/x
    plt.plot(x, y)
    plt.savefig('so.png')

print(gip())