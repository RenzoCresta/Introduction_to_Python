def buscar_precios(lista_precios, dinero):
  resultado = 0

  # Convertir la lista en un diccionario
  # Las claves serán los precios, los valores serán la cantidad de ocurrencias
  dict_precios = dict()

  # Iterar por todos los precios en la lista
  for p in lista_precios:
    # Agregar los elementos previos al diccionario
    dict_precios[p] = dict_precios.get(p, 0) + 1

    # Analizar si el dinero restante se encuentra en el dict y cuantas veces
    # Para evitar contar dos veces, chequeamos con los elementos anteriores
    restante = dinero - p
    if restante in dict_precios:
      resultado += dict_precios[restante]

  return resultado

print(buscar_precios( [1, 2, 3, 4, 5, 4] , 8))
print(buscar_precios( [7, 4, 2, 6, 7, 7] , 9))
print(buscar_precios( [4, 3, 7, 5] , 5))
