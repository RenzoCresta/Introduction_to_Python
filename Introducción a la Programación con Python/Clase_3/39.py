postulantes = {
    "Juan" : {"Español", "Ingles", "Italiano"} ,
    "Pablo" : {"Ingles", "Chino", "Italiano"},
    "Carlos" : {"Español", "Frances", "Italiano"},
    "Ana" : {"Español", "Ingles", "Chino", "Italiano"},
    "Maria" : {"Ingles", "Italiano"}
}

# Creamos un set con todos los idiomas
todos = {"Español", "Ingles", "Chino", "Frances", "Italiano"}

for p in postulantes:
  todos &= postulantes[p] # Es lo mismo que: todos = todos & postulantes[p]

print("Todos los candidatos aprendieron este(os) idioma(s):")
for i in todos:
  print(i)

# Creamos un set vacio
esp_ing = set()
for p in postulantes:
  if "Español" in postulantes[p] and "Ingles" in postulantes[p]:
    # Qué postulantes que saben ingles y español
    esp_ing.add(p)

print("Los candidatos que aprendieron al menos Español e Inglés:")
for i in esp_ing:
  print(i)
