n = str(input('Digite seu nome completo: ')).strip()
nome = n.split()

# Adicionadas as chaves {} que faltavam
print('Seu primeiro nome é: {}'.format(nome[0]))

# Corrigido de .fromat() para .format()
print('Seu último nome é: {}'.format(nome[len(nome)-1]))