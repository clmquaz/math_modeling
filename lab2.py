def dec(func):
    def wrapped(a, b, c):
            if c =='+':
                  print(a+b)
            elif c =='-':
                  print(a-b)
            else:
                print(a/b)
    return wrapped

@dec
def num(a, b, c):
    return a,b, c

num(3, 88, '/')