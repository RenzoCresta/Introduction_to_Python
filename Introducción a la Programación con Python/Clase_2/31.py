#codigo secreto

import random

def comparar_numeros(numero, numero_sugerido):
    respuesta = [0, 0]               # Primero mal ubicados, despues correctos

    aux_numero = ""
    aux_numero_sugerido = ""

    for i in range(len(numero)):
        # Agrego los correctos
        if numero[i] == numero_sugerido[i]:
            respuesta[1] += 1
        # Puede que el dígito esté mal ubicado
        else:
            aux_numero += numero[i]
            aux_numero_sugerido += numero_sugerido[i]

    for j in range(len(aux_numero)):
        if aux_numero_sugerido[j] in aux_numero:
            # Sumo un mal ubicado
            respuesta[0] += 1
            # Evito falsos positivos, reemplazando el número por otra cosa.
            aux_numero.replace(aux_numero_sugerido[j], "!", 1)

    return respuesta

numero_rand = str(random.randint(10000, 99999)) # Número aleatorio de 4 dígitos
intentos = 0
termino = False

# Explicación
print("Agente þ1ŧħ0n comunicándose.")
print("Entrego un número de 5 digitos y usted debe adivinarlo\
, un dígito a la vez.")
print("Te indicaré la cantidad de dígitos correctos y de mal ubicados.")
print("La comunicación finaliza cuando descubras el número.\n")
print("Escribe 'exit' cuando desees salir del juego.\n")

while termino == False:
  numero_us = input("Intenta adivinar el número: ")
  if numero_us == "exit":
    break
  while len(numero_us) != 5:
    numero_us = input("Debes ingresar un número de 5 dígitos: ")
  resultado = comparar_numeros(numero_rand, numero_us)
  intentos += 1

  print("Tienes " + str(resultado[0]) + " número(s) mal ubicado(s)\
 y " + str(resultado[1]) + " correcto(s).")

  if resultado[1] ==  5:
    termino = True
    print("Has adivinado luego de " + str(intentos) + " intentos.")
    break #redundant exit
  else:
    print("Intenta nuevamente.")
