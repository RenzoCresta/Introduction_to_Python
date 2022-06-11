file = open("noticia.txt") # Guardamos el contenido del archivo en una variable

contenido = file.readlines() # Obtenemos una lista de renglones
palabras = []
no_deseado = ['\n', '"', ',', '.']

for line in contenido:

    # eliminamos los distintos carácteres no deseados uno por uno
    for caracter in no_deseado:
      line = line.replace(caracter,'')

    palabras_linea = line.split(' ') # separamos por espacios

    for palabra in palabras_linea: # por cada "string" separado por espacios
      if palabra != '':
        palabras.append(palabra.upper()) # convertimos todo a mayuscula

crater = 0
que = 0
for palabra in palabras:
  if palabra == 'CRÁTER':
    crater += 1
  if palabra == 'QUE':
    que += 1

print('Cantidad de ocurrencias de "cráter": ', crater)
print('Cantidad de ocurrencias de "que": ', que)
