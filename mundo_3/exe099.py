from time import sleep  # Importa a função sleep para pausar a execução


# O *num é o empacotamento de parâmetros: permite receber N números em forma de tupla
def maior(*num):
    cont = maior_valor = 0
    print('-=' * 20)
    print('Analisando os valores passados...')
    
    # Percorre cada valor recebido no empacotamento 'num'
    for valor in num:
        print(f'{valor} ', end='', flush=True)  # Exibe os números um a um sem quebrar a linha
        sleep(0.3)
        
        # Na primeira iteração (cont == 0), o primeiro número é definido como o maior
        if cont == 0:
            maior_valor = valor
        else:
            # Nas iterações seguintes, atualiza o maior_valor se encontrar um número superior
            if valor > maior_valor:
                maior_valor = valor
        cont += 1  # Incrementa o contador de números lidos
        
    # Exibe a quantidade total de números recebidos e qual foi o maior
    print(f'\nForam informados {cont} valores ao todo.')
    print(f'O maior valor informado foi {maior_valor}.')


# --- PROGRAMA PRINCIPAL ---
# Testes da função com diferentes quantidades de argumentos

maior(2, 9, 4, 5, 7, 1)  # 6 valores
maior(4, 7, 0)           # 3 valores
maior(1, 2)              # 2 valores
maior(6)                 # 1 valor
maior()                  # 0 valores (trabalha com a tupla vazia)