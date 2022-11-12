l = []
for i in range(1, 2022, 1):
  l.append(i**2)
def ff (l):
  s = []
  for i in range(len(l)-2, 1, -1):
    h = l[i]+l[i-2]
    s.append(h)
  