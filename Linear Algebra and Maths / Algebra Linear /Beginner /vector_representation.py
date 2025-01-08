import numpy as np 

# Crie dois vetores (v1) e (v2) com o numpy 

v1 = np.array([1,2,3])
v2 = np.array([4,5,6])

print(v1)
print(v2)

# soma de 2 vetores 
soma = v1 + v2 
print(f" a soma dos vetores é {soma}")

# produto escalar dos vetores 
produto_escalar = np.dot(v1,v2)
print(f" o produto escalar de dois vetores vai resultar no seguinte escalar = {produto_escalar}")

# norma/magnitude dos vetores - forma com o numpy 
norma_1 = np.linalg.norm(v1)
norma_2 = np.linalg.norm(v2)
print(f" a norma do vetor 1 é {norma_1}")
print(f" a norma do vetor 2 é {norma_2}")
