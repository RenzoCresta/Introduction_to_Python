cantidad = int(input("¿Cuántos nombres serán ingresados? "))
nombres = []

for i in range(cantidad):
  mensaje = "Ingrese el nombre #" + str(i + 1) + ": "
  nuevo_nombre = input(mensaje)
  nombres.append(nuevo_nombre)

nombres.sort()

print("Los nombres ingresados son: ")
for n in nombres:
  print(n)
