pessoas = list()
pessoa = dict()
soma = 0

while True:
    pessoa.clear()
    pessoa['nome'] = str(input('Nome: '))
    
    # Validação do Sexo
    while True:
        pessoa['sexo'] = str(input('Sexo [M/F]: ')).strip().upper()[0]
        if pessoa['sexo'] in 'MF':
            break
        print('ERRO! Por favor, digite apenas M ou F.')

    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    pessoas.append(pessoa.copy())
    
    # Validação da Continuação
    while True:
        r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
        if r in 'SN':
            break
        print('ERRO! Responda apenas S ou N.')
        
    if r == 'N':
        break

print('-=' * 30)

# A) Total de pessoas
print(f'A) Ao todo temos {len(pessoas)} pessoas cadastradas.')

# B) Média de idade
media = soma / len(pessoas)
print(f'B) A média de idade é de {media:5.2f} anos.')

# C) Lista de mulheres
print('C) As mulheres cadastradas foram ', end='')
for p in pessoas:
    if p['sexo'] == 'F':
        print(f'{p["nome"]} ', end='')
print()

# D) Lista de pessoas com idade acima da média
print('D) Lista das pessoas que estão acima da média:')
for p in pessoas:
    if p['idade'] >= media:
        print('   ', end='')
        for k, v in p.items():
            print(f'{k} = {v}; ', end='')
        print()

print('<< ENCERRADO >>')