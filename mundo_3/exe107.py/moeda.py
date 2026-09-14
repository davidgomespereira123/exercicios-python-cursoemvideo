def aumento(preço, taxa):
    res = preço + (preço * taxa/100)
    return res


def desconto(preço, taxa):
    res = preço - (preço * taxa/100)
    return res


def dobro(preço):
    res = preço * 2
    return res


def metade(preço):
    res = preço / 2
    return res
    