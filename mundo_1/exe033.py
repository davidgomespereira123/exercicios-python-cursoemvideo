n1 = int(input('Digite um numero: '))
n2 = int(input('Digite outro numero: '))

# Estrutura encadeada com `elif` e `else` evita verificações desnecessárias
if n1 > n2:
    print(f'O maior número é {n1} e o menor número é {n2}')
elif n2 > n1:
    print(f'O maior número é {n2} e o menor número é {n1}')
else:
    print('Os dois números são iguais')