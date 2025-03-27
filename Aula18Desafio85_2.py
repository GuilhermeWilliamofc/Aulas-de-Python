from emoji import emojize
text = emojize(' Desafio 85 :cold_face: ')
print(f'{text:=^30}')

temp = []
num = [[], []]
pares = impares = contador = 0

for i in range(1, 8):
    temp.clear()
    temp.append(int(input(f'\033[33mDigite o {i}º número: ')))
    if temp[0] % 2 == 0:
        num[0].append(temp[0])
        pares += 1
    elif temp[0] % 2 == 1:
        num[1].append(temp[0])
        impares += 1

num[0].sort()
num[1].sort()

if pares > 0:
    print(f'\033[32mOs Números Pares Digitados Foram: {num[0]}')
else:
    print('\033[31mNenhum Número Par foi Digitado')

if impares > 0:
    print(f'\033[32mOs Números Ímpares Digitados Foram: {num[1]}')
else:
    print('\033[31mNenhum Número Ímpar foi Digitado')
