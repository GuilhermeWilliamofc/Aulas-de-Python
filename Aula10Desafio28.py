from emoji import emojize
from time import sleep
text = emojize(' Desafio 28 :cold_face: ')
print(f'{text:=^30}')

from random import randint
print('\033[4;34mVou pensar em um número entre 0 e 5. Tente adivinhar...')
num = int(input('\033[0;36mEm que número eu pensei? '))
print('\033[0;33mCarregando...')
sleep(2)
num_aleatorio = randint(0, 5)
if num == num_aleatorio:
    print(emojize('\033[0;32mParabéns! Você acertou! :smiling_face_with_sunglasses:'))
else:
    print(emojize(f'\033[0;31mVocê errou! Eu pensei no número {num_aleatorio}... :face_with_rolling_eyes:'))
