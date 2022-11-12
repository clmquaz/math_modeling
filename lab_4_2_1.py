def www (a = 1, n = 1):
    a = int(input('a = '))
    n = int(input('n = '))
    l = []
    r = 1
    for i in range(0, n, 1):
        t = r*a
        r = t
        i+1
        l.append(r)
    g =l[len(l)-1]
    print(g)
print(www())
