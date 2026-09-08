# 'def' define a função personalizada 'notas'
# *n: empacotamento para receber N notas (tupla)
# sit=False: parâmetro opcional que define se a situação do aluno será exibida ou não
def notas(*n, sit=False):
    """
    -> Função para analisar notas e situações de vários alunos.
    :param n: uma ou mais notas dos alunos (aceita várias)
    :param sit: valor opcional, indicando se deve ou não adicionar a situação
    :return: dicionário com várias informações sobre a turma.
    """
    r = dict()
    
    # Preenche o dicionário com estatísticas usando funções embutidas do Python
    r['total'] = len(n)       # Quantidade de notas informadas
    r['maior'] = max(n)       # Maior nota
    r['menor'] = min(n)       # Menor nota
    r['média'] = sum(n) / len(n)  # Cálculo da média das notas

    # Adiciona o campo de situação se o usuário passar sit=True
    if sit:
        if r['média'] >= 7:
            r['situação'] = 'BOA'
        elif r['média'] >= 5:
            r['situação'] = 'RAZOÁVEL'
        else:
            r['situação'] = 'RUIM'

    # Retorna o dicionário populado com os dados
    return r


# --- PROGRAMA PRINCIPAL ---

# Chamada da função passando as notas e solicitando a exibição da situação (sit=True)
resp = notas(5.5, 2.5, 1.5, sit=True)

# Exibe o dicionário resultante
print(resp)

# Exemplo de docstring (ajuda da função)
# help(notas)