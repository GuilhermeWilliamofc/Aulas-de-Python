from emoji import emojize
from time import sleep
text = emojize(' Desafio 98 :cold_face: ')
print(f'{text:=^30}')

def contador(a, b, c):
    print('\033[33m-' * 30)
    if c == 0:
        c = 1
    if c < 0:
        c *= -1
    print(f'\033[33mContagem de {a} até {b} de {c} em {c}:')
    if b < a:
        b -= 1
        c = -c
    else:
        b += 1
    for i in range(a, b, c):
        print(f'[{i}]', end= ' ', flush=True) 
        # o flush deixa você ver os números contando em tempo real
        sleep(0.5)
    print('')
    print('-' * 30)
    sleep(1)

contador(1, 10, 1)
contador(10, 0, 2)
print('\033[32mAgora a sua vez de personalizar a contagem!')
sleep(1)
while True:
    inicio = int(input('\033[35mInício: '))
    fim = int(input('\033[36mFim: '))
    passo = int(input('\033[34mPasso: '))
    contador(inicio, fim, passo)
    resposta = ' '
    while resposta not in 'sn':
        resposta = input('Deseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break

print('\033[31mFim do Programa')
