from emoji import emojize
text = emojize('Desafio 17 :cold_face:')
print(f'{text:=^30}')

from math import hypot
catoposto = float(input('Digite o Valor do Cateto Oposto - '))
catadjac = float(input('Digite o Valor do Cateto Adjacente - '))
hip = hypot(catoposto, catadjac)
print(f'A Hipotenusa é igual a {hip:.2f}')
