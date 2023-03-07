
hora = int(input(""))
#conversao de horas para segundos
hora_em_segundos = hora * 3600

minuto = int(input(""))
#conversao de minutos para segundos
minutos_em_segundos = minuto * 60

segundos = int(input(""))

total_de_segundos = hora_em_segundos + minutos_em_segundos + segundos

print(f'{total_de_segundos}')