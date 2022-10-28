import numpy as np

a =     [1, 5, 3, 6]

slice = a[2:5:1]
print(slice = a[2:5:1])

slice = a[3:0:-1]
print(slice)

slice = a[::-1]
print(slice)
	
b = np.array([a, np.array(a)*3])
slice = b[::, 1]
print(slice)
slice = b[1,2:3:1]
print(slice)
slice = b[1,2::1]
print(slice)