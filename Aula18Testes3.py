dados = []
galera = []

while True:
    dados.append(input('Digite o nome: '))
    dados.append(int(input('Digite a idade: ')))
    galera.append(dados[:])
    dados.clear()

    resposta = ' '
    while resposta not in 'sn':
        resposta = input('Deseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break

for i in galera:
    print(f'{i[0]} tem {i[1]} anos de idade')
