from emoji import emojize
from fibonacci import fibonacci
text = emojize(' Desafio 63 :cold_face: ')
print(f'{text:=^30}')

resposta = 's'
while resposta == 's':
    num = int(input('\033[33mDigite um Número: '))
    print(fibonacci(length = num))
    resposta = input('\033[32mDeseja digitar outro número? [S/N] ').lower().strip()
print('\033[31mFim do Programa')
