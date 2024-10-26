def fun(n, nu, a, z):
    if len(a)!=n:
        a.append(nu)
        if n%nu == 0:
            z.append(nu)
        else:
            pass
        fun(n, nu+1, a, z)
    else:
        return a, z
    
def number(p):
    a = []
    z = []
    fun(p, 1, a, z)
    s = lambda z: 'yes' if len(z)==2 or len(z) ==1 else 'no'
    if s(z) == 'yes':
        yield 2**p
    else:
        pass


number(2)











def func(n, nu, a, z):
    if len(a)!=n:
        a.append(nu)
        if n%nu == 0:
            z.append(nu)
        else:
            pass
        fun(n, nu+1, a, z)
    else:
        return a, z
    

def numbers(p):
    a = []
    z = []
    fun(p, 1, a, z)
    for i in range(0, len(z)-1):
        z[i] = z[i]**2
    return z

print(numbers(4))