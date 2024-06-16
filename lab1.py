import numpy as np
 

a = [2, 44, 51, 33]
b = np.array(a)

def f_func(b):
    x = 0
    for i in range(0, len(b), 1):
        x += b[i]
    print(x/len(b))

f_func(b)