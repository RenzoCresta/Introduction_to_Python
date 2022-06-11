#mediciones CSV

def derivada(x):
    return [x[i] - x[i-1] for i in range(1,len(x))]

file = open("mediciones.csv") # cargamos el archivo a la variable file
contenido = file.readlines()  # obtenemos todas las lineas
datos = contenido[20:]        # eliminamos las primeras 20 lineas

time = []
channel1 = []
channel2 = []

for linea in datos:
  valores = linea.split(',')
  t = float( valores[0] )
  c1 = float( valores[1] )
  c2 = float( valores[2].replace('\n', '') )  # eliminamos los '\n'
  time.append( t )
  channel1.append( c1 )
  channel2.append( c2 )

instantes = []
signo = 0
for i in range(1, len(channel1)):
  if channel1[i] > 0:
    if signo == -1:   # Si hay un cambio en los signos, agrego el instante
      instantes.append(time[i])
    signo = 1         # Actualizo la variable signo
  elif channel1[i] < 0:
    signo = -1

print( instantes )
print( derivada(instantes) )
