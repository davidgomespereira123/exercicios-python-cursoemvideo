aluno = dict()
nome = str(input('Nome:'))
media = float(input(f'Média de {nome}: '))
print('-=' * 30)
aluno['nome'] = nome
aluno['média'] = media
if media >= 7:
    aluno['situação'] = 'Aprovado'
else:
    aluno['situação'] = 'Reprovado'

for k, v in aluno.items():
    print(f'{k}: {v}')