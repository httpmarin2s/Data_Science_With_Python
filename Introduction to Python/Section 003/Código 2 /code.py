#Crie uma função que receba uma lista de números e retorne apenas os números pares dessa lista.

def numeros_pares(lista): #define  função
  pares = [] # lista vazia 
  for i in lista: # para cada item de lista, o for loop vai funcionar com base em cada item da lista, exemplo, se tiver 10 elementos o for loop vai acontecer 10x
    if i % 2 == 0: 
      pares.append(i)
  return(pares)

lista1 = [1,2,3,4,5,6,7,8,9,10]
numeros_pares(lista1)
