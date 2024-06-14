a1 = []
for i in range(1, 10, 1):
    for ii in range(1, 10, 1):
        a1.append(i*ii)
print(a1)

r = 0
aa1 = []
for i in range(1, 10, 1):
    for a in range(0, 9, 1):
        r = i+9*a
        aa1.append(a1[r-1])
    print(aa1)
    aa1.clear()