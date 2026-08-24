# float() lê o valor do salário aceitando centavos (ex: 1500.50)
s = float(input('Digite o valor do seu salario: '))

# Calcula o valor do aumento (15% do salário atual)
aumento = s * 15 / 100

# Exibe o salário final somando o valor do aumento (s + aumento)
# :.2f garante a exibição com 2 casas decimais no padrão de moeda
print(f'Seu salário com aumento de 15% é R$ {s + aumento:.2f}')