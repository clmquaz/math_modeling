class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
    
    def __add__(self, other):
        planets_1 = self.planets.copy()
        planets_1.append(other)
        return StarSystem(planets_1, self.name)
    
    def __radd__(self, other):
        planets_1 = self.planets.copy()
        planets_1.insert(0, other)
        return StarSystem(planets_1, self.name)
    
system1 = StarSystem(['p1'], 'System_1')
system1 = system1 + 'p2'
print(system1.planets)
