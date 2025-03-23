from emoji import emojize
text = emojize(' Desafio 79 :cold_face: ')
print(f'{text:=^30}')

num = list()
lista = ' '
while True:
    lista = int(input('\033[33mDigite um número: '))
    while lista in num:
        print('\033[31mEsse número já foi digitado')
        print('\033[31mTente Novamente, ', end= '')
        lista = int(input('\033[33mDigite um número: '))

    num.append(lista)

    pergunta = ' '
    while pergunta not in 'sn':
        pergunta = input('\033[35mDeseja Continuar? [S/N]: ').lower().strip()[0]
    if pergunta == 'n':
        break


num.sort()
print(f'\033[32mA lista de números é:\n{num}')
print('\033[31mFim do Programa')
