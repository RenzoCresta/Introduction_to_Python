n = int(input('Ingrese un número: '))

def es_primo(n) :
    for i in range(2, n) :
        if n % i == 0:
            print('No es primo')
            return False
        else:
            print('Es primo.')
            return True

print(es_primo(n))

#por qué si primero declaro el return y luego el print, sólo me devuelve el return?
