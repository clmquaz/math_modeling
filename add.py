class Number:
    def __init__(self, val):
        self.val = val
        
    def __add__(self, other):
        print('add', self.val, other)
        return self.val + other
    
    # __radd__ = __add__
    
    def __radd__(self, other):
        print('radd', other, self.val)
        return other + self.val
    
x = Number(32)
y = Number(25)

print(x + 1)
print(2 + y)
print(x + y)