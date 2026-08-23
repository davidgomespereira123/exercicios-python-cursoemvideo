# Lê o número inteiro digitado pelo usuário
num = int(input('Digite um número para ver sua tabuada: '))

# O laço for repete o código variando 'c' de 1 até 10
for c in range(1, 11):
    # :2d alinha os números de 1 dígito à direita na exibição
    print(f'{num} x {c:2d} = {num * c}')