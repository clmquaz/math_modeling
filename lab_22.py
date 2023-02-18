import numpy as np
from scipy.integrate import odeint
import matplotlib.pyplot as plt

t = np.arange(0, 24, 0.01)

def radio_function(S, t):
    dsdt = np.sqrt(S/np.pi)*S*np.cos(np.pi/12*(t-12))*Es*k
    return dsdt

Es = 1367
k = 1.2
S0 = 1600

S_t = odeint(radio_function, S0, t)
 
plt.plot(t, S_t[:,0])
plt.savefig('s.png')


