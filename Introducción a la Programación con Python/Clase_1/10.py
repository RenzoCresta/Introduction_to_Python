a = int(input('Por favor ingrese la primer calificación: '))
b = int(input('Ingrese la segunda calificación: '))
c = int(input('Ingrese la tercer calificación: '))

def calcular_promedio(a, b ,c):
    promedio = (a + b + c) / 3
    if 1 > (a and b and c) > 10 :
        return '¡Error! Por favor, ingrese calificación válida.'
    elif 4 <= promedio <= 10 :
        return 'Aprobado'
    else :
        return 'Reprobado'

print(calcular_promedio(a, b, c))
