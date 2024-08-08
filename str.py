class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
        
    def __str__(self):
        return f'Название системы {self.name} \
            и её планеты{[i for i in self.planets]}'
    
sys1 = StarSystem(['p1', 'p2'], 'Sys1')
print(sys1)