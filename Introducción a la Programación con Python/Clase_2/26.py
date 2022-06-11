#calculador derivadas

def derivada(x):
    return [x[i]-x[i-1] for i in range(1,len(x))]

z = [0, 1, 3, 6, 10, 15, 21, 22, 23, 10, 0]
d = derivada(z)
salto_pos = max(d)
salto_neg = min(d)

print("Derivada:", d)
print("El mayor salto positivo es de", salto_pos,
      "y ocurrió el día", d.index(salto_pos)+1)
print("El mayor salto negativo es de", salto_neg,
      "y ocurrió el día", d.index(salto_neg)+1)
