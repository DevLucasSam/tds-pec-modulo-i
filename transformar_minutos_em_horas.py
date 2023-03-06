#Recebe o valor em minutos
minutos = int(input(""))

#Divide de forma inteira,sem numeros decimais
tempo_em_horas = minutos // 60

#Guarda o resto da divisao
tempo_em_minutos = minutos % 60

#imprime na tela o resultado da conversao
print(f"{tempo_em_horas}h{tempo_em_minutos}min")