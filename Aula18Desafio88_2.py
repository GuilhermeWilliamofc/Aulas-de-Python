from emoji import emojize
from random import randint
from time import sleep
text = emojize(f' Desafio 88 :cold_face: ')
print(f'{text:=^30}')

sorteio = []
lista = []
jogos = int(input('\033[33mDigite quantos jogos você quer que eu sorteie: '))
print(f'Sorteando {jogos} jogos!')

for i in range(1, jogos + 1):
    sorteio.clear()
    while len(sorteio) != 6:
        num = randint(1, 60)
        if num not in sorteio:
            sorteio.append(num)
    sorteio.sort()
    lista.append(sorteio[:])

for i, l in enumerate(lista):
    print(f'\33[36m{i + 1}º Jogo: {l}')
    sleep(1)

print('\033[32mBoa Sorte!')

