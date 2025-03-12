from emoji import emojize
text = emojize(' Desafio 28 :cold_face: ')
print(f'{text:=^30}')

from random import randint
print('Vou pensar em um número entre 0 e 5. Tente adivinhar...')
num = int(input('Em que número eu pensei? '))
num_aleatorio = randint(0, 5)
if num == num_aleatorio:
    print(emojize('Parabéns! Você acertou! :smiling_face_with_sunglasses:'))
else:
    print(emojize(f'Você errou! Eu pensei no número {num_aleatorio}... :face_with_rolling_eyes:'))
