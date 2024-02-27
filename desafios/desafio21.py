import pygame
pygame.init()
pygame.mixer.music.load('desafio21.mp3')
pygame.mixer.music.play()
input()   # precisa adiciona input() agora para fazer com que a música toque.
pygame.event.wait()
