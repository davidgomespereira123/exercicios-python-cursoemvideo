# int() converte a entrada do usuário para um número inteiro
n = int(input('Digite um numero: '))

# O operador % (módulo) pega o resto da divisão por 2
# Se o resto for 0, o número é divisível por 2 (PAR)
if n % 2 == 0:
    print('O numero é PAR!')
# Se o resto for 1, o número não é divisível por 2 (ÍMPAR)
else:
    print('O numero é IMPAR!')