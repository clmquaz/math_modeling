from модуль_физ_конст import  g

def uuu (m=0,h=0,v=0):
  m = int(input("m = "))
  h = int(input("h = "))
  v = int(input("v = "))
  E = m*(v**2)/2+m*g*h
  print(f'полная механическая энергия тела = {E}')
print(uuu())