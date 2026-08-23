# int() converte o texto retornado pelo input() em um número inteiro (int).
# Sem o int(), o Python trataria os valores como texto e juntaria os números em vez de somar.
n1 = int(input('Digite um numero: '))

# Recebe o segundo número digitado e também o converte para inteiro.
n2 = int(input('Digite outro numero: '))

# Realiza a operação matemática de adição entre os dois números inteiros.
soma = n1 + n2

# Exibe o resultado usando f-string, permitindo inserir as variáveis n1, n2 e soma diretamente dentro do texto.
print(f'A soma dos numeros {n1} e {n2} é {soma}')