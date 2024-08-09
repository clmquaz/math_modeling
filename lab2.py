class Cell:
    def __init__(self, n):
        self.cell = ['cell']*n
        
    def __add__(self, other):
        cell_1 = ['cell']*(len(self.cell)+len(other.cell))
        return cell_1
    
    def __sub__(self, other):
        cell_1 = ['cell']*(len(self.cell)-len(other.cell))
        return cell_1
        
    def __mul__(self, other):
        cell_1 = ['cell']*(len(self.cell)*len(other.cell))
        return cell_1
        
    def __truediv__(self, other):
        cell_1 = ['cell']*round(len(self.cell)/len(other.cell))
        return cell_1


     
s = Cell(6)
d = Cell(3)
print(s/d)
        