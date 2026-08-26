import math

angulo = float(input('Digite o ângulo que você deseja: '))

# Converte o ângulo de graus para radianos
radiano = math.radians(angulo)

seno = math.sin(radiano)
cosseno = math.cos(radiano)
tangente = math.tan(radiano)

print(f'O ângulo de {angulo}° tem o SENO de {seno:.2f}')
print(f'O ângulo de {angulo}° tem o COSSENO de {cosseno:.2f}')
print(f'O ângulo de {angulo}° tem a TANGENTE de {tangente:.2f}')