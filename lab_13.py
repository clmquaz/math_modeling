import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

 
def radio_function(v, r):
    dvdr = -(G*M/(v*r**2))
    return dvdr

v0 = 0.1
R = 6378.1*10**3
r = np.arange(10**8+R, R, -1000)
G = 6.67*10**(-11)
M = 5.973*10**24

n_t = odeint(radio_function, v0, r)
 
plt.plot(r, n_t[:,0])
plt.savefig('s.png')