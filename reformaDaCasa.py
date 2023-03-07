#escreva um programa que leia 3 números correspondendo ao valor da altura, comprimento e largura da sala em metros
# e em seguida imprima: Área do piso da sala: largura * comprimento Volume da sala: largura * comprimento * altura
# Área das paredes da sala: 2 * altura * largura + 2 * altura * comprimento
altura = int(input("Digite a altura da parede:"))
comprimento = int(input("Digite o cumprimento da sala:"))
largura = int(input("Digite a largura da sala:"))

area_do_piso = largura * comprimento
print(f"A área do piso é de: {area_do_piso} metros²")

volume_da_sala = largura * comprimento * altura
print(f'O volume da sala é: {volume_da_sala} metros³')
# 2 * altura * largura + 2 * altura * comprimento
area_das_paredes = (2 * altura * largura) + (2 * altura * comprimento)
print(f'A área das paredes é: {area_das_paredes} metros²')