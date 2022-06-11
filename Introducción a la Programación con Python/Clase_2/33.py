#Convirtiendo numeros

def text2number(text):
  num_str = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  num_int = [ 0,   1,   2,   3,   4,   5,   6,   7,   8,   9]

  number = 0
  sign = 1

  i = 0
  while text[i] == ' ':
    i += 1
    if i == len(text):
      return None # Inválido, sólo hay espacios

  if text[i] == '+':
    sign = 1      # Positivo
    i += 1
  if text[i] == '-':
    sign = -1     # Negativo
    i += 1

  if i == len(text):
    return None # Inválido, sólo hay espacios y/o signos +-

  while i < len(text):
    if text[i] in num_str:
      number *= 10                 # Multiplico por 10 lo que tenía
      index = num_str.index( text[i] )
      number += num_int[index] # y sumo el nuevo dígito
    elif text[i] != ' ':
      return None # Inválido, no es ni número ni espacio
    else:
      break  # Llegué a un espacio
    i += 1

  if i < len(text):
    while text[i] == ' ':
      i += 1
      if i == len(text):
        return sign*number # Válido, llegué al final
    else:
      return None          # Inválido, el número ya terminó y no es un espacio
  else:
    return sign*number     # Válido, no hay más espacios despues del número

print(text2number('   +123   '))
print(text2number(' 4 5 6 '))
print(text2number(' -789 '))
print(text2number(' - 123 '))
print(text2number('456'))
