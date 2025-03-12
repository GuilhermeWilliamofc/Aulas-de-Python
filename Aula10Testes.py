from emoji import emojize
text = emojize(' Aula 10 - Testes :cold_face: ')
print(f'{text:=^30}')

nome = input('Digite seu nome: ')
corrigirnome = nome.strip().capitalize()
edicoes = nome.lower().strip().split()
if edicoes[0] == 'guilherme':
    print(emojize(f'Nome Bonito {corrigirnome} :smiling_face_with_sunglasses:'))
else:
    print(emojize(f'Nome Feio {corrigirnome}... :face_with_rolling_eyes:'))
