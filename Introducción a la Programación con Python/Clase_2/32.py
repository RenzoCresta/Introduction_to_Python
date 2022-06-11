#problema estadístico, análisis productivo

archivo = open("ControlCalidadBotellas.csv")
contenido = archivo.readlines()
contenido = contenido[1:]     # Descarto la primera fila

fallas = []
for renglon in contenido:
  dato = renglon.split(',')[1]  # Me quedo con el segundo elemento
  dato = dato.replace('\n', '') # Descarto el caracter de escape \n
  fallas.append( int(dato) )    # Convierto el dato a un tipo numérico

media = sum(fallas) / len(fallas)

var = 0
for f in fallas:
  var += (f-media)**2
var /= len(fallas)

# Creo una lista de ceros, con indices de 0 a max(fallas)
ocurrencias = [0] * (max(fallas)+1)
for f in fallas:
  ocurrencias[f] += 1

moda = ocurrencias.index( max(ocurrencias) )

fallas.sort()
mediana = fallas[ len(fallas) // 2 ]

print("La media es:", media)
print("La varianza es:", var)
print("La moda es:", moda)
print("La mediana es:", mediana)
