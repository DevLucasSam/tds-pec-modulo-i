# Lê o raio do usuário
PI = 3.141592
raio = float(input(""))
# Calcula o comprimento da circunferência
comprimento = 2 * PI * raio
print(f"{comprimento:.6f}")

# Calcula a área do círculo
area_circulo = PI * raio ** 2
print(f"{area_circulo:.6f}")

# Calcula a área da esfera
area_esfera = 4 * PI * raio ** 2
print(f"{area_esfera:.6f}")

# Calcula o volume da esfera
volume_esfera = 4/3 * PI * raio ** 3
print(f"{volume_esfera:.6f}")
