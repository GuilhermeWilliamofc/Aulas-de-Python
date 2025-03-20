from emoji import emojize
from random import randint
text = emojize(' Desafio 74 :cold_face: ')
print(f'{text:=^30}')

num = (randint(1,10), randint(1,10), randint(1,10), randint(1,10), randint(1,10))

print(f'Eu sorteei os valores:')

for i in num:
    print(f'{i}', end = ' ')

print(f'\nO maior valor sorteado foi {max(num)}')
print(f'O menor valor sorteado foi {min(num)}')
