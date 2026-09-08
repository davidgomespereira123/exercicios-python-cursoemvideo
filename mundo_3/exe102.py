def fatorial(n, show=True):
    """
    CALCULA O FATORIAL DE UM NÚMERO.
    :param n: O número a ser calculado.
    :param show: (opcional) Mostrar ou não a conta.
    :return: O valor do Fatorial de um número n.
    """
    f = 1
    for c in range(n, 0, -1):
        if show:
            print(c, end='')
            if c > 1:
                print(' x ', end='')
            else:
                print(' = ', end='')
        f *= c
    return f


# Exemplo 1: Mostrando o processo do cálculo (show=True por padrão)
print(fatorial(5))

# Exemplo 2: Ocultando o processo e trazendo apenas o resultado
print(fatorial(5, show=False))