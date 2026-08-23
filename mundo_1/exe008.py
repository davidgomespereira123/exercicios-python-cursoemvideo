# float() lê o valor digitado aceitando casas decimais (ex: 1.5)
v = float(input('Digite um valor em metros: '))

# Multiplica por 100 para converter metros em centímetros
cm = v * 100

# Multiplica por 1000 para converter metros em milímetros
mm = v * 1000

# Exibe o valor original e suas conversões na mesma linha
print(f'{v}m = {cm}cm = {mm}mm')