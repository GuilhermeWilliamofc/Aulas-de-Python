from emoji import emojize
text = emojize(' Desafio 75 :cold_face: ')
print(f'{text:=^30}')


num = tuple(int(input('Digite um número: ')) for i in range(1,5))
cont = 0

if 9 in num:
    print(f'O Número 9 aparece {num.count(9)} vezes')
else:
    print('O Número 9 não foi digitado')

if 3 in num:
    print(f'O Número 3 aparece na posição {num.index(3) + 1}')
else:
    print('O Número 3 não foi digitado')

print('Os Números Pares Digitados Foram: ', end = '')

for i in num:
    if i % 2 == 0:
        print(i, end = ' ')
        cont += 1

if cont == 0:
    print('Nenhum : (')
