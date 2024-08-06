class Planet:
    planets = []
    def __init__(self, R, l, name):
        self.radius = R
        self.len = l
        Planet.planets.append(name)
    @property
    def look(self):
        print(f'Угловой диаметр палнеты = {2*self.radius/self.len} рад.')
    @staticmethod
    def time(l):
        print(f'До планеты лететь {l/((3*10**8)*60*60*24*365.256)}свет. лет')
    @classmethod
    def names(cls):
        print(f'Планеты: {cls.planets}')

Planet.time(293580235730475384657)
ss = Planet(40000, 293580235730475384657, 'astro')
ss.look
Planet.names()