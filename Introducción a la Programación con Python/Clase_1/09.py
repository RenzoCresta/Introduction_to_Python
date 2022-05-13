numero = int(input('Ingrese un número: '))

def lothar(numero):
    contador_pasos = 0
    while numero > 1:
        contador_pasos += 1
        if numero % 2 == 0:
            numero //= 2
        else:
            numero = numero * 3 + 1

    return contador_pasos


print(lothar(numero))
