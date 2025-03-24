from emoji import emojize
text = emojize(' Desafio 84 :cold_face: ')
print(f'{text:=^30}')

dados = []
pessoas = []
nome_pesado = []
pesado = []
nome_leve = []
leve = []
nome_leve_final = []
nome_pesado_final = []
pessoas_num = maior = menor = cont = 0

while True:
    dados.append(input('Digite o Nome: ').capitalize().strip())
    dados.append(float(input('Digite o peso: ')))
    if len(pessoas) == 0:
        maior = menor = dados[1]
    else:
        if dados[1] > maior:
            maior = dados[1]
        if dados[1] < menor:
            menor = dados[1]
    pessoas.append(dados[:])
    dados.clear()

    resposta = ' '
    while resposta not in 'sn':
        resposta = input('Deseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break

print(f'No total {len(pessoas)} pessoa(s) foram cadastradas')
print(f'O maior peso foi de {maior}Kg, peso de ', end= '')
for i in pessoas:
    if i[1] == maior:
        print(f'[{i[0]}]', end= ' ')
print(f'\nO menor peso foi de {menor}Kg, peso de ', end= '')
for i in pessoas:
    if i[1] == menor:
        print(f'[{i[0]}]', end= ' ')
