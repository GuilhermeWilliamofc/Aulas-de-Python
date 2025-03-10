import emoji
text = emoji.emojize('Desafio 16 :cold_face:')
print(f'{text:=^30}')

from math import trunc
num = float(input('Digite um Número Real Qualquer - '))
numint = trunc(num)
print(f'A porção inteira de {num} é {numint}')
