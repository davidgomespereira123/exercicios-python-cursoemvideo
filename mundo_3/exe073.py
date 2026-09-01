# Tupla com os 20 times do Brasileirão
times = (
    'Palmeiras', 'Flamengo', 'Athletico-PR', 'Fluminense', 'Bahia',
    'Cruzeiro', 'Coritiba', 'Atlético-MG', 'Red Bull Bragantino', 'Corinthians',
    'São Paulo', 'Botafogo', 'Vitória', 'Santos', 'Grêmio',
    'Mirassol', 'Vasco da Gama', 'Internacional', 'Remo', 'Chapecoense'
)

# Exibe uma linha divisória visual
print('-=' * 15)

# Imprime a tupla completa com todos os 20 times
print(f'Lista de times do Brasileirão: {times}')

print('-=' * 15)

# Usa o fatiamento (slicing) [0:5] para pegar os elementos do índice 0 até o 4 (os 5 primeiros)
print(f'Os 5 primeiros são: {times[0:5]}')

print('-=' * 15)

# Usa o fatiamento com índice negativo [-4:] para buscar do antepenúltimo até o último elemento
print(f'Os 4 ultimos times sao: {times[-4:]}')

print('-=' * 15)

# A função sorted() organiza a tupla em ordem alfabética (retorna uma lista ordenada)
print(f'Times em ordem alfabetica são: {sorted(times)}')

print('-=' * 15)

# O método .index() descobre a posição (índice) da 'Chapecoense' na tupla.
# Adiciona-se +1 porque em Python a contagem de índices começa em 0.
print(f'O Chapecoense esta na {times.index("Chapecoense")+1}ª posição')