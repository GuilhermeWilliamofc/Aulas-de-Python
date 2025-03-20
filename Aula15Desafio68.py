from emoji import emojize
from random import randint
from time import sleep
text = emojize(' Desafio 68 :cold_face: ')
print(f'{text:=^30}')

contador = 0
print('\033[35mVamos Jogar Par ou Ímpar!')
sleep(1)

while True:
    num_jogador = int(input('\033[33mDigite um Número: '))
    jogada_jogador = ' '
    while jogada_jogador not in 'pi':
        jogada_jogador = input('\033[36mPar ou Ímpar? [P/I]: ').lower().strip()[0]

    num_pc = randint(0, 10)
    jogada_pc = 0

    if jogada_jogador == 'p':
        jogada_pc += 1
        print('Sua Jogada: Par\nJogada do Computador: Ímpar')
    elif jogada_jogador == 'i':
        jogada_pc += 2
        print('Sua Jogada: Ímpar\nJogada do Computador: Par')

    total = num_jogador + num_pc

    print(f'\033[33mVocê Jogou {num_jogador} e o Computador {num_pc}. Dando o total de {total}', end = '')

    if total % 2 == 0:
        print('\033[33m, Deu Par!')
    else:
        print('\033[33m, Deu Ímpar!')

    if total % 2 == 0 and jogada_pc == 2 or total % 2 == 1 and jogada_pc == 1:
        print('\033[31mVocê Perdeu!')
        break
    else:
        print('\033[32mVocê Ganhou!')
        contador += 1
    sleep(1)

sleep(1)
if contador > 0:
    print(f'\033[31mFim de Jogo! Você venceu {contador} vezes seguidas')
else:
    print(f'\033[31mFim de Jogo! Perdeu de primeira, Você é um fracasso!')
