from emoji import emojize
text = emojize(' Desafio 93 :cold_face: ')
print(f'{text:=^30}')

dados_jogador = {}
gols = []
gols_total = gols_temp = 0

dados_jogador['nome'] = input('Nome do Jogador: ').title()
dados_jogador['partidas'] = int(input(f'Quantas Partidas {dados_jogador["nome"]} Jogou? '))

if dados_jogador['partidas'] > 0:
    for i in range(0, dados_jogador['partidas']):
        gols_temp = 0
        gols_temp = int(input(f'Quantos Gols na {i + 1}º Partida? '))
        gols.append(gols_temp)
        gols_total += gols_temp

print(f'Nome do Jogador: {dados_jogador["nome"]}')
print(f'A Lista de Gols é: {gols}')
print(f'O Total de Gols é: {gols_total}')

print(f'O Jogador {dados_jogador["nome"]} Jogou {dados_jogador["partidas"]} Partidas:')

for n, p in enumerate(gols):
    print(f'Na {n + 1}º Partida, fez {p} Gols')

print(f'Foi um total de {gols_total} gols')
