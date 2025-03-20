from emoji import emojize
import math
text = emojize(' Desafio 71 :cold_face: ')
print(f'{text:=^30}')

banco = 'Banco Gw'
resposta = ' '

print('='*30)
print(f'{banco: ^30}')
print('='*30)
print('')

while True:
    dindin1 = 0
    dindin2 = 0
    dindin3 = 0
    dindin4 = 0
    
    valor = int(input('\033[33mQue valor você quer sacar? R$'))
    
    if valor / 50 > 0:
        conta1 = math.trunc(valor / 50)
        dindin1 = valor - (50 * conta1)
        if dindin1 >= 0 and conta1 > 0:
            print(f'\033[32m{conta1} Notas de R$50.00 Sacadas')
    if dindin1 / 20 > 0:
        conta2 = math.trunc(dindin1 / 20)
        dindin2 = dindin1 - (20 * conta2)
        if dindin2 >= 0 and conta2 > 0:
            print(f'\033[32m{conta2} Notas de R$20.00 Sacadas')
    if dindin2 / 10 > 0:
        conta3 = math.trunc(dindin2 / 10)
        dindin3 = dindin2 - (10 * conta3)
        if dindin3 >= 0 and conta3 > 0:
            print(f'\033[32m{conta3} Notas de R$10.00 Sacadas')
    if dindin3 / 1 > 0:
        conta4 = math.trunc(dindin3 / 1)
        dindin4 = dindin3 - (1 * conta4)
        if dindin4 >= 0:
            print(f'\033[32m{conta4} Notas de R$1.00 Sacadas')
    if valor == 0:
        print('\033[31mNenhum Valor Sacado')

    resposta = input('\033[33mDeseja Realizar Outro Saque? [S/N]: ').lower().strip()[0]
    while resposta not in 'sn':
        resposta = input('\033[33mDeseja Realizar Outro Saque? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break


print('\033[36mObrigado Por Utilizar Nossos Serviços e Volte Sempre!')
