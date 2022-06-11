#Locos por las matemáticas:

def factorial(n): # esto es una función recursiva
    if n <= 1:
        return 1
    else:
        return n * factorial(n - 1)

def piApprox(num):
    mul = 2**(3/2)/9801
    suma = 0
    for k in range(num):
        suma += factorial(4*k) /factorial(k)**4 *(1103+26390*k)/396**(4*k)
    return 1/(mul*suma)

print(piApprox(10))
