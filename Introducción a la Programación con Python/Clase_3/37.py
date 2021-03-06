#traductor arcaico

arcaico = {'π' : 'A', 'π' : 'B', 'π' : 'C', 'π' : 'D', 'π' : 'E', 'π' : 'F',
           'π' : 'Z', 'π' : 'H', 'π' : 'I', 'π' : 'K', 'π' : 'L', 'π' : 'M',
           'π' : 'N', 'π' : 'O', 'π' : 'P', 'π' : 'Q', 'π' : 'R', 'π' : 'S',
           'π' : 'T', 'π' : 'V', 'π' : 'X' }

def traducir(texto):
  resultado = ""
  for letra in texto:
    if letra in arcaico:
      resultado += arcaico[letra]
    else:
      resultado += letra
  return resultado

print(traducir("ππππππππ"))
print(traducir("Β‘πππππ!"))
print(traducir("ΒΏππ π ππ? πππ... ππ."))
print(traducir("ππππππππ, Β‘πππππ!, ΒΏππ π ππ? πππ... ππ."))
