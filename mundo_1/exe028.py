from random import randint

# O computador gera um número inteiro aleatório entre 0 e 5
computador = randint(0, 5)

print('-=-' * 20)
print('Vou pensar em um número de 0 a 5. Tente adivinhar...')
print('-=-' * 20)

jogador = int(input('Em que número eu pensei?: '))

# Estrutura condicional (if / else) para verificar o acerto
if jogador == computador:
    print('PARABÉNS! Você conseguiu me vencer!')
else:
    print(f'GANHEI! Eu pensei no número {computador} e não no {jogador}!')