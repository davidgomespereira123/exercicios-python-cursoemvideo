# Cria uma lista vazia para armazenar os valores em ordem
lista = []

# Loop para solicitar 5 números ao usuário
for c in range(0, 5):
    n = int(input('Digite um valor: '))
    
    # 1º Caso: Se for o primeiro elemento OU se o número for maior que o último da lista
    if c == 0 or n > lista[-1]:
        lista.append(n)
        print('Adicionado ao final da lista...')
    else:
        # 2º Caso: Procura a posição correta de inserção percorrendo a lista existente
        pos = 0
        while pos < len(lista):
            # Se o valor digitado for menor ou igual ao elemento da posição atual
            if n <= lista[pos]:
                lista.insert(pos, n)  # Insere o número na posição exata 'pos'
                print(f'Adicionado na posição {pos} da lista...')
                break  # Para o loop while assim que inserir o número
            pos += 1

print('-=' * 30)
# Exibe a lista final já totalmente ordenada
print(f'Os valores digitados em ordem foram {lista}')