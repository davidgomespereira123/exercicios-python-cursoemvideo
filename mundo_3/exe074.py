# Importa a função 'randint' da biblioteca 'random' para gerar números inteiros aleatórios
from random import randint

# Gera uma tupla 'n' com 5 números aleatórios, cada um variando de 1 a 10.
# As vírgulas entre as chamadas do randint() é o que definem a criação de uma tupla.
n = (randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10), randint(1, 10))

# Imprime a tupla completa contendo todos os números sorteados
print(f'Eu sorteei os valores {n}')

# A função embutida max() analisa a tupla e retorna o maior valor numérico encontrado nela
print(f'O maior valor sorteado foi {max(n)}')

# A função embutida min() analisa a tupla e retorna o menor valor numérico encontrado nela
print(f'O menor valor sorteado foi {min(n)}')