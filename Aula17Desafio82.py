from emoji import emojize
text = emojize(' Desafio 82 :cold_face: ')
print(f'{text:=^30}')

padrao = []
pares = []
impares = []
cont = 1

while True:
    lista = int(input(f'\033[33mDigite o {cont}º Número: '))
    padrao.append(lista)
    if lista % 2 == 0:
        pares.append(lista)
    elif lista % 2 == 1:
        impares.append(lista)

    cont += 1

    resposta = ' '
    while resposta not in 'sn':
        resposta = input('\033[36mDeseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break

print(f'\033[32mA lista dos números pares é:\n{pares}\nA lista dos números ímpares é:\n{impares}\nA lista com todos os números é:\n{padrao}')
