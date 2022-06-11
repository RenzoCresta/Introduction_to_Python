
n = int(input("Cantidad de votos: "))

contador = {}
votos_totales = 0


while votos_totales < n :
        candidato = input("Candidato a votar: ")
        votos_totales += 1
        if not candidato in contador :
            contador[candidato] = 1
        else :
            contador[candidato] = contador[candidato] + 1

ganador = max(contador, key=contador.get)

print(ganador)
