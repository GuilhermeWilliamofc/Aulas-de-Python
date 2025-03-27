from emoji import emojize
text = emojize(' Desafio 86 :cold_face: ')
print(f'{text:=^30}')

matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l][c]:^5}]', end= '')
    print()
