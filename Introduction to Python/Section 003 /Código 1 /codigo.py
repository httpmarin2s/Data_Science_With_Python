# Escreva uma função chamada calcular_area_retangulo que recebe a largura 
# e o comprimento de um retângulo e retorna sua área.


def calcular_area_retangulo(x,y): 
  area = x * y 
  return area 

base = int(input("Digite a base do retângulo: "))
altura = int(input("Digite a altura do retângulo: "))
calcular_area_retangulo(base,altura)
