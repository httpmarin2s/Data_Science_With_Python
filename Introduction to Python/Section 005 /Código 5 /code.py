import numpy as np

def calcular_media(x):
  media = np.mean(x)
  return media

vetor1 = np.random.randint(1,100, size=10)
print(vetor1)
print(calcular_media(vetor1))
