# Cria uma lista 'n' utilizando list comprehension. 
# O loop 'for' executa 5 vezes (de 0 a 4), solicitando um número por vez e convertendo para inteiro.
n = [int(input('Digite um valor: ')) for c in range(0, 5)]

# Imprime a lista completa com os 5 valores digitados
print(f'Você digitou os valores {n}')

# max(n) encontra o maior valor da lista.
# n.index(max(n)) localiza a primeira posição (índice) onde esse maior valor está.
# Adiciona-se +1 para mostrar a posição humana (1ª, 2ª...) em vez do índice do Python (que começa em 0).
print(f'O maior valor digitado foi {max(n)} na posição {n.index(max(n))+1}')

# min(n) encontra o menor valor da lista.
# n.index(min(n)) localiza o índice do menor valor, e o +1 ajusta para a contagem a partir de 1.
print(f'O menor valor digitado foi {min(n)} na posição {n.index(min(n))+1}')