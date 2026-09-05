time = list()
jogador = dict()
partidas = list()

while True:
    jogador.clear()
    partidas.clear()  # Limpa a lista para não acumular os gols do jogador anterior
    
    jogador['nome'] = str(input('Nome do jogador: '))
    tot = int(input(f'Quantas partidas o {jogador["nome"]} jogou? '))

    for c in range(0, tot):
        partidas.append(int(input(f'   Quantos gols na partida {c + 1}? ')))

    jogador['gols'] = partidas[:]    
    jogador['total'] = sum(partidas)
    time.append(jogador.copy())  # Salva a cópia do jogador na lista principal

    # Validação para continuar
    while True:
        resp = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if resp in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
    if resp == 'N':
        break

print('-=' * 30)    

# CABEÇALHO FORMATADO
# Em vez de ler as chaves do dicionário limpo, pegamos as chaves do primeiro jogador cadastrado
print(f'{"cod":<4}', end='')
for i in time[0].keys():
    print(f'{i:<15}', end='')
print()
print('-' * 50)

# EXIBIÇÃO DA TABELA
for k, v in enumerate(time):
    print(f'{k:<4}', end='')
    for d in v.values():
        print(f'{str(d):<15}', end='')
    print()
print('-' * 50)

# SISTEMA DE BUSCA INDIVIDUAL
while True:
    busca = int(input('Mostrar dados de qual jogador? (999 para parar): '))
    if busca == 999:
        break
    if busca >= len(time) or busca < 0:
        print(f'ERRO! Não existe jogador com código {busca}!')
    else:
        print(f' -- LEVANTAMENTO DO JOGADOR {time[busca]["nome"]}:')
        for i, g in enumerate(time[busca]['gols']):
            print(f'    No jogo {i + 1} fez {g} gols.')
    print('-' * 50)

print('<< VOLTE SEMPRE >>')