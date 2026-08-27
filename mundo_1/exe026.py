# .strip() remove espaços extras nas pontas e .upper() padroniza tudo para MAIÚSCULO
frase = str(input('Digite uma frase: ')).strip().upper()

# .count('A') conta quantas vezes a letra "A" aparece no texto
print('A letra A aparece {} na frase.'.format(frase.count('A')))

# .find('A') busca a PRIMEIRA ocorrência da letra "A" (da esquerda para a direita)
# O +1 ajusta o índice do Python (que começa em 0) para a contagem humana (que começa em 1)
print('A primeira letra A apareceu na posição {}'.format(frase.find('A')+1))

# .rfind('A') (right find) busca a ÚLTIMA ocorrência da letra "A" (da direita para a esquerda)
print('A ultima letra A apareceu na posição {}'.format(frase.rfind('A')+1))