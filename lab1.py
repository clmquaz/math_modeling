class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
    
    def __sub__(self, other):
        planets_1 = self.planets.copy()
        planets_1.remove(other)
        return StarSystem(planets_1, self.name)
        
    def __rsub__(self, other):
        planets_1 = self.planets.copy()
        planets_1.remove(other)
        return StarSystem(planets_1, self.name)   
         
    def __isub__(self, other):
        self.planets.remove(other)
        return self
        
    
f = StarSystem(['p1', 'p2', 'p3'], 'a')
f -= 'p1'
print(f.planets)
v = f - 'p2'
print(v.planets)
v = 'p2' - f
print(v.planets)