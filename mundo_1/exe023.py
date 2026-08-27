# int() lê o valor digitado e converte para número inteiro
num = int(input('Digite um numero: '))

# A divisão inteira (//) remove as casas à direita e o resto da divisão (% 10) pega o último dígito restante
n1 = num // 1 % 10    # Pega a Unidade
n2 = num // 10 % 10   # Pega a Dezena
n3 = num // 100 % 10  # Pega a Centena
n4 = num // 1000 % 10 # Pega o Milhar

print('Analisando numero {}'.format(num))
print('Unidade:{}'.format(n1))
print('Dezena:{}'.format(n2))
print('Centena:{}'.format(n3))
print('Milhar:{}'.format(n4))