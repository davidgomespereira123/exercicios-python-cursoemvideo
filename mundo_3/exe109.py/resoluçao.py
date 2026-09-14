import moeda

num = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda.moeda(num)} é {moeda.metade(num, True)}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.dobro(num, True)}')
print(f'Aumentando 10%, temos {moeda.aumento(num, 10, True)}')
print(f'Reduzindo 15%, temos {moeda.desconto(num, 15, True)}')