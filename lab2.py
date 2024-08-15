def ffunc(num, a):
    if num < a[int(len(a)/2)]:
        print(f'num < {a[int(len(a)/2)]}')
        ffunc(num, a[0:int(len(a)/2)])
    elif num > a[int(len(a)/2)]:
        print(f'num > {a[int(len(a)/2)]}')
        ffunc(num,  a[int(len(a)/2)+1:len(a)])
    else:
        print(f'num == {a[int(len(a)/2)]}')


def fun(n, nu, a):
    if len(a)!=n:
        a.append(nu)
        fun(n, nu+1, a)
    else:
        return a


def func(n):
    num = int(input('num: '))
    if num >= 1 and num <= n:
        print('num is correct')
        a = []
        fun(n, 1, a)
        ffunc(num, a)
    else:
        print('num is incorrect')

func(100)