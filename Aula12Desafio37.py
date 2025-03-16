from emoji import emojize
text = emojize(' Desafio 37 :cold_face: ')
print(f'{text:=^30}')

num = int(input('Escreva um número inteiro qualquer: '))
opcao = int(input('Qual será a base de conversão?\n1 para binário\n2 para octal\n3 para hexadecimal\nSua opção: '))
if opcao == 1:
    print(f'{num} em binário é igual a {bin(num)[2:]}')
elif opcao == 2:
    print(f'{num} em octal é igual a {oct(num)[2:]}')
elif opcao == 3:
    print(f'{num} em hexadecimal é igual a {hex(num)[2:]}')
else:
    print(f'Opção Inválida : (')
