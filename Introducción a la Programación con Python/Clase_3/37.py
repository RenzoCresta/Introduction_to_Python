#traductor arcaico

arcaico = {'𐌀' : 'A', '𐌁' : 'B', '𐌂' : 'C', '𐌃' : 'D', '𐌄' : 'E', '𐌅' : 'F',
           '𐌆' : 'Z', '𐌇' : 'H', '𐌉' : 'I', '𐌊' : 'K', '𐌋' : 'L', '𐌌' : 'M',
           '𐌍' : 'N', '𐌏' : 'O', '𐌐' : 'P', '𐌒' : 'Q', '𐌓' : 'R', '𐌔' : 'S',
           '𐌕' : 'T', '𐌖' : 'V', '𐌗' : 'X' }

def traducir(texto):
  resultado = ""
  for letra in texto:
    if letra in arcaico:
      resultado += arcaico[letra]
    else:
      resultado += letra
  return resultado

print(traducir("𐌀𐌋𐌅𐌀𐌁𐌄𐌕𐌏"))
print(traducir("¡𐌐𐌄𐌓𐌃𐌉!"))
print(traducir("¿𐌔𐌉 𐌏 𐌍𐌏? 𐌌𐌌𐌌... 𐌔𐌉."))
print(traducir("𐌀𐌋𐌅𐌀𐌁𐌄𐌕𐌏, ¡𐌐𐌄𐌓𐌃𐌉!, ¿𐌔𐌉 𐌏 𐌍𐌏? 𐌌𐌌𐌌... 𐌔𐌉."))
