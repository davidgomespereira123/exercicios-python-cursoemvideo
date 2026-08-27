# float() permite a leitura de distâncias com números decimais (ex: 150.5 km)
d = float(input('Digite a distancia em km da sua viagem: '))

# Viagens de até 200 km cobram R$ 0,50 por km
if d <= 200:
    print('O valor da passagem dessa viagem é: R$', d * 0.50)
# Viagens mais meias (acima de 200 km) cobram uma tarifa promocional de R$ 0,45 por km
else:
    print('O valor da passagem para essa viagem é: R$', d * 0.45)