horas = int(input('Ingrese las horas que tarda el corredor: '))
if horas <= 23 : hora_llegada = horas
else :  hora_llegada = horas % 24
print('Como el corredor tarda', horas, 'horas, llegará a las', hora_llegada, 'hs')
