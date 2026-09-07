from random import randint  # Importa a função para gerar números inteiros aleatórios
from time import sleep      # Importa a função para pausar a execução por alguns segundos


# FUNÇÃO 1: Sorteia 5 números e insere na lista passada como argumento
def sorteia(lista):
    print('Sorteando 5 valores da lista: ', end='', flush=True)
    
    # O laço roda exatamente 5 vezes
    for _ in range(5):
        num = randint(1, 10)   # Sorteia um número de 1 a 10
        lista.append(num)      # Adiciona o número sorteado no final da lista
        print(f'{num} ', end='', flush=True) # Exibe o número na tela imediatamente
        sleep(0.3)             # Pausa de 0.3 segundos para dar efeito visual
        
    print('PRONTO!')


# FUNÇÃO 2: Soma apenas os números pares da lista recebida
def somaPar(lista):
    soma = 0
    # Percorre cada elemento contido na lista
    for valor in lista:
        if valor % 2 == 0:     # Verifica se o resto da divisão por 2 é zero (se é par)
            soma += valor      # Acumula o valor par na variável 'soma'
            
    print(f'Somando os valores pares de {lista}, temos {soma}.')


# --- PROGRAMA PRINCIPAL ---

numeros = []        # Cria uma lista vazia

sorteia(numeros)    # Passa a lista vazia para a função preencher com 5 números
somaPar(numeros)    # Passa a lista preenchida para calcular a soma dos pares