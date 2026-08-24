valor_dia = 60
valor_km = 0.15
km = float(input('Quantos km foram percorridos: '))
d = int(input('Quandos dias foram alugados: '))

total = d * valor_dia + km * valor_km
print(f'O total a pagar é R$ {total:.2f}')