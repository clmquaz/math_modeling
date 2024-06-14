a = int(input('a '))
x = [1, 1]
for i in range(0, a-1, 1):
    y = x[i]+x[i+1]
    x.append(y)
print(x)