co = float(input('Comprimento do cateto oposto: '))
ca = float(input('Comprimento do cateto adjacente: '))

# (co**2 + ca**2) eleva os catetos ao quadrado e soma
# ** (1/2) tira a raiz quadrada do resultado da soma
hi = (co**2 + ca**2) ** (1/2)

print(f'A hipotenusa vai medir {hi:.2f}')