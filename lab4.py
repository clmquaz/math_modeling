import numpy as np



N = int(input('N '))
M = int(input('M '))

trigonometry_array = np.zeros((N, M))
print(trigonometry_array)

for i in range(0, N, 1):
    for j in range(0, M, 1):
        print(i)
        print(j)
        trigonometry_array[i, j] = np.sin(np.pi/180*(N*i + M*j +1))

