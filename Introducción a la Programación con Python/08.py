def contar_divisores(n):
    contador_divisores = 0

    for i in range (1, n + 1):
        if n % i == 0:
            contador_divisores += 1
    return contador_divisores

def encontrar_divisores(n):

    for i in range (1, n + 1):
        while n % i == 0:
            return i

n = int(input('Introduzca un número entero mayor que cero: '))
if n <= 0:
    print('Usted no aprende, ¿VERDAD?')
else:
    print('El número ', n, 'tiene ', contar_divisores(n), 'divisores: ', encontrar_divisores(n))

#resolver como listar o mencionar los divisores SIN USAR LISTAS.
