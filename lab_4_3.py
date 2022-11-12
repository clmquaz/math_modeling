import from модуль_физ_конст.py g

def uuu (m,h,v):
  m = int(input("m = "))
  h = int(input("h = "))
  v = int(input("v = "))
  E = m*(v**2)/2+m*g*h
  print(f'полная механическая энергия тела = {E}')