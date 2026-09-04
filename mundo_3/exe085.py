# Cria uma lista composta com duas sublistas internas:
# valores[0] vai guardar os números pares
# valores[1] vai guardar os números ímpares
valores = [[], []]

# Loop 'for' para ler exatamente 7 números (c vai de 0 a 6)
for c in range(0, 7):
    # c + 1 ajusta a exibição para o usuário ver de 1º a 7º valor
    n = int(input(f'Digite o {c + 1}º valor: '))
    
    # Se o número for par (resto da divisão por 2 é 0)
    if n % 2 == 0:
        valores[0].append(n)  # Insere na primeira sublista (pares)
    else:
        valores[1].append(n)  # Insere na segunda sublista (ímpares)

# sorted(valores[0]) exibe a sublista de pares ordenada de forma crescente
print(f'Os valores pares digitados foram: {sorted(valores[0])}')

# sorted(valores[1]) exibe a sublista de ímpares ordenada de forma crescente
print(f'Os valores ímpares digitados foram: {sorted(valores[1])}')