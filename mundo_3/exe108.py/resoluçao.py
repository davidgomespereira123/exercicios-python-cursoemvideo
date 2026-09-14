import moeda

num = float(input('Digite o preço: R$ '))

print(f'A metade de {moeda.moeda(num)} é {moeda.moeda(moeda.metade(num))}')
print(f'O dobro de {moeda.moeda(num)} é {moeda.moeda(moeda.dobro(num))}')
print(f'Aumentando 10%, temos {moeda.moeda(moeda.aumento(num, 10))}')
print(f'Reduzindo 10%, temos {moeda.moeda(moeda.desconto(num, 10))}')