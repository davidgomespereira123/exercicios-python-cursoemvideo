import random
from time import sleep

# Lista principal para armazenar todos os palpites
jogos = []

print('-=' * 30)
print(f'{"JOGO DA MEGA SENA":^60}') 
print('-=' * 30)

# Define a quantidade total de jogos que o loop vai gerar
c = int(input('Quantos jogos você quer que eu sorteie? '))

# Preenche a lista 'jogos' com a quantidade pedida em 'c'
for _ in range(c):
    # Sorteia 6 números únicos entre 1 e 60, e sorted() os coloca em ordem crescente
    jogo = sorted(random.sample(range(1, 61), 6))
    jogos.append(jogo)

print('\n' + '-=' * 5, f' SORTEANDO {c} JOGOS ', '-=' * 5)

# Exibe cada jogo com a numeração iniciando em 1
for i, jogo in enumerate(jogos, start=1):
    print(f'Jogo {i}: {jogo}')
    sleep(0.5)  # Efeito visual de pausa a cada jogo impresso

print('-=' * 5, '< BOA SORTE! >', '-=' * 5)