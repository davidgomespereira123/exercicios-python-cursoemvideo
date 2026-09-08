# 'def' define a função 'ficha' usando Parâmetros Opcionais (valores padrão)
# Se 'jog' não for passado, assume '<desconhecido>'. Se 'gol' não for passado, assume 0
def ficha(jog='<desconhecido>', gol=0):
    print(f'O jogador {jog} fez {gol} gol(s) no campeonato.')


# --- PROGRAMA PRINCIPAL ---

# Lê o nome do jogador e remove os espaços extras nas pontas (.strip())
n = str(input('Nome do Jogador: ')).strip()

# Lê a quantidade de gols como texto (str) para permitir validação antes de converter
g = str(input('Número de Gols: ')).strip()

# Verifica se o valor digitado nos gols contém apenas dígitos numéricos
if g.isnumeric():
    g = int(g)  # Converte o texto para número inteiro
else:
    g = 0       # Se o usuário digitou letras, caracteres especiais ou deixou vazio, assume 0

# Valida se o nome do jogador foi preenchido ou deixado em branco
if n == '':
    # Chama a função omitindo o nome (o Python usará o padrão '<desconhecido>') 
    # e passa explicitamente apenas a quantidade de gols
    ficha(gol=g)
else:
    # Chama a função enviando tanto o nome 'n' quanto os gols 'g'
    ficha(n, g)