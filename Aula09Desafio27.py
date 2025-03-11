from emoji import emojize
text = emojize(' Desafio 27 :cold_face: ')
print(f'{text:=^30}')

nome = input('Digite seu nome completo: ').split()
print(f'Seu primeiro nome é {nome[0]} e seu último nome é {nome[-1]}')
