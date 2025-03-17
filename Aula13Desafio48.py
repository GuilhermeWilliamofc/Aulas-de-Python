from emoji import emojize
text = emojize(' Desafio 48 :cold_face: ')
print(f'{text:=^30}')

soma = 0
for c in range(1, 500, 2):
    if c % 3 == 0:
        soma += c
    else:
        pass

print(f'A Soma de todos os número ímpares múltiplos de 3 entre 1 e 500 é {soma}')
