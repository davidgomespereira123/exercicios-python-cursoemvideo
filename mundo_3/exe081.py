# Cria uma lista vazia para armazenar os valores
lista = []

# Loop infinito para leitura contínua de números
while True:
    # Lê um número inteiro e adiciona ao final da lista
    n = int(input('Digite um valor: '))
    lista.append(n)

    # Pergunta se o usuário deseja continuar e trata o texto (.strip() e .upper())
    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    
    # Condição para encerrar o programa quando a resposta for 'N'
    if r == 'N':
        print('-=' * 20)
        
        # 1. Exibe a quantidade total de elementos cadastrados
        print(f'Você digitou {len(lista)} elementos.')
        
        # 2. Exibe a lista ordenada de forma decrescente (reverse=True)
        print(f'Os valores em ordem decrescente são {sorted(lista, reverse=True)}') 
        
        # 3. Verifica se o número 5 faz parte da lista
        if 5 in lista:
            # Usa lista.index(5) para achar o primeiro índice onde o 5 aparece
            print(f'O valor 5 faz parte da lista e foi encontrado na posição {lista.index(5)}!')
        else:
            print('O valor 5 não foi encontrado na lista!')    
        
        # Encerra o loop 'while'
        break