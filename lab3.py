a = int(input('r '))

if a/4 == a//4:
    if a/400==a//400:
        print('yes')
    elif a/100!=a//100:
        print('yes')
    else:
        print('no')
else:
    print('no')