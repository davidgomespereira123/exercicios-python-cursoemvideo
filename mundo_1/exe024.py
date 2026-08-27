# .strip() remove espaços extras no início e no final da resposta
nome = str(input('Em que cidade você nasceu?: ')).strip()

# nome[:5] pega as 5 primeiras letras da frase
# .upper() transforma essas letras em MAIÚSCULAS
# == 'SANTO' compara se o resultado é exatamente a palavra "SANTO" (retorna True ou False)
print(nome[:5].upper() == 'SANTO')