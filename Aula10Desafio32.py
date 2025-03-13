from emoji import emojize
from datetime import date
text = emojize(' Desafio 32 :cold_face: ')
print(f'{text:=^30}')

ciano = ('\033[36m')
verde = ('\033[32m')
vermelho = ('\033[31m')

ano = int(input(f'{ciano}Digite um ano (Digite -1 para analisar o ano atual): '))
if ano == -1:
    ano = date.today().year
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'{verde}O Ano de {ano} é um ano bissexto')
else:
    print(f'{vermelho}O Ano de {ano} não é um ano bissexto')
