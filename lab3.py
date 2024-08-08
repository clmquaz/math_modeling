import numpy as np
class ClassVector:
    def __init__(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        
    def __len__(self):
        return np.sqrt(self.x**2+self.y**2+self.z**2)
    
v = ClassVector(2, 4, 5)
print(len(v))
    
    