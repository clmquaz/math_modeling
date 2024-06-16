import numpy as np

b = np.random.randint(-22, 30, size = (1, 1, 3))
a = b[0, 0]
def f_func(a):
    x = 1
    for i in range(0, len(a), 1):
        x *= a[i]
    print(x)

f_func(a)