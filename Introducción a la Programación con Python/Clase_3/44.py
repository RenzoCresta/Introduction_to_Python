import json


usuarios = json.loads(input())
email = input("Mail: ")
password = input("Contraseña: ")

if email in usuarios["usuarios"]:
  index = usuarios["usuarios"].index(email)
  if password == usuarios["contra"][index]:
    print("OK")
  else:
    print("NO")
else:
  print("DNE")
