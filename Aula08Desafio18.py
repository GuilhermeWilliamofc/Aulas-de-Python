from emoji import emojize
text = emojize('Desafio 18 :cold_face:')
print(f'{text:=^30}')

from math import cos,sin,tan,radians
angulo = float(input('Digite algum ângulo - '))
radiano = radians(angulo)
seno = sin(radiano)
cose = cos(radiano)
tang = tan(radiano)
print(f'Com o ângulo de {angulo:.2f}° você tem:\nSeno: {seno:.2f}\nCosseno: {cose:.2f}\nTangente: {tang:.2f}')

# não sabia que as funções sin, cos e tan precisavam de radianos para funcionar