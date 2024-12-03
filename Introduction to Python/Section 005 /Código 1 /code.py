import numpy as np

def quadrado (x):
  y = x * x
  return y


lista1 = [1,2,3,4,5]
array = np.array(lista1)
for x in array:
  print(quadrado(x))
