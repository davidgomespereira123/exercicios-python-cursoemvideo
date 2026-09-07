from time import sleep  # Importa a função sleep para pausar a execução por alguns segundos


def contador(inicio, fim, passo):
    # Trata o caso em que o usuário digita passo 0 (evita laço infinito)
    if passo == 0:
        passo = 1
    
    # Converte passo negativo em positivo para padronizar os cálculos
    if passo < 0:
        passo = abs(passo)

    print('-=' * 20)
    print(f'Contagem de {inicio} até {fim} de {passo} em {passo}:')
    sleep(0.5)

    # CASO 1: Contagem Crescente (Início menor que o Fim)
    if inicio < fim:
        cont = inicio
        while cont <= fim:
            # flush=True força o Python a mostrar o número na tela imediatamente sem esperar o laço terminar
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont += passo  # Avança somando o passo
        print('FIM!')
        
    # CASO 2: Contagem Regressiva (Início maior que o Fim)
    else:
        cont = inicio
        while cont >= fim:
            print(f'{cont} ', end='', flush=True)
            sleep(0.3)
            cont -= passo  # Recua subtraindo o passo
        print('FIM!')


# --- PROGRAMA PRINCIPAL ---

# a) Executa a contagem padrão de 1 a 10 de 1 em 1
contador(1, 10, 1)

# b) Executa a contagem regressiva padrão de 10 a 0 de 2 em 2
contador(10, 0, 2)

# c) Leitura de dados para contagem personalizada do usuário
print('-=' * 20)
print('Agora é sua vez de personalizar a contagem!')
ini = int(input('Início: '))
fim = int(input('Fim:    '))
pas = int(input('Passo:  '))

# Executa a função com os valores digitados pelo usuário
contador(ini, fim, pas)