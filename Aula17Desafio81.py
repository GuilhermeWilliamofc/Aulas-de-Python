from emoji import emojize
text = emojize(' Desafio 81 :cold_face: ')
print(f'{text:=^30}')

cont = 0
num = []

while True:
    num.append(int(input(f'\033[33mDigite o {cont + 1}º Número: ')))
    cont += 1
    
    resposta = ' '
    while resposta not in 'sn':
        resposta = input('\033[35mDeseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break

num.sort(reverse=True)

print(f'\033[34m{cont} Números Foram Digitados')

print(f'\033[36mA Lista em Ordem Decrescente: {num}')

if 5 in num:
    print('\033[32mO Número 5 está na lista')
else:
    print('\033[31mO Número 5 não está na lista')
