a = int(input('Ingrese un valor A: '))
b = int(input('Ingrese un valor B (mayor que A): '))

if a >= b:
    print('B debe ser mayor que A!')

else:
    while a <= b:
        print(a)
        a += 1
