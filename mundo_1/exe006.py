# Lê o número digitado e converte para número decimal (float)
n = float(input("Digite um número: "))

# Cálculos matemáticos
dobro = n * 2
triplo = n * 3
raiz = n ** 0.5  # Elevar a 0.5 é o mesmo que calcular a raiz quadrada

# Exibe os resultados
print(f"O dobro de {n} é {dobro}")
print(f"O triplo de {n} é {triplo}")
print(f"A raiz quadrada de {n} é {raiz:.2f}")  # :.2f limita para 2 casas decimais