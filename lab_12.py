import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 1460, 1)
 
def radio_function(n, t):
    dndt = - k*n*t
    return dndt
 
n_0 = 1000
k = 0.08

n_t = odeint(radio_function, n_0, t)
 
plt.plot(t, n_t[:,0])
plt.savefig('ssss.png')