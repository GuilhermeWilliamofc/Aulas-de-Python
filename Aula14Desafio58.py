from emoji import emojize
from time import sleep
from random import randint
text = emojize(' Desafio 58 :cold_face: ')
print(f'{text:=^30}')

print('\033[36mVou Pensar em um número inteiro entre 0 e 10...')
sleep(1)
print('\033[35mPensando...')
sleep(1)
num_pc = randint(0, 10)
num_jogador = -1
tentativas = 0
while num_jogador != num_pc:
    num_jogador = int(input('\033[33mEm que número eu pensei? '))
    if num_jogador < num_pc:
        print('\033[31mÉ Maior! Tente Novamente')
        tentativas += 1
    if num_jogador > num_pc:
        print('\033[31mÉ Menor! Tente Novamente')
        tentativas += 1
if tentativas == 0:
    print(f'\033[32mVocê Acertou de Primeira! Eu Pensei no Número {num_pc}')
else:
    print(f'\033[32mVocê Acertou! Eu Pensei no Número {num_pc},\033[31m Mas você errou {tentativas} vez(es)!')
