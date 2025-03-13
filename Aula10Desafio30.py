from emoji import emojize
from time import sleep
text = emojize(' Desafio 30 :cold_face: ')
print(f'{text:=^30}')

amarelo = ('\033[33m')
verde = ('\033[32m')
vermelho = ('\033[31m')

numero = int(input(f'{amarelo}Digite um número: '))
print('Carregando...')
sleep(0.5)
if numero % 2 == 0:
    print(f'{verde}O número {numero} é par.')
else:
    print(f'{vermelho}O número {numero} é ímpar.')
