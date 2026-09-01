# Cria uma tupla 'n' lendo 4 números inteiros digitados pelo usuário.
# Os parenteses e as vírgulas ao redor das entradas formam a tupla diretamente.
n = (
    int(input('Digite um número: ')),
    int(input('Digite outro número: ')),
    int(input('Digite mais um número: ')),
    int(input('Digite o último número: '))
)

# Imprime a tupla completa com os 4 valores informados
print(f'Você digitou os valores {n}')

# O método .count(9) conta quantas vezes o número 9 está presente dentro da tupla 'n'
print(f'O número 9 apareceu {n.count(9)} vezes')

# O método .count(3) conta a quantidade total de aparições do número 3
print(f'O número 3 apareceu {n.count(3)} vezes')

# Verifica se o número 3 está presente na tupla para evitar erro (ValueError) na busca por índice
if 3 in n:
    # .index(3) encontra a PRIMEIRA posição (índice) onde o 3 aparece.
    # Somamos +1 porque a contagem no Python começa em 0.
    print(f'O número 3 apareceu na {n.index(3)+1}ª posição')
else:
    # Exibido apenas se o número 3 não tiver sido digitado nenhuma vez
    print('O número 3 não foi digitado em nenhuma posição')

# Exibe o texto de abertura para a lista de números pares (end='' evita a quebra de linha)
print('Os números pares digitados foram: ', end='')

# Percorre cada elemento 'num' da tupla 'n'
for num in n:
    # O operador % (módulo) calcula o resto da divisão por 2.
    # Se o resto for 0, o número é par.
    if num % 2 == 0:
        print(num, end=' ')  # Imprime o número par seguido de um espaço