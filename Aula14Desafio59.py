from emoji import emojize
from time import sleep
text = emojize(' Desafio 59 :cold_face: ')
print(f'{text:=^30}')

num1 = int(input('\033[33mDigite o Primeiro Valor: '))
num2 = int(input('Digite o Segundo Valor: '))
maior = 0
opcao = 0
# while opcao != 5 também funciona
# dava pra usar sleep fora dos if...
while not opcao == 5:
    opcao = int(input('\033[36mEscolha uma Opção:\n\033[33m[ 1 ]\033[m Somar\n\033[33m[ 2 ]\033[m Multiplicar\n\033[33m[ 3 ]\033[m Maior Número\n\033[33m[ 4 ]\033[m Digitar Novos Números\n\033[33m[ 5 ]\033[m Sair do Programa\n\033[32mOpção: '))
    if opcao == 1:
        soma = num1 + num2
        texto = (f'\033[33m Soma: {num1} + {num2} = {soma} ')
        print(f'{texto:=^30}')
        sleep(2)
    if opcao == 2:
        soma2 = num1 * num2
        texto2 = (f'\033[33m Multiplicação: {num1} x {num2} = {soma2} ')
        print(f'{texto2:=^40}')
        sleep(2)
    if opcao == 3:
        if num1 > num2:
            maior = num1
        if num2 > num1:
            maior = num2
        texto3 = (f'\033[33m Maior Número = {maior} ')
        print(f'{texto3:=^30}')
        sleep(2)
    if opcao == 4:
        num1 = int(input('\033[33mDigite o Primeiro Valor: '))
        num2 = int(input('\033[33mDigite o Segundo Valor: '))
    if opcao > 5 or opcao < 1:
        print('\033[31mOpção Inválida! Tente Novamente')
        sleep(1)

print('\033[31mPrograma Fechado')
