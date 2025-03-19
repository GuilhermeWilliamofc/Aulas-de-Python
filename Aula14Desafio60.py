from emoji import emojize
from math import factorial
text = emojize(' Desafio 60 :cold_face: ')
print(f'{text:=^30}')

resposta = 's'
conta = 0
while resposta == 's':
    num = int(input('\033[33mDigite um Número Para Descobrir seu fatorial: '))

    for i in range(num, 0, -1):
        if i == num:
            print(f'{num}! =', end = ' ')
        if i == num or i > 1:
            conta = i
            print(f'{i} x ', end = '')
        else:
            print(f'{i} = {multiplicacao}', end = '')
        multiplicacao = factorial(num)
    resposta = input('\nDeseja digitar outro número? [S/N]: ').lower().strip()
print('\033[31mFim do Programa')
