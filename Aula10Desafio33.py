from emoji import emojize
from time import sleep
text = emojize(' Desafio 33 :cold_face: ')
print(f'{text:=^30}')

azul = ('\033[34m')
roxo = ('\033[35m')
amarelo = ('\033[33m')

num1 = int(input(f'{roxo}Digite o Primeiro Número: '))
num2 = int(input('Digite o Segundo Número: '))
num3 = int(input('Digite o Terceiro Número: '))

print(f'{amarelo}Carregando...')
sleep(1.5)
maior = num1
if num2 == num2 > num1 and num2 > num3:
    maior = num2
if num3 == num3 > num1 and num3 > num2:
    maior = num3

menor = num1
if num2 == num2 < num1 and num2 < num3:
    menor = num2
if num3 == num3 < num1 and num3 < num2:
    menor = num3

print(f'{azul}{menor} é o menor número e {maior} é o maior número')
