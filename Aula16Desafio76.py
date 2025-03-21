from emoji import emojize
text = emojize(' Desafio 76 :cold_face: ')
print(f'{text:=^30}')

nome = 'Listagem de Preços'
listagem = ('Lápis', 1.75, 'Borracha', 2.00, 'Caderno', 15.90, 'Estojo', 25.00, 'Transferidor', 4.20, 'Compasso', 9.99, 'Mochila', 120.32, 'Canetas', 22.30, 'Livro', 34.90)

print('-' * 37)
print(f'{nome:^37}')
print('-' * 37)
print('')

for pos in range(0, len(listagem)):
    if pos % 2 == 0:
        print(f'{listagem[pos]:.<30}', end = '')
    else:
        print(f'R${listagem[pos]:.2f}')

print('-' * 37)
