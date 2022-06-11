# Uso una variable para contar los paréntesis que aún no se cerraron
 contador = 0
 for letra in texto:
   if letra == '(':
     contador += 1
   elif letra == ')':
     contador -= 1

   # Si se cierra un paréntesis que nunca se abrió entonces
   # no necesito continuar, retorno False y termina la función
   if contador < 0:
     return False

 # ¿Se cerró cada paréntesis que se abrió?
 return contador == 0

ans = esCorrecto( "Yo (Juan) quiero (necesito) café." )
print(ans)
ans = esCorrecto( " (1*(2+3) " )
print(ans)
ans = esCorrecto( " )(()) " )
print(ans)
ans = esCorrecto( " ( ) ) ( ( ) " )
print(ans)
