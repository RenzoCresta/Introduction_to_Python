#Calculador de integrales:

def f1(x):
  return 1

def f2(x):
  return x

def f3(x):
  return x**2 - 3*x

def integral(f, a, b, dx):
  resultado = 0
  x = a
  while (x + dx) <= b:
    resultado += f(x) * dx
    x += dx
  return resultado

print( integral(f1, 10, 15, 0.0001) )
print( integral(f2, 1, 2, 0.0001) )
print( integral(f3, 0, 3, 0.0001) )
