import os
import pygame

pygame.init()

# Encontra a pasta exata onde este arquivo exe021.py está salvo
pasta_atual = os.path.dirname(__file__)
caminho_audio = os.path.join(pasta_atual, 'exe021.mp3')

pygame.mixer.music.load(caminho_audio)
pygame.mixer.music.play()

# Aguarda a música terminar de tocar para fechar
while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)