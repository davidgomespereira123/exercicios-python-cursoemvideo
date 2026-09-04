from random import randint
jogo = {'jogador 1': randint(1, 6),}
jogo['jogador 2'] = randint(1, 6)
jogo['jogador 3'] = randint(1, 6)
jogo['jogador 4'] = randint(1, 6)
print('Valores sorteados:')
for k, v in jogo.items():
    print(f'{k} tirou {v} no dado.')
print('-=' * 30)    
for i, v in enumerate(sorted(jogo.values(), reverse=True)):
    for k, j in jogo.items():
        if j == v:
            print(f'{i + 1}º lugar: {k} com {j}.')    