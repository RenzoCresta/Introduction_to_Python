def segundo_valor(x):
  return x[1]

file = open("noticia.txt") # cargamos el archivo a la memoria
contenido = file.readlines() # calculamos todas las lineas

tildes = {'á':'a', 'é':'e', 'í':'i', 'ó':'o', 'ú':'u'}

total = 0
ocurrencias = {}
for renglon in contenido:
  renglon_lower = renglon.lower() # pasamos a minúscula el archivo.
  for letra in renglon_lower:
    # Si la letra tiene tilde, la remplazo por su versión sin tilde.
    if letra in tildes:
      letra = tildes[letra]

    if letra.isalpha():
      # Si la letra es alfanumerica, la agrego a la lista de ocurrencias.
      # Info get(): https://www.w3schools.com/python/ref_dictionary_get.asp
      ocurrencias[letra] = ocurrencias.get(letra, 0) + 1
      total += 1

items = ocurrencias.items()

# Info Sorted: https://www.programiz.com/python-programming/methods/built-in/sorted
# Ordenamos las ocurrencias de mayor a menor.
lista = sorted(items, key = segundo_valor, reverse = True)

for k,v in lista:
  print("{} aparece {} veces: {:0.3f} %".format(k, v, v/total * 100))
