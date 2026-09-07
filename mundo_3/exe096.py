# 'def' define uma função personalizada chamada 'area'
# 'larg' e 'comp' são os parâmetros que receberão os valores enviados
def area(larg, comp):
    # Calcula a área multiplicando largura por comprimento
    a = larg * comp
    
    # Exibe a largura e o comprimento informados
    print(f'A largura do terreno é {larg}m e o comprimento é {comp}m.')
    
    # Exibe o resultado da área formatado com 2 casas decimais (:.2f)
    print(f'A área total do terreno é de {a:.2f}m².')


# --- PROGRAMA PRINCIPAL ---

# Imprime o título e uma linha divisória
print('  Controle de Terrenos')
print('-' * 25)

# Pede ao usuário os valores do terreno e converte a resposta para número decimal (float)
l = float(input('LARGURA (m): '))
c = float(input('COMPRIMENTO (m): '))

# Chama a função 'area' enviando os valores guardados nas variáveis 'l' e 'c'
area(l, c)