# float() lê o valor do produto aceitando casas decimais (ex: 49.90)
v = float(input('Digite o valor do produto: '))

# Calcula o valor do desconto (5% do valor total)
desconto = v * 5 / 100

# Exibe o valor original e o preço final após subtrair o desconto (v - desconto)
# :.2f garante a exibição com 2 casas decimais no padrão de moeda
print(f'O produto custa R${v:.2f} com 5% de desconto fica por R${v - desconto:.2f}')