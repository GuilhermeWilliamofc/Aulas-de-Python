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
    if dados[1] >= 100:
        pesado.append(dados[:])
    if dados[1] < 100:
        leve.append(dados[:])
    pessoas.append(dados[:])
    dados.clear()
    pessoas_num += 1

    resposta = ' '
    while resposta not in 'sn':
        resposta = input('Deseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break

for p in pesado:
    if p[1] > maior:
        maior = p[1]
    if p[1] == maior:
            nome_pesado.append(p)

for i in nome_pesado:
    if i[1] == maior:
        nome_pesado_final.append(i[0])

for l in leve:
    if cont == 0:
        menor = l[1]
    if l[1] < menor:
        menor = l[1]
    if l[1] == menor:
        nome_leve.append(l)
    cont += 1

for i in nome_leve:
    if i[1] == menor:
        nome_leve_final.append(i[0])

print(f'No total {pessoas_num} pessoa(s) foram cadastradas')
if maior == 0:
    print('Nenhum maior peso foi registrado')
else:
    print(f'O maior peso foi de {maior}Kg, peso de {nome_pesado_final}')
if menor == 0:
    print('Nenhum menor peso foi registrado')
else:
    print(f'O menor peso foi de {menor}Kg, peso de {nome_leve_final}')
