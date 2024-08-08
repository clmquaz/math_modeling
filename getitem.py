class StarSystem:
    def __init__(self, planets, name):
        self.planets = list(planets)
        self.name = name
        
    def __getitem__(self, key):
        return self.planets[key]
    
sys1 = StarSystem(['p1', 'p2'], 'Sys1')
print(sys1[0])
print(sys1[0:2])