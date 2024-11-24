def numero_primo(numero): 
    if numero <= 1:  # Primeira condição: Números menores ou iguais a 1 não são primos
        return False
    for i in range(2, int(numero**0.5) + 1):  # Verifica divisores até a raiz quadrada do número
        if numero % i == 0: 
            return False
    return True  # Se não encontrou divisores, é primo
  
print(numero_primo(10))  # Deve retornar False, pois 10 não é primo
print(numero_primo(11))  # Deve retornar True, pois 11 é primo
