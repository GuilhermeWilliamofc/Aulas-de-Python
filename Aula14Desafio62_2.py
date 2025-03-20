from emoji import emojize
text = emojize(' Desafio 62 :cold_face: ')
print(f'{text:=^30}')

primeiro = int(input('Digite o termo: '))
razao = int(input('Digite a razão: '))
termo = primeiro
cont = 0
cont_2 = 1
resposta = 's'

while resposta == 's':   
    print(f'{cont_2}º Termo - {termo}')
    termo += razao
    cont += 1
    cont_2 += 1
    if cont == 10:
        resposta = input('Deseja ver mais 10 termos? [S/N] ').strip().lower()[0]
        cont = 0

print('Fim do Programa')
