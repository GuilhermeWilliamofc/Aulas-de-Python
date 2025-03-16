from emoji import emojize
text = emojize(' Desafio 38 :cold_face: ')
print(f'{text:=^30}')

num1 = int(input('\033[33mDigite um número inteiro: '))
num2 = int(input('Digite outro número inteiro: '))
if num1 > num2:
    print(f'\033[32m{num1} é o maior valor')
elif num2 > num1:
    print(f'\033[32m{num2} é o maior valor')
else:
    print('\033[31mNão existe valor maior, os dois são iguais')
