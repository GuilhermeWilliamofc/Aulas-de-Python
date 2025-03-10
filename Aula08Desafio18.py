from emoji import emojize
text = emojize('Desafio 18 :cold_face:')
print(f'{text:=^30}')

from math import cos,sin,tan
angulo = float(input('Digite algum ângulo - '))
seno = sin(angulo)
cose = cos(angulo)
tang = tan(angulo)
print(f'Com o ângulo de {angulo}° você tem:\nSeno: {seno}\nCosseno: {cose}\nTangente: {tang}')
