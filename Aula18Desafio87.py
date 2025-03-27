from emoji import emojize
text = emojize(' Desafio 86 :cold_face: ')
print(f'{text:=^30}')

soma1 = soma2 = 0
matriz = [0, 0, 0], [0, 0, 0], [0, 0, 0]
for l in range(0, 3):
    for c in range(0, 3):
        matriz[l][c] = int(input(f'Digite um valor para [{l}, {c}]: '))

for l in range(0, 3):
    for c in range(0, 3):
        print(f'[{matriz [l][c]:^5}]', end= '')
    print()

for l in range(0, 3):
    for c in range(0, 3):
        if matriz[l][c] % 2 == 0:
            soma1 += matriz[l][c]

for l in range(0, 3):
    soma2 += matriz[l][2]

for l in range(0, 3):
    if l == 0:
        maior = matriz[1][c]
    elif matriz[1][c] > maior:
        maior = matriz[1][c]

print(f'A soma dos valores pares é {soma1}')
print(f'A soma dos valores da terceira coluna é {soma2}')
print(f'O maior valor da segunda linha é {maior}')
