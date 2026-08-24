# float() lê a temperatura aceitando valores decimais (ex: 36.5 ou -5.0)
c = float(input('Digite a temperatura em °C: '))

# Aplica a fórmula matemática de conversão: (C × 9/5) + 32
f = (c * 9 / 5) + 32

# Exibe o resultado formatado com 1 casa decimal (:.1f)
print(f'A temperatura de {c:.1f}°C corresponde a {f:.1f}°F!')