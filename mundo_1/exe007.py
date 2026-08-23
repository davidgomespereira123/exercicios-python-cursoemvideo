# float() lê o valor com casas decimais (ex: 7.5)
nt1 = float(input('Digite a primeira nota: '))
nt2 = float(input('Digite a segunda nota: '))

# Os parênteses são obrigatórios para somar as notas antes de dividir por 2
media = (nt1 + nt2) / 2

# :.1f formata o resultado para mostrar apenas 1 casa decimal após a vírgula
print(f'A média do aluno é {media:.1f}.')