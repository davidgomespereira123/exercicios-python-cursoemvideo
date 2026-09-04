# Declara a matriz 3x3 pré-preenchida com zeros
# Estrutura: matriz[linha][coluna]
matriz = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]

# 1. BLOCO DE LEITURA
# Loop externo 'c' controla o índice das LINHAS (0, 1 e 2)
for c in range(3):
    # Loop interno 'd' controla o índice das COLUNAS (0, 1 e 2)
    for d in range(3):
        # Substitui o valor '0' da posição [c][d] pelo número digitado pelo usuário
        matriz[c][d] = int(input(f'Digite um valor para [{c}, {d}]: '))

# 2. BLOCO DE EXIBIÇÃO FORMATADA
# Percorre novamente as linhas da matriz
for c in range(3):
    # Percorre as colunas da linha atual
    for d in range(3):
        # f'[{matriz[c][d]:^5}]' centraliza o número em um espaço de 5 caracteres.
        # end='' impede que o Python pule para a próxima linha a cada número impresso.
        print(f'[{matriz[c][d]:^5}]', end='')
    
    # print() vazio força a quebra de linha após imprimir os 3 elementos de uma linha
    print()