from emoji import emojize
text = emojize(' Desafio 95 :cold_face: ')
print(f'{text:=^30}')

dados_jogador = {}
gols = []
num_jogador = num_jogador_total = cont = 0

while True:
    gols_total = gols_temp = 0

    dados_jogador[f'nome{num_jogador}'] = input('Nome do Jogador: ').title()
    dados_jogador[f'partidas{num_jogador}'] = int(input(f'Quantas Partidas {dados_jogador[f"nome{num_jogador}"]} Jogou? '))

    if dados_jogador[f'partidas{num_jogador}'] > 0:
        for i in range(0, dados_jogador[f'partidas{num_jogador}']):
            gols_temp = 0
            gols_temp = int(input(f'Quantos Gols na {i + 1}º Partida? '))
            gols.append(gols_temp)
            gols_total += gols_temp

    dados_jogador[f"gols{num_jogador}"] = gols[:]
    dados_jogador[f"gols_total{num_jogador}"] = gols_total
    gols.clear()
    
    resposta = ' '
    while resposta not in 'sn':
        resposta = input('Deseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break
    if resposta == 's':
        num_jogador += 1
        num_jogador_total += 1
    
while True:
    print('')    
    print('Jogadores: ', end= '')
    print()

    for i in range(0, num_jogador_total + 1):
        print(f'Nº{i} -', end= ' ')
        print(f'[{dados_jogador[f"nome{i}"]}]')
        
    if cont == 0:
        opcao = int(input('Mostrar dados de qual jogador? (Digite o Número do Jogador): '))
    else:
        opcao = int(input('Mostrar dados de qual jogador dessa vez? '))

    if opcao > num_jogador_total or opcao < 0:
        while opcao > num_jogador_total or opcao < 0:
            print('Número de Jogador Inválido')
            opcao = int(input('Mostrar dados de qual jogador? (Digite o Número do Jogador): '))

    print('')
    print(f'Nome do Jogador: {dados_jogador[f"nome{opcao}"]}')
    print(f'Jogou {dados_jogador[f"partidas{opcao}"]} Partidas')
    print(f'A Lista de Gols é: {dados_jogador[f"gols{opcao}"]}')
    print(f'O Total de Gols é: {dados_jogador[f"gols_total{opcao}"]}')
    print('')
    print('Partidas:')
    for n, p in enumerate(dados_jogador[f"gols{opcao}"]):
        print(f'Na {n + 1}º Partida, fez {p} Gols')

    print('')

    resposta = ' '
    while resposta not in 'sn':
        resposta = input('Deseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break
    cont += 1

print('Fim do Programa')
