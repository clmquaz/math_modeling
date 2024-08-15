
def fun(n, nu, a):
    if len(a)!=n:
        a.append(nu)
        fun(n, nu+1, a)
    else:
        return a
a = []   
fun(100, 1, a)


def ffunc(num, a):
    if num < a[int(len(a)/2)-1]:
        print(a)
        print(f'num < {a[int(len(a)/2)-1]}')
        ffunc(num, a[0:int(len(a)/2)-1])
    elif num > a[int(len(a)/2)-1]:
        print(a)
        print(f'num > {a[int(len(a)/2)-1]}')
        ffunc(num,  a[int(len(a)/2):len(a)])
    else:
        print(a)
        print(f'num == {a[int(len(a)/2)-1]}')

ffunc(25, a)





















