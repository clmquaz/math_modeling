class Cl:
    count = 0
    def __init__(self):
        Cl.count = Cl.count +1
    @classmethod
    def classmethod(cls):
        print(cls.count)

Cl.classmethod()
d = Cl()
s = Cl()
sd = Cl()
Cl.classmethod()