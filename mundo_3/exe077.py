# Tupla com várias palavras em formato de texto (strings)
palavras = ('aprender', 'programar', 'linguagem', 'python',
            'curso', 'gratis', 'estudar', 'praticar',
            'trabalhar', 'mercado', 'programador', 'futuro')

# Primeiro loop (externo): percorre cada palavra 'p' contida na tupla 'palavras'
for p in palavras: 
    # Imprime uma nova linha (\n) e exibe a palavra atual em maiúsculas (p.upper())
    # end='' evita a quebra de linha automática no final deste print
    print(f'\nNa palavra {p.upper()} temos ', end='')
    
    # Segundo loop (interno): percorre cada letra individual da palavra 'p' atual
    for letra in p:
        # Converte a letra para minúscula (.lower()) e verifica se ela é uma vogal ('a', 'e', 'i', 'o', 'u')
        if letra.lower() in 'aeiou':
            # Imprime a vogal encontrada seguida de um espaço na mesma linha
            print(letra, end=' ')