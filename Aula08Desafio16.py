import emoji
text = emoji.emojize('Desafio 16 :cold_face:')
print(f'{text:=^30}')

from math import trunc
num = float(input('\033[33mDigite um Número Real Qualquer - '))
numint = trunc(num)
print(f'\033[36mA porção inteira de {num} é {numint}')
