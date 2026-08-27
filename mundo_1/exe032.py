import datetime

# Lê o ano digitado pelo usuário
ano = int(input('Que ano quer analisar? Digite 0 para analisar o ano atual: '))

# Se o usuário digitar 0, pega o ano atual configurado no sistema
if ano == 0:
    ano = datetime.date.today().year

# Regra matemática do ano bissexto:
# 1. Deve ser divisível por 4 (ano % 4 == 0)
# 2. NÃO pode ser divisível por 100 (ano % 100 != 0)
# 3. EXCETO se for divisível por 400 (ano % 400 == 0)
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O ano {ano} é BISSEXTO!')
else:
    print(f'O ano {ano} NÃO é BISSEXTO!')