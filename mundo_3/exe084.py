# Lista principal que vai guardar todas as pessoas cadastradas (lista de listas)
pessoas = []
# Lista temporária para armazenar os dados de UMA pessoa (nome e peso)
pessoa = []

# Loop de repetição infinito para cadastro de dados
while True:
    # 1. Lê o nome e adiciona na 1ª posição (índice 0) da lista temporária
    pessoa.append(str(input('Nome: ')))
    
    # 2. Lê o peso e adiciona na 2ª posição (índice 1) da lista temporária
    pessoa.append(float(input('Peso: ')))
    
    # 3. Lê a resposta, remove espaços (.strip()), converte para maiúscula (.upper())
    # e pega apenas a primeira letra ([0])
    r = str(input('Quer continuar? [S/N] ')).strip().upper()[0]
    
    # 4. pessoas.append(pessoa[:]) insere uma CÓPIA [:] da lista temporária dentro de 'pessoas'.
    # Isso evita que as alterações futuras apaguem os dados já inseridos.
    pessoas.append(pessoa[:])
    
    # 5. Limpa a lista temporária para deixá-la pronta para o próximo cadastro
    pessoa.clear()
    
    # Se a resposta digitada for 'N', executa o bloco de encerramento do programa
    if r == 'N':
        
        # Exibe a quantidade total de cadastros realizados usando o tamanho da lista (len)
        print(f'Foram cadastradas {len(pessoas)} pessoas.')
        
        # ATENÇÃO: max(pessoas) tenta descobrir a sublista "maior".
        # O Python compara o Nome (ordem alfabética) e pega o segundo elemento [1] do resultado.
        print(f'O maior peso foi de {max(pessoas)[1]}Kg. Peso de ', end='')
        
        # Varre a lista principal 'pessoas' acessando cada sublista 'p'
        for p in pessoas:
            # Se o peso da pessoa atual (p[1]) for igual ao peso encontrado no max():
            if p[1] == max(pessoas)[1]:
                # Imprime o nome da pessoa (p[0]) na mesma linha (end='')
                print(f'{p[0]} ', end='')
        print()  # Quebra de linha visual
        
        # Repete a mesma lógica usando min(pessoas) para buscar o menor valor
        print(f'O menor peso foi de {min(pessoas)[1]}Kg. Peso de ', end='')
        for p in pessoas:
            if p[1] == min(pessoas)[1]:
                print(f'{p[0]} ', end='')
        print()  # Quebra de linha visual
        
        # Encerra o loop 'while'
        break