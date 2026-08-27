s = float(input('Digite o valor do seu salario: '))

# Se o salário for maior que R$ 1250.00, o aumento é de 10%
if s > 1250.00:
    a = s + (s * 0.10)
# Para salários menores ou iguais a R$ 1250.00, o aumento é de 15%
else:
    a = s + (s * 0.15)

print(f'Após o aumento, seu salário é: R$ {a:.2f}')