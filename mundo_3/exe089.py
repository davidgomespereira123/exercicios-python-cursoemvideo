# Estrutura com 3 sublistas: [0] Nomes, [1] Nota 1, [2] Nota 2
aluno = [[], [], []]

# 1. BLOCO DE CADASTRO
while True:
    nome = str(input('Nome: '))
    nota1 = float(input('Nota 1: '))
    nota2 = float(input('Nota 2: '))
    
    aluno[0].append(nome)
    aluno[1].append(nota1)
    aluno[2].append(nota2)
    
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    if r == 'N':
        break

print('-=' * 30)

# 2. BLOCO DE EXIBIÇÃO DO BOLETIM
# Calcula as médias de todos os alunos cadastrados
media = [(aluno[1][i] + aluno[2][i]) / 2 for i in range(len(aluno[0]))]

# Cabeçalho formatado com alinhamento correto
print(f'{"No.":<4}{"NOME":<10}{"MÉDIA":>8}')
print('-' * 26)

# Exibe o índice real (i) para bater com a busca posterior
for i, nome in enumerate(aluno[0]):
    print(f'{i:<4}{nome:<10}{media[i]:>8.1f}')

print('-' * 26)

# 3. BLOCO DE CONSULTA INDIVIDUAL
while True:
    opc = int(input('Mostrar notas de qual aluno? (999 interrompe): '))
    
    if opc == 999:
        print('FINALIZANDO...')
        break
        
    # Valida se o índice informado existe na lista de alunos
    if opc < len(aluno[0]) and opc >= 0:
        print(f'Notas de {aluno[0][opc]} são [{aluno[1][opc]}, {aluno[2][opc]}]')
        print('-' * 35)
    else:
        print(f'ERRO! Não existe aluno com o código {opc}. Tente novamente.')