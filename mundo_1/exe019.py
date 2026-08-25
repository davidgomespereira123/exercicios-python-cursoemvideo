import random

# str(input()) lê os nomes digitados pelo usuário como texto
n1 = str(input('primeiro aluno: '))
n2 = str(input('segundo aluno: '))
n3 = str(input('terceiro aluno: '))
n4 = str(input('quarto aluno: '))

# Cria uma lista [] contendo os 4 nomes lidos
lista = [n1, n2, n3, n4]

# random.choice() escolhe um item aleatório dentro da lista
escolhido = random.choice(lista)

# Exibe o resultado do sorteio
print('O aluno escolhido foi : ', escolhido)