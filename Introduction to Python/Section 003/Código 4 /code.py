def vogais (x): 
  lista = []
  vogais = ['a', 'e', 'i', 'o', 'u']
  for i in x: 
    if i in vogais: 
      lista.append(i)
  return lista

palavra = input("Digite uma palavra: ")
vogais(palavra)
