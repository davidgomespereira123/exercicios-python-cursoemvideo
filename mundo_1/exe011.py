# float() lê o valor da altura aceitando casas decimais (ex: 2.75)
a = float(input('Digite a altura da parede: '))

# float() lê o valor da largura aceitando casas decimais (ex: 3.50)
l = float(input('Digite a largura da parede: '))

# Calcula a área da parede em metros quadrados (altura x largura)
area = a * l

# Exibe a área calculada formatada com 2 casas decimais (:.2f)
print(f'A área da parede é {area:.2f} m².')

# Cada litro de tinta pinta 2 m², então divide a área por 2 para saber a quantidade de tinta
print(f'Você precisará de {area / 2:.2f} litros de tinta.')