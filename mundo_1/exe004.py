# Lê a entrada do teclado
entrada = input("Digite algo: ")

# Exibe o tipo primitivo (sempre será <class 'str'> para input)
print(f"O tipo primitivo deste valor é: {type(entrada)}")

# Exibe informações detalhadas sobre o texto digitado
print(f"É numérico? {entrada.isnumeric()}")
print(f"É alfabético? {entrada.isalpha()}")
print(f"É alfanumérico? {entrada.isalnum()}")
print(f"Está em maiúsculas? {entrada.isupper()}")
print(f"Está em minúsculas? {entrada.islower()}")
print(f"Está capitalizado (primeira maiúscula)? {entrada.istitle()}")
print(f"Contém apenas espaços? {entrada.isspace()}")