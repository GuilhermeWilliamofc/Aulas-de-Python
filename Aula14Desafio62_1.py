from emoji import emojize
text = emojize(' Desafio 61 :cold_face: ')
print(f'{text:=^30}')

primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 1
total = 0
mais = 10

while mais != 0:
    total += mais
    while cont <= total:
        print(f'{termo} -- ', end= '')
        termo += razao
        cont += 1
    print('Pausa')
    mais = int(input('Quantos termos você quer mostrar a mais? '))

print(f'Durante a execução do programa {total} termos foram mostrados')
