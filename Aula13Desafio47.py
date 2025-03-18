from emoji import emojize
text = emojize(' Desafio 47 :cold_face: ')
print(f'{text:=^30}')

for c in range(2, 51, 2):
    print(c, end = ' ')
print('\nFim da Contagem')
