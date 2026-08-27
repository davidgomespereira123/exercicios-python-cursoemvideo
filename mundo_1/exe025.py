# .strip() remove os espaços desnecessários no início e no final do nome
nome = str(input('Qual e o seu nome completo?: ')).strip()

# nome.upper() transforma todo o nome para MAIÚSCULO
# 'SILVA' in ... verifica se a palavra "SILVA" existe em qualquer parte do texto (retorna True ou False)
print('Seu nome tem Silva? {}'.format('SILVA' in nome.upper()))