import math
#Lê o raio
raio = float(input(""))

#metodo para usar o pi ate a sexta casa
piArredondado = round(math.pi,4)


#calcula o comprimento da circunferência
comprimento = 2 * piArredondado * raio
print(f"{comprimento:.6f}")

#calcula a área do círculo
areaDoCirculo = piArredondado * raio **2
print(f'{areaDoCirculo:.6f}')

#calcula a área da esfera
areaDaEsfera = 4 * piArredondado * raio **2
print(f"{areaDaEsfera:.6f}")

# calcula o volume da esfera
volumeDaEsfera = 4/3 * piArredondado * raio **3
print(f"{volumeDaEsfera:.6f}")
