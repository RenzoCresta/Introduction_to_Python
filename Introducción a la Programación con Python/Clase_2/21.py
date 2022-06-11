nombre = input("Ingrese el nombre: ")
apellido = input("Ingrese el apellido: ")

nombre_y_apellido = nombre + " " + apellido

# El largo es mayor a 26?
if len(nombre_y_apellido) > 26:
  nombre_y_apellido = nombre[0] + " " + apellido

  # El largo todavia es mayor a 26?
  if len(nombre_y_apellido) > 26:
    nombre_y_apellido = nombre[0] + " " + apellido[:24]

print(nombre_y_apellido)
