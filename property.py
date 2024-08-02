class Sum:
    def __init__(self, a, b):
        self.a = a
        self.b = b

    @property
    def sum_two_num(self):
        q = f'Sum of two numbers =+ {self.a+self.b}'
        print(q)


ss = Sum(1, 2)
ss.sum_two_num