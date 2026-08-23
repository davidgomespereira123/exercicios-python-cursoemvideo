# float() lê o valor em reais digitado pelo usuário (aceita casas decimais)
n = float(input('Digite quanto você tem na carteira em reais R$: '))

# Cotação comercial de referência do dólar em 23 de agosto de 2026 (R$ 5,14)
dolar = 5.14

# Exibe o valor convertido para dólares limitando o resultado a 2 casas decimais (:.2f)
print(f'Com R${n:.2f} você pode trocar por US${n / dolar:.2f} dólares (Cotação de 23/08/2026)')