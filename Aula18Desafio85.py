from emoji import emojize
text = emojize(' Desafio 85 :cold_face: ')
print(f'{text:=^30}')

temp = []
num = []
pares = impares = contador = 0

for i in range(1, 8):
    temp.append(int(input(f'\033[33mDigite o {i}º número: ')))
    num.append(temp[:])
    if temp[contador] % 2 == 0:
        pares += 1
    elif temp[contador] % 2 == 1:
        impares += 1
    contador += 1

if pares > 0:
    print('\033[32mOs Números Pares Digitados Foram: ', end= '')
else:
    print('\033[31mNenhum Número Par foi Digitado')

for cont, i in enumerate(num):
    if i[cont] % 2 == 0:
        print(i[cont], end= ' ')

if impares > 0:
    print('\n\033[32mOs Números Ímpares Digitados Foram: ', end= '')
else:
    print('\n\033[31mNenhum Número Ímpar foi Digitado')

for cont, i in enumerate(num):
    if i[cont] % 2 == 1:
        print(i[cont], end= ' ')
