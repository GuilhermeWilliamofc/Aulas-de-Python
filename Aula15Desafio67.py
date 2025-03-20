from emoji import emojize
from time import sleep
text = emojize(' Desafio 67 :cold_face: ')
print(f'{text:=^30}')

while True:
    num = int(input('\033[33mDigite um número para Aparecer sua tabuada: '))
    if num < 0:
        break
    for i in range(1, 11):
        conta = num * i
        print(f'\033[32m{num} x {i} = {conta}')

print('\033[31mFim do Programa')
