
z = []
for i in range(1, 10, 1):
  for a in range(1, 10, 1):
          x = a*i
          z.append(x)
  print(str(z).strip('[]'))
  z=[]
