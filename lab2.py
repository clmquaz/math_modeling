class Cell:
    cells = 0
    def __init__(self, n):
        self.cell = [cell]*n
        cells += 1
    
    def __add__(self, other):
        cell_1 = self.cell.copy()
        for i in range(0, len(other.cell.copy())):
            cell_1.append(other.cell.copy[i])
        return cell_1
    
    def __sub__(self, other):
        cell_1 = self.cell.copy()
        for i in range(0, len(other.cell.copy())):
            cell_1.pop(0)
        return cell_1
        
    def __mul__():
        
        
    def __truediv__():
        
        