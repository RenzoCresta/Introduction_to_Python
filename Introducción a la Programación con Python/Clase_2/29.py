#las naranjas de Miguel

def leerPedido(pedido):
    naranjas = 0
    bananas = 0
    for letra in pedido:
        if letra == "N":
            naranjas += 1
        else:
            bananas += 1
    return naranjas, bananas

def cuantasDar(naranjas, bananas):
    naranjasParaHermana = 0
    bananasParaHermana = 0
    if naranjas < 2:
        naranjasParaHermana = 0
    else:
        naranjasParaHermana = 1

    if bananas > 1:
        bananasParaHermana = 2
    else:
        bananasParaHermana = bananas

    return naranjasParaHermana, bananasParaHermana

# Genero pedidos aleatorios. Puede hacerse a mano igualmente.
P = "B" * randint(0, 10) + "N" * randint(0, 10)

n, b = leerPedido(P) # Leo pedido y guardo a memoria las frutas que tengo
nh, bh = cuantasDar(n, b) # Aqui calculo naranjas para darle a la hermana

print("Bienvenido Miguel. Tu cosecha fue: ", P,
      ". Hoy te quedaron ",n - nh," Naranja(s) y ",
      b - bh," banana(s).", sep="")
