# la primer calificación debe representar un 20% del total, la segunda un 50% y la tercera un 30%.

a = int(input('Por favor ingrese la primer calificación: '))
b = int(input('Ingrese la segunda calificación: '))
c = int(input('Ingrese la tercer calificación: '))
coef_a = a * 0.2
coef_b = b * 0.5
coef_c = c * 0.3

def promedio_ponderado(coef_a, coef_b, coef_c) :
    nota_final = coef_a + coef_b + coef_c

    if 4 <= nota_final <= 10 :
        return 'Aprobado'
    else :
        return 'Reprobado'

if 1 < (a or b or c) <= 10 :
    print(promedio_ponderado(coef_a, coef_b, coef_c))
else :
    print('¡Error! Por favor, ingrese calificación válida.')
