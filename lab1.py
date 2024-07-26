def dec_par(x1):
    def dec_ril(func):
        def wrapper(num):
            x2 =  func(num)
            print(x1+x2)
        return wrapper
    return dec_ril

@dec_par(6)
def num(x2):
    return x2

num(-3)