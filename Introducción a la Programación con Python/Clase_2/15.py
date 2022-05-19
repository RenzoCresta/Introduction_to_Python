#Ejercicio Integrador Número 2

palabra = input('Palabra a adivinar (escriba en mayúsculas): ')

contador = 0

while len(palabra) > 0:
    letra = input('Ingrese su intento: ')
    if letra in palabra :
        palabra = palabra.replace(letra, '')
        contador += 1
        print('Muy bien! Siga adivinando...')
    else :
        print('Incorrecto! Intente nuevamente...')
        contador += 1

print('Felicidades! Ha adivinado, la palabra era: ', palabra, 'y le ha tomado ', contador, 'intentos.')
