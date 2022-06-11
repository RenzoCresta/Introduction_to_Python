postulantes = {
    "Juan" : {"Español":True, "Ingles":True, "Chino":False,
              "Frances":False, "Italiano":True},
    "Pablo" : {"Español":False, "Ingles":True, "Chino":True,
               "Frances":False, "Italiano":True},
    "Carlos" : {"Español":True, "Ingles":False, "Chino":False,
                "Frances":True, "Italiano":True},
    "Ana" : {"Español":True, "Ingles":True, "Chino":True,
             "Frances":False, "Italiano":True},
    "Maria" : {"Español":False, "Ingles":True, "Chino":False,
               "Frances":False, "Italiano":True}
}

idioma = input("Ingrese un idioma: ")

for nombre, dicParticular in postulantes.items():
    if idioma in dicParticular and dicParticular[idioma] == True:
        print(nombre, 'habla', idioma)
