#conversor temperatura

def CelciusToFarenheit(tempC):
    return tempC * 9 / 5 + 32

def CelciusToKelvin(tempC):
    return tempC + 273.15

temp = float(input("Ingrese temperatura en celcius: "))

if temp < -273.15:
  print("Advertencia: La temperatura es inferior al cero absoluto.")
else:
  print("Temperatura en Farenheit: ", CelciusToFarenheit(temp))
  print("Temperatura en Kelvin: ", CelciusToKelvin(temp))
