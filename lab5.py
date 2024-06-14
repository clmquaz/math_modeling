a = int(input('a '))
b = int(input('b '))

if b != 0:
    if a/b == a//b:
        print(a/b)
    else:
        print(a/b, a%b)
else:
    print('false')