#palindromo

def palindromo(texto):
  puntuacion = [' ','.', ',', ':', ';', '-', '¿', '?', '¡', '!']
  nuevo_texto = ''
  for letra in texto:
    if letra not in puntuacion:
      nuevo_texto += letra
  texto = nuevo_texto.lower()
  return texto == texto[::-1]

print( palindromo( "reconocer" ) )
print( palindromo( "Neuquén" ) )
print( palindromo( "¿Acaso hubo buhos aca?" ) )
print( palindromo( "¡Arriba la birra!" ) )
print( palindromo( "No di mi decoro, cedi mi don." ) )
