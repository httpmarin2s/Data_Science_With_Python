#8. Escreva um programa que peça ao usuário para inserir 5 números. Adicione esses números a uma lista e depois imprima a lista em ordem crescente.
lista = [1,2,3,4,5]

for i in range(1,6): 
  x = int(input("digite um número: "))
  lista.append(x)
  print(lista)
