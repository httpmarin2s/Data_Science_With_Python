# 10. Escreva um programa que encontre o maior e o menor número em uma lista fornecida pelo usuário.]
import numpy as np 
numero = np.random.randint(1,100, size=10)
numero = sorted(numero)
print(numero)
print(max(numero))
print(min(numero))
