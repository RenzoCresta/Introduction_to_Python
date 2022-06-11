#TRUCO
# Solución 1: diccionario

###Antes de hacer la funcion dueloDeCartas, creamos el diccionario que leerá para saber que carta gana

valorCarta = dict()

# casos especiales: esto no lo puedo hacer con un for
valorCarta["1 de espada"] = 14
valorCarta["1 de basto"] = 13
valorCarta["7 de espada"] = 12
valorCarta["7 de oro"] = 11

# el resto de los valores son de 10 para abajo
valor = 10
for x in [3, 2, 1, 12, 11, 10, 7, 6, 5, 4]:
    # itero por los numeros de las cartas, de la mas a la menos poderosa
    if x == 1: # con este if elijo que palos de este numero guardo
        palos = ["oro","copa"]
    elif x == 7:
        palos = ["basto", "copa"]
    else:
        palos = ["oro", "copa", "basto", "espada"]

    # para todos los palos que elegí, guardo la carta con el mismo valor
    for palo in palos:
        valorCarta[str(x) + " de " + palo] = valor

    valor -= 1 # la carta que viene es menos poderosa

def dueloDeCartas(cartaA, cartaB):
    # usamos el diccionario que creamos para saber el valor de las cartas
    # que nos pasan
    if valorCarta[cartaA] > valorCarta[cartaB]:
        return cartaA
    elif valorCarta[cartaA] < valorCarta[cartaB]:
        return cartaB
    else:
        return "empate"
