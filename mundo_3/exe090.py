aluno = dict()
aluno['nome'] = str(input('Nome: '))
aluno['média'] = float(input(f'Média de {aluno["nome"]}: '))

# Lógica de situação com recuperação
if aluno['média'] >= 7.0:
    aluno['situação'] = 'Aprovado'
elif 5.0 <= aluno['média'] < 7.0:
    aluno['situação'] = 'Recuperação'
else:
    aluno['situação'] = 'Reprovado'

print('-=' * 20)

# Exibição formatada
for chave, valor in aluno.items():
    print(f'  - {chave.capitalize()} é igual a {valor}')