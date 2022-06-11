texto = input("Ingrese un string: ")
indice1 = int(input("Ingrese el primer índice: "))
indice2 = int(input("Ingrese el segundo índice: "))

largo = len(texto)

if (indice1 < -largo) or (indice2 < -largo) or \
(indice1 >= largo) or (indice2 >= largo):
  print("Los indices indicados no son válidos")
else:
  lista = list(texto)
  lista[indice1], lista[indice2] = lista[indice2], lista[indice1]

  print( ''.join(lista) )
