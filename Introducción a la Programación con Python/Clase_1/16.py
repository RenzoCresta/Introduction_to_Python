#Adivina adivinador...

numero = 50
respuesta = ''
turnos = 0

while respuesta != '=':

  print("Estoy pensando en el numero:", numero)
  respuesta = input("¿Tu numero es >, < o = ? ")

  if respuesta == '<':
     numero = numero - 1

  elif respuesta == '>':
     numero = numero + 1

  turnos += 1

print("Tardé", turnos, "turnos en adivinar.")
