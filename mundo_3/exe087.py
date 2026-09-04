# Declara a matriz 3x3 pré-preenchida com zeros
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# Lista para armazenar apenas os NUMEROS PARES digitados
par = []

# 1. BLOCO DE LEITURA
for c in range(3):
    for d in range(3):
        # Lê o valor digitado pelo usuário
        matriz[c][d] = int(input(f'Digite um valor para [{c}, {d}]: '))

print('-=' * 20)

# 2. BLOCO DE EXIBIÇÃO FORMATADA E ANÁLISE DOS PARES
for c in range(3):
    for d in range(3):
        # Imprime o valor centralizado com 5 espaços
        print(f'[{matriz[c][d]:^5}]', end='')
        
        # Testa se O VALOR inserido na matriz é par (e não o índice c ou d)
        if matriz[c][d] % 2 == 0:
            par.append(matriz[c][d])
            
    # Quebra de linha a cada 3 colunas exibidas
    print()

print('-=' * 20)    

# A) Soma todos os valores pares armazenados na lista 'par'
print(f'A soma de todos os valores pares digitados é {sum(par)}')

# B) Soma os elementos da 3ª coluna (índice [2] fixo nas 3 linhas)
soma_coluna_3 = matriz[0][2] + matriz[1][2] + matriz[2][2]
print(f'A soma dos valores da terceira coluna é {soma_coluna_3}')

# C) max(matriz[1]) extrai o maior elemento contido na 2ª linha (índice 1)
print(f'O maior valor da segunda linha é {max(matriz[1])}')