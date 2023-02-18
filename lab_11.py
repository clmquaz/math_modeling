import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 180, 0.1)
 
def radio_function(n, t):
    dndt =  k*n
    return dndt
 
n_0 = 2
k = 1/15

n_t = odeint(radio_function, n_0, t)
 
plt.plot(t, n_t[:,0])
plt.savefig('sss.png')