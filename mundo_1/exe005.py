# input() lê o número digitado e int() o converte de texto para número inteiro
n = int(input('Digite um numero: '))

# Soma 1 ao número digitado para descobrir o próximo número
sucessor = n + 1

# Subtrai 1 do número digitado para descobrir o número anterior
antecessor = n - 1

# f"..." insere os valores das variáveis diretamente dentro do texto para exibir o resultado
print(f"O sucessor de {n} e {sucessor} e o antecessor e {antecessor}.")