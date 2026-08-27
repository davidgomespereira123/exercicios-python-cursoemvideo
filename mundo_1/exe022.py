# .strip() elimina espaços inúteis antes do primeiro e depois do último nome
nome = str(input('Digite seu nome completo: ')).strip()

# .upper() converte todas as letras para maiúsculas
print('Seu nome em maiusculo é: {}'.format(nome.upper()))

# .lower() converte todas as letras para minúsculas
print('Seu nome em minusculo é: {}'.format(nome.lower()))

# len(nome) conta todos os caracteres. Subtraímos nome.count(' ') para não contar os espaços entre os nomes
print('Seu nome possui {} letras'.format(len(nome) - nome.count(' ')))

# .find(' ') descobre a posição do primeiro espaço, que bate exatamente com o tamanho do primeiro nome
print('Seu primeiro nome tem {} letras'.format(nome.find(' ')))