class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
    
    def __iadd__(self, other):
        self.planets.append(other)
        return self
    
system1 = StarSystem(['p1'], 'System_1')
system1 += 'p2'
print(system1.planets)