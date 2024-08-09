import numpy as np
class ClassVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __len__(self):
        return np.sqrt(self.x**2+self.y**2+self.z**2)
    
    def __str__(self):
        return f'x={self.x}, y={self.y}, z={self.z}'
    
    def __repr__(self):
        return f'Vector (x={self.x}, y={self.y}, z={self.z})'
    
    def __add__(self, other):
        if type(other) == ClassVector:
            x1 = self.x + other.x
            y1 = self.y + other.y
            z1 = self.z + other.z
            return ClassVector(x1, y1, z1)
        else:
            print('Traceback (most recent call last):\n  File "/workspaces/math_modeling/lab3.py", line 17 \n   def __add__(self, other):\n                     ^\nSyntaxError: invalid syntax.')
    
    def __sub__(self, other):
        if type(other) == ClassVector:
            x1 = self.x - other.x
            y1 = self.y - other.y
            z1 = self.z - other.z
            return ClassVector(x1, y1, z1)
        else:
            print('Traceback (most recent call last):\n  File "/workspaces/math_modeling/lab3.py", line 26 \n   def __add__(self, other):\n                     ^\nSyntaxError: invalid syntax.')
    
    def __mul__(self, other):
        if type(other) == ClassVector:
            x1 = self.x * other.x
            y1 = self.y * other.y
            z1 = self.z * other.z
            return ClassVector(x1, y1, z1)
        elif type(other) == int or type(other) == float:
            x1 = self.x * other
            y1 = self.y * other
            z1 = self.z * other
            return ClassVector(x1, y1, z1)
        else:
            print('Traceback (most recent call last):\n  File "/workspaces/math_modeling/lab3.py", line 26 \n   def __add__(self, other):\n                     ^\nSyntaxError: invalid syntax.')
    
    def 




    
v = ClassVector(2, 4, 5)
a = ClassVector(2, 4, 5)
#print(v.__len__())
#print(v)
print(v+2.3)
#print(v.__repr__())
    
