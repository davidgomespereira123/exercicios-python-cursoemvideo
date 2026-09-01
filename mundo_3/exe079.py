# Cria uma lista vazia para armazenar os números digitados
n = []

# Loop infinito para leitura de dados
while True:
    # Solicita um número inteiro ao usuário
    valor = int(input('Digite um valor: '))
    
    # Verifica se o valor informado já foi cadastrado na lista
    if valor in n:
        # Mensagem exibida caso o número seja repetido
        print('Valor duplicado! Não será adicionado...')
    else:
        # Adiciona o número ao final da lista apenas se for inédito
        n.append(valor)
        # Mensagem de confirmação (agora só exibe se o valor realmente for inserido)
        print('Valor adicionado com sucesso...')
    
    # Pergunta ao usuário se deseja continuar cadastrando valores
    # .strip() remove espaços extras e .upper() converte o texto para maiúsculo
    resposta = str(input('Quer continuar? [S/N] ')).strip().upper()
    
    # Encerra o loop caso a resposta comece ou seja igual a 'N'
    if resposta == 'N':
        break

# sorted(n) retorna uma cópia da lista com os elementos ordenados do menor para o maior
print(f'Você digitou os valores {sorted(n)}')