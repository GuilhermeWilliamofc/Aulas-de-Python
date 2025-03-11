from emoji import emojize
text = emojize(' Desafio 25 :cold_face: ')
print(f'{text:=^30}')
nome = input('Digite seu nome completo: ')
if nome:
    nome = nome.lower().split()
    if 'silva' in nome:
        print('Seu nome tem Silva')
    else:
        print('Seu nome não tem Silva')
