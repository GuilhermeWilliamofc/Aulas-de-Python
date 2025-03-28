from emoji import emojize
text = emojize(' Desafio 94 :cold_face: ')
print(f'{text:=^30}')

pessoas = {}
cont = tot_idades = 0
total = 1
mulheres = []

while True:
    pessoas[f'nome{cont}'] = input('Nome: ').title()

    pessoas[f'sexo{cont}'] = ' '

    while pessoas[f'sexo{cont}'] not in 'mf':
        pessoas[f'sexo{cont}'] = input('Sexo [M/F]: ').lower().strip()[0]
    if pessoas[f'sexo{cont}'] == 'f':
        mulheres.append(pessoas[f'nome{cont}'])
    pessoas[f'idade{cont}'] = int(input('Idade: '))

    tot_idades += pessoas[f'idade{cont}']

    resposta = ' '
    while resposta not in 'sn':
        resposta = input('Deseja Continuar? [S/N]: ').lower().strip()[0]
    if resposta == 'n':
        break
    total += 1
    cont += 1

media = tot_idades / total

print('-' * 30)
print(f'O grupo tem {total} pessoas')
print(f'A média de idades é de {media:.2f} anos')

if len(mulheres) > 0:
    print(f'As mulheres cadastradas foram: ', end= '')

for i in mulheres:
    print(f'[{i}]', end= ' ')

print(f'\nA Lista de Pessoas que estão acima da média:')

for i in range(0, total):
    if pessoas[f'idade{i}'] > media:
        print(f'Nome: {pessoas[f'nome{i}']}, Sexo: {pessoas[f'sexo{i}'].title()}, Idade: {pessoas[f'idade{i}']};')

print('-' * 30)
print('Fim do Programa')
