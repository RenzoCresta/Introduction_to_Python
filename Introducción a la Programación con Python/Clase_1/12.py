# e = 1/0! + 1/1! + 1/2! + 1/3! + ...

import math

n = int(input('Ingrese número de términos: '))

def euler(n) :
    e = 0
    for i in range (n) :
        term = 1/math.factorial(i)
        e += term
    return e

if n > 0 :
    print(euler(n))
else :
    print('Ingrese un número válido')
