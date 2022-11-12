from модуль_физ_конст import  g

def uuu (m=0,h=0,v=0):
  E = m*(v**2)/2+m*g*h
  print(f'полная механическая энергия тела = {E}')

print(uuu(4, 8, 10))