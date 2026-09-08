from time import sleep

# Definição de tupla com códigos de cores ANSI para formatação do terminal
c = (
    '\033[m',         # 0 - sem cor
    '\033[0;30;41m',  # 1 - vermelho
    '\033[0;30;42m',  # 2 - verde
    '\033[0;30;43m',  # 3 - amarelo
    '\033[0;30;44m',  # 4 - azul
    '\033[0;30;45m',  # 5 - roxo
    '\033[7;30m'      # 6 - branco invertido
)


def ajuda(com):
    """
    Exibe o manual interativo (docstring) de um comando ou biblioteca usando o help()
    """
    titulo(f'Acessando o manual do comando \'{com}\'', 4)
    print(c[6], end='')  # Aplica a cor branca invertida para a documentação
    help(com)
    print(c[0], end='')  # Reseta a cor original do terminal
    sleep(1)


def titulo(msg, cor=0):
    """
    Cria um cabeçalho personalizado com bordas ajustáveis e cores
    """
    tam = len(msg) + 4
    print(c[cor], end='')
    print('~' * tam)
    print(f'  {msg}')
    print('~' * tam)
    print(c[0], end='')  # Reseta a cor original
    sleep(0.5)


# --- PROGRAMA PRINCIPAL ---
comando = ''

while True:
    titulo('SISTEMA DE AJUDA PyHELP', 2)
    comando = str(input('Função ou Biblioteca > ')).strip()

    # Valida a palavra de parada
    if comando.upper() == 'FIM':
        break
    else:
        ajuda(comando)

titulo('ATÉ LOGO!', 1)