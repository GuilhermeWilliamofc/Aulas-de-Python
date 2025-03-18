from emoji import emojize
text = emojize(' Desafio 52 :cold_face: ')
print(f'{text:=^30}')

num = int(input('\033[33mDigite um número: '))
tot = 0
for i in range(2, num):
    if num % i == 0:
        tot += 1
        print('\033[31m', end = ' ')
    else:
        print('\033[32m', end = ' ')
    print(i, end = ' ')

if tot > 0:
    print(f'\n\033[31mO Número {num} não é primo, pois entre 2 e {num - 1} ele é divisível por {tot} número(s)')
elif num == 1:
    print(f'\n\033[31mO Número {num} não é primo, pois o número 1 só é dividido por ele mesmo')
else:
    print(f'\n\033[32mO Número {num} é primo')
