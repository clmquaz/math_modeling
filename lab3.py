import functools
import math
 
def debug(func):
    @functools.wraps(func)
    def wrapper_debug(*args, **kwargs):
        args_repr = [str(a) for a in args]
        kwargs_repr = [f"{k}={v}" for k, v in kwargs.items()]
        signature = ", ".join(args_repr + kwargs_repr)
        print(f"Вызываем функцию {func.__name__}({signature})")
        value = func(*args, **kwargs)
        print(f"Функцию {func.__name__} вернула значение {value}")
        return value
 
    return wrapper_debug
@debug
def num(x, y ):
    x2 = (x+y)
    return x2

num(2, 3)
num(4,5)