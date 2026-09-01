# Lê a expressão digitada pelo usuário como uma string
expr = str(input('Digite a expressão: '))

# Lista que funcionará como uma pilha de parênteses
pilha = []

# Percorre cada caractere da string 'expr'
for simb in expr:
    # Se o caractere for um parêntese de abertura, adiciona à pilha
    if simb == '(':
        pilha.append('(')
    
    # Se o caractere for um parêntese de fechamento
    elif simb == ')':
        # Se a pilha não estiver vazia, remove o último '(' correspondente
        if len(pilha) > 0:
            pilha.pop()
        # Se a pilha estiver vazia, significa que há um ')' sem um '(' anterior
        else:
            pilha.append(')')
            break

# Se a pilha terminar vazia, todos os parênteses foram abertos e fechados corretamente
if len(pilha) == 0:
    print('Sua expressão está válida!')
else:
    print('Sua expressão está errada!')