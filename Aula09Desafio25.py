from emoji import emojize
text = emojize(' Desafio 25 :cold_face: ')
print(f'{text:=^30}')

amarelo = ('\033[33m')
verde = ('\033[32m')
vermelho = ('\033[31m')

nome = input(f'{amarelo}Digite seu nome completo: ')
if nome:
    nome = nome.lower().split()
    if 'silva' in nome:
        print(f'{verde}Seu nome tem Silva')
    else:
        print(f'{vermelho}Seu nome não tem Silva')
