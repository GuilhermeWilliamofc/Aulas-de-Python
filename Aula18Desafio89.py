from emoji import emojize
text = emojize(' Desafio 89 :cold_face: ')
print(f'{text:=^30}')

galera = []
cont = 1
cont2 = cont1 = 0

while True:
    nome = input(f'\033[33mNome do {cont}º Aluno: ').title().strip()
    nota1 = float(input(f'Primeira nota do(a) {nome}: '))
    nota2 = float(input(f'Segunda nota do(a) {nome}: '))
    media = (nota1 + nota2) / 2
    galera.append([nome, [nota1, nota2], media])

    resposta = ' '
    while resposta not in 'sn':
        resposta = input('Deseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break
    cont += 1

for i, a in enumerate(galera):
    print(f'\033[32m{i + 1}º Aluno: {a[0]} - Média: {a[2]}')

while True:
    aluno = int(input('\033[36mQual aluno você deseja ver a nota? (Digite o Número do Aluno): '))
    print(f'\033[mNotas de {galera[aluno - 1][0]}: ', end= '')
    print(f'{galera[aluno - 1][1]}')

    resposta = ' '
    while resposta not in 'sn':
        resposta = input('\033[35mDeseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break

print('\033[31mFim do Programa')
