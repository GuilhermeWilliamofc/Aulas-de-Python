from emoji import emojize
text = emojize(' Desafio 27 :cold_face: ')
print(f'{text:=^30}')

amarelo = ('\033[33m')
ciano = ('\033[36m')

nome = input(f'{amarelo}Digite seu nome completo: ').split()
print(f'{ciano}Seu primeiro nome é {nome[0]} e seu último nome é {nome[-1]}')
