# 'def' define uma nova função chamada 'escreva'
# 'msg' é o parâmetro que recebe o texto digitado ao chamar a função
def escreva(msg):
    
    # len(msg) conta a quantidade de caracteres (letras, espaços, símbolos)
    # Somamos + 4 para deixar uma margem de 2 espaços na esquerda e 2 na direita
    tam = len(msg) + 4
    
    # Imprime o caractere '~' multiplicado pelo número total em 'tam' (cria a borda superior)
    print('~' * tam)
    
    # Imprime a mensagem centralizada com 2 espaços antes e 2 depois
    print(f'  {msg}  ')
    
    # Imprime a borda inferior do mesmo tamanho da borda superior
    print('~' * tam)


# --- CHAMADAS DA FUNÇÃO ---
# Cada chamada envia o texto entre aspas para o parâmetro 'msg' dentro da função

escreva('Olá, Mundo!')
escreva('Curso de Python no YouTube')
escreva('Exercício 97 Mundo 3')