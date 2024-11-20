# 1. Escreva um programa que receba dois números do usuário e imprima a soma, subtração, multiplicação e divisão deles.

a = int(input("Digite o primeiro número: "))
b = int(input("Digite o segundo número:"))

soma = a + b
subtracao = a - b 
multiplicacao = a * b
divisao = a/b 

print(f"a soma de {a} e de {b} foi de {soma}")
print(f"a subtração de {a} e de {b} foi de {subtracao}")
print(f"a multiplicação de {a} e de {b} foi de {multiplicacao}")
print(f"a divisão de {a} e de {b} foi de {divisao}") 
