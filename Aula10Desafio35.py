from emoji import emojize
text = emojize(' Desafio 35 :cold_face: ')
print(f'{text:=^30}')

comprimento1 = float(input('\033[4;36mDigite o Primeiro Comprimento:\033[0m '))
comprimento2 = float(input('\033[4;33mDigite o Segundo Comprimento:\033[0m '))
comprimento3 = float(input('\033[4;35mDigite o Terceiro Comprimento:\033[0m '))

if comprimento1+comprimento2 > comprimento3 and comprimento2+comprimento3 > comprimento1 and comprimento1+comprimento3 > comprimento2:
    print(f'\033[0;32mCom esses comprimentos é possível formar um triângulo')
else:
    print(f'\033[0;31mCom esses comprimentos não é possível formar um triângulo')
