espanolToChaos = {"ve":"regards", "bien":"bom", "se":"it"}
oracion = "se ve bien!"
whitespace = [" ", ".", ",", "!", "?"]

resultado = ""
palabra = ""
for i in range(0, len(oracion)):
    letra = oracion[i]
    if letra in whitespace: # reviso si la letra es una espacio en blanco
        if palabra != "":
            # traducir la palabra que tengo hasta ahora y agregarla
            resultado = resultado+espanolToChaos[palabra]

        resultado = resultado+letra # agrego el espacio a la palabra nueva
        palabra = ""
    else:
        palabra = palabra + letra

print(resultado)
