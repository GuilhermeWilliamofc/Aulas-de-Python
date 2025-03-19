from emoji import emojize
text = emojize(' Desafio 61 :cold_face: ')
print(f'{text:=^30}')

primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
while cont <= 10:
    print(f'{termo} -- ', end= '')
    termo += razao
    cont += 1
print('Fim')