from emoji import emojize
from random import randint
from time import sleep
from operator import itemgetter
text = emojize(' Desafio 91 :cold_face: ')
print(f'{text:=^30}')

dados = {}
ranking = list()
dados['jogador1'] = randint(1, 6)
dados['jogador2'] = randint(1, 6)
dados['jogador3'] = randint(1, 6)
dados['jogador4'] = randint(1, 6)

print('Valores Sorteados:')
sleep(1)

for k, v in dados.items():
    print(f'O {k} tirou {v}')
    sleep(1)

ranking = sorted(dados.items(), key=itemgetter(1), reverse=True)

print('\nRanking:')
sleep(1)

for i, v in enumerate(ranking):
    print(f'{i + 1}º Lugar - {v[0]} com {v[1]}')
    sleep(1)
