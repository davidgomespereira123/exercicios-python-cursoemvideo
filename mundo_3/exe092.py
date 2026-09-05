from datetime import date

dados = dict()
dados['nome'] = str(input('Nome: '))
ano_nascimento = int(input('Ano de nascimento: '))
dados['idade'] = date.today().year - ano_nascimento
dados['ctps'] = int(input('Carteira de trabalho (0 não tem): '))

if dados['ctps'] != 0:
    dados['contratacao'] = int(input('Ano de contratação: '))
    dados['salario'] = float(input('Salário: R$ '))
    # Idade na aposentadoria = idade atual + quantos anos faltam para completar 35 de contribuição
    dados['aposentadoria'] = dados['idade'] + ((dados['contratacao'] + 35) - date.today().year)

print('-=' * 20)

# O loop fica fora do IF para imprimir os dados com ou sem CTPS
for k, v in dados.items(): 
    print(f'  - {k} tem o valor {v}')