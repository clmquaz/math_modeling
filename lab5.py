from lab4 import trigonometry_array
from lab4 import N

x = 0
y = 1
s=0
for i in range(0, N, 1):
        s = trigonometry_array[i, x]
        trigonometry_array[i, x] = trigonometry_array[i, y]
        trigonometry_array[i, y] = s

print(trigonometry_array)