import numpy as np
def funcao (x):
  y = x * 10
  return y

vetor1 = np.random.randint(1,100, size=10)
print(vetor1)
for x in vetor1:
  print(funcao(x))
