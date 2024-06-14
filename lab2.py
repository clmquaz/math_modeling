import numpy as np
import math
import lab1 as l


h = 100
a = np.pi/3
b = 30

v = np.sqrt(l.g*h*np.tan(b)**2/2*np.cos(a)**2*(1-np.tan(b)*np.tan(a)))
print(v)


T = 200

N = 2/np.sqrt(np.pi)*l.h/(l.k*T)**(3/2)*math.e**(-math.e/(l.k*T))*math.e**(T/2)
print(N)