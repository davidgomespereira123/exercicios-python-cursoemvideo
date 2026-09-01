# Tupla com a escrita por extenso dos números de 0 a 20.
# A posição de cada elemento (índice) é igual ao próprio número (ex: cont[0] é 'zero', cont[5] é 'cinco').
cont = ('zero', 'um', 'dois', 'três', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez',
        'onze', 'doze', 'treze', 'quatorze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

# Loop de validação: executa repetidamente até que o usuário digite um valor válido
while True:
    # Recebe a entrada do usuário pelo teclado e converte o texto para um número inteiro
    num = int(input('Digite um numero entre 0 e 20:'))
    
    # Condição de parada: verifica se o número está dentro do intervalo permitido (0 a 20)
    if 0 <= num <= 20:
        break  # Encerra o loop 'while' quando o valor for aceito
    
    # Exibido apenas se o número for inválido (< 0 ou > 20). 
    # O end='' faz o próximo input/print continuar na mesma linha.
    print('Tente novamente. ', end='')

# Exibe o resultado final buscando a palavra na tupla 'cont' usando o número como índice
print(f'Você digitou o numero {cont[num]}')