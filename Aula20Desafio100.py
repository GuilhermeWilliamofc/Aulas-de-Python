from emoji import emojize
from time import sleep
from random import randint
text = emojize(' Desafio 100 :smiling_face_with_horns: :skull: :folded_hands: :moai: :wine_glass: ')
print(f'{text:=^30}')

def sorteia(lista):
    # no desafio original era para sortear 5 números e colocar na lista, mas decidi deixar a quantidade de números aleatória também
    quant = randint(1, 10)
    for n in range(0, quant):
        lista.append(randint(1, 10))
    print(f'Sorteando {len(lista)} valores da lista: ', end= '')
    for i in lista:
        print(f'{i}', end= ', ', flush=True)
        sleep(0.5)
    print('Pronto!')

def somapar(lista):
    sp = 0
    for n in lista:
        if n % 2 == 0:
            sp += n
    print(f'Somando os valores pares de {lista}, temos {sp}')


list = []
sorteia(list)
somapar(list)
