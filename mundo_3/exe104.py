# 'def' define a função personalizada 'leiaInt'
# O parâmetro 'msg' recebe o texto que será exibido no prompt do input
def leiaInt(msg):
    ok = False  # Variável de controle para indicar se um valor válido foi digitado
    valor = 0   # Guarda o número convertido final

    while True:
        # Lê a entrada do usuário como texto
        n = str(input(msg)).strip()

        # Verifica se o texto digitado consiste apenas em dígitos numéricos (positivos)
        if n.isnumeric():
            valor = int(n)  # Converte a string válida para número inteiro
            ok = True       # Atualiza a flag indicando que a validação passou
        else:
            # Exibe mensagem de erro em vermelho usando códigos de cores ANSI (\033[...m)
            print('\033[0;31mERRO! Digite um número inteiro válido.\033[m')

        # Se a validação foi bem-sucedida, sai do laço
        if ok:
            break

    # Retorna o número inteiro já validado e convertido para quem chamou a função
    return valor


# --- PROGRAMA PRINCIPAL ---

# O valor retornado por leiaInt() é armazenado diretamente na variável 'n'
n = leiaInt('Digite um número: ')
print(f'Você acabou de digitar o número {n}')