from emoji import emojize
from random import randint
from time import sleep
text = emojize(' Desafio 45 :cold_face: ')
print(f'{text:=^30}')

print('\033[35mVamos Jogar Jokenpô!')
sleep(1)
print('\033[36mSuas Opções:\n[ 0 ] Pedra\n[ 1 ] Papel\n[ 2 ] Tesoura')
jogada = int(input('\033[33mQual é a sua jogada? '))
nome = jogada

jogada_pc = randint(0, 2)

print('Carregando...')
sleep(2)

if nome == 0:
    print('Sua Jogada: Pedra')
if nome == 1:
    print('Sua Jogada: Papel')
if nome == 2:
    print('Sua Jogada: Tesoura') 
if nome > 2 or nome < 0:
    print('\033[31mSua Jogada: Inválida')

if jogada_pc == 0 and nome <= 2 and nome >= 0:
    print('\033[33mMinha Jogada: Pedra')
elif jogada_pc == 1 and nome <= 2 and nome >= 0:
    print('\033[33mMinha Jogada: Papel')
elif jogada_pc == 2 and nome <= 2 and nome >= 0:
    print('\033[33mMinha Jogada: Tesoura')

if jogada == jogada_pc:
    print('\033[33mEmpate!')
elif jogada == 0 and jogada_pc == 1 or jogada == 2 and jogada_pc == 0 or jogada == 1 and jogada_pc == 2:
    print('\033[31mVocê Perdeu!')
elif jogada == 1 and jogada_pc == 0 or jogada == 0 and jogada_pc == 2 or jogada == 2 and jogada_pc == 1:
    print('\033[32mVocê Venceu!')
elif jogada > 2 or jogada < 0:
    print('\33[31mJogada Inválida : (')
