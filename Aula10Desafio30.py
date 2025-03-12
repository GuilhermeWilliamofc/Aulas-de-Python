from emoji import emojize
text = emojize(' Desafio 30 :cold_face: ')
print(f'{text:=^30}')

numero = int(input('Digite um número: '))
if numero % 2 == 0:
    print(f'O número {numero} é par.')
else:
    print(f'O número {numero} é ímpar.')
