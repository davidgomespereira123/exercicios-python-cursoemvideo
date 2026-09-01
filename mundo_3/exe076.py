# Tupla intercalada contendo o nome do produto (texto) e o seu preço (número)
listagem = ('Lápis', 1.75,
            'Borracha', 2.00,
            'Caderno', 15.00,
            'Mochila', 100.00,
            'Caneta', 1.20)

# Percorre todos os índices numéricos da tupla (de 0 até o tamanho total da tupla - 1)
for pos in range(0, len(listagem)):
    # Se o índice é par (0, 2, 4, 6, 8...), significa que a posição guarda o NOME do produto
    if pos % 2 == 0:
        # :.<30 alinha o texto à esquerda (<) em um espaço de 30 caracteres e preenche o resto com pontos (.)
        # end='' evita a quebra de linha para que o preço saia na mesma linha
        print(f'{listagem[pos]:.<30}', end='')
    
    # Se o índice é ímpar (1, 3, 5, 7, 9...), a posição guarda o PREÇO do produto
    else:
        # :>7.2f alinha o valor à direita (>) em um campo de 7 caracteres com 2 casas decimais (.2f)
        print(f'R${listagem[pos]:>7.2f}')