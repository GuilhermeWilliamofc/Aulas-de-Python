from emoji import emojize
text = emojize(' Desafio 50 :cold_face: ')
print(f'{text:=^30}')

num = 0
x = 0
cont = 0
for soma in range(0, 6):
    x += 1
    num2 = int(input(f'Digite o {x}° número: '))
    if num2 % 2 == 0:
        num += num2
        cont += 1
if num == 0 and cont == 0:
    print('Nenhum número par foi digitado')
else:
    print(f'A Soma de todos os {cont} números pares digitados é igual a {num}')
