jogador = dict()
jogador['nome'] = str(input('Nome do jogador: '))
partidas = int(input(f'Quantas partidas {jogador["nome"]} jogou? '))
for c in range(0, partidas):
    gols = jogador[f'partida {c + 1}'] = int(input(f'Quantos gols na partida {c + 1}? '))
print('-=' * 30)
print(f'O nome do jogador é {jogador["nome"]}.')    
print(f'Ele jogou {partidas} partidas.')
for k, v in jogador.items():
    if k != 'nome':
        print(f'Na {k} ele fez {v} gols.')
print(f'Foi um total de {sum(jogador.values())} gols.')        