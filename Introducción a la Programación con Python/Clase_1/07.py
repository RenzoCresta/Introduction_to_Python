user = input('Usuario: ')
password = input('Contraseña: ')

def account_check(user, password):
    if (user == 'Juan' and password == '12345_') or (user == 'Pablo' and password == xDcFvGbHn):
        return 'True'
    else:
        return 'False'
print(account_check(user, password))
