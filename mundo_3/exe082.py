# Cria a lista principal e duas listas auxiliares para pares e ímpares
lista = []
pares = []
impares = []

# Loop de leitura contínua
while True:
    n = int(input('Digite um valor: '))
    lista.append(n)
    
    # Separa o número na lista correspondente no momento da digitação
    if n % 2 == 0:
        pares.append(n)
    else:
        impares.append(n)

    r = str(input('Quer continuar? [S/N] ')).strip().upper()
    
    # Encerra o cadastro e exibe os resultados quando o usuário digita 'N'
    if r == 'N':
        print('-=' * 20)
        # len(lista) informa a quantidade total de elementos digitados
        print(f'Você digitou {len(lista)} elementos no total.')
        
        # Exibe a lista completa digitada
        print(f'A lista completa é: {lista}')
        
        # Exibe apenas a lista de pares ordenada de forma crescente
        print(f'Os valores pares digitados foram: {sorted(pares)}')
        
        # Exibe apenas a lista de ímpares ordenada de forma crescente
        print(f'Os valores ímpares digitados foram: {sorted(impares)}')
        
        break