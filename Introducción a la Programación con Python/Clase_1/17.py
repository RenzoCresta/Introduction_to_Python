#Dominó
def cantidadFichas(n):
    print((n + 1) * (n + 2) // 2)

def mostrarFichas(n):
    for i in range(0, n + 1):
        for j in range(i, n + 1):
            print(str(i) + '-' + str(j))

def valorMaximo(num):
    n = 1
    while (n + 1) * (n + 2) / 2 < num:
        n += 1
    if (n + 1) * (n + 2) / 2 == num:
        print(n)
    else:
        print(-1)

# Probamos con distintos casos las tres funciones

print("CantidadFichas(3)")
cantidadFichas(3)

print("CantidadFichas(4)")
cantidadFichas(4)

print("mostrarFichas(3)")
mostrarFichas(3)

print("ValorMaximo(10)")
valorMaximo(10)

print("ValorMaximo(11)")
valorMaximo(11)

print("ValorMaximo(15)")
valorMaximo(15)
