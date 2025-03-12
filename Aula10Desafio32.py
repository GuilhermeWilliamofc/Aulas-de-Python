from emoji import emojize
text = emojize(' Desafio 32 :cold_face: ')
print(f'{text:=^30}')

ano = int(input('Digite um ano: '))
if ano % 4 == 0 and ano % 100 != 0 or ano % 400 == 0:
    print(f'O Ano de {ano} é um ano bissexto')
else:
    print(f'O Ano de {ano} não é um ano bissexto')
