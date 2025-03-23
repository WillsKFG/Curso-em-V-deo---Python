#tocador de mp3

import pygame
pygame.init()
pygame.mixer.init()
pygame.mixer.music.load('BARRACO - Marcynho Sensação (DVD Ao Vivo em Fortaleza).mp3')
pygame.mixer.music.play()

while pygame.mixer.music.get_busy():
    pygame.time.Clock().tick(10)
