from random import randint
from random import randint
from operator import itemgetter
from time import sleep

jogo = {
    'jogador 1': randint(1, 6),
    'jogador 2': randint(1, 6),
    'jogador 3': randint(1, 6),
    'jogador 4': randint(1, 6)
}

print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
    sleep(0.5)  # Efeito visual opcional para dar suspense

print('-=' * 20)

# sorted() ordena os itens pelo valor do dado (índice 1) do maior para o menor e retorna uma lista de tuplas
ranking = sorted(jogo.items(), key=itemgetter(1), reverse=True)

print('== RANKING DOS JOGADORES ==')
for i, v in enumerate(ranking):
    print(f'{i + 1}º lugar: {v[0]} com {v[1]}.')
    sleep(0.5)