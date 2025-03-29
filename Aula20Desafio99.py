from emoji import emojize
from time import sleep
text = emojize(' Desafio 99 :cold_face: ')
print(f'{text:=^30}')

def maior(* num):
    if len(num) == 0:
        print('-' * 50)
        print('Analisando os valores passados...')
        sleep(1)
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi nenhum')
        print('-' * 50)
    else:
        print('-' * 50)
        print('Analisando os valores passados...')
        sleep(1)
        for i in num:
            print(f'[{i}]', end= ' ')
        print(f'Foram informados {len(num)} valores ao todo.')
        print(f'O maior valor informado foi {max(num)}')
        print('-' * 50)
    

maior(2, 9, 4, 5, 7, 1)
maior(4, 7, 0)
maior(1, 2)
maior(6)
maior()
