def fun(n, nu, a):
    if len(a)!=n:
        a.append(nu)
        fun(n, nu+1, a)
    else:
        return a
    
def number(p):
    q = 0
    a = []
    fun(p, 1, a)
    map(lambda a, q: q+1 if 0 == p%a else q, a)
    print(q)
    s = lambda q: 'yes' if q==2 or q ==1 else 'no'
    print(s(q))
number(1)
