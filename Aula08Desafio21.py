from emoji import emojize
text = emojize('Desafio 21 :cold_face:')
print(f'{text:=^30}')

import pygame
botao = input(emojize('\033[33mDigite Qualquer Botão :musical_note: : '))
pygame.init()
pygame.mixer.music.load('kyuss_hurricane.mp3')
pygame.mixer.music.play()
print(emojize('\033[32mMúsica Tocada Com Sucesso! :smiling_face_with_sunglasses:'))
input()
pygame.event.wait()
