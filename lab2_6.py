import numpy as np

a = [1, 3, 2010]
b = np.array(a)
x=0
y=0

if b[2]>=0:
    if b[1]==7 and b[0]>1 or b[1]>7:
        n = 1
    else:
        n = 2
else:
    if b[1]==7 and b[0]>1 or b[1]>7:
        n = 0
    else:
        n = 1

x = (b[2]+776-n)//4+1
y = (b[2]+776-n)%4 +1

print(f'OL {x}.{y}')