from emoji import emojize
text = emojize(' Desafio 65 :cold_face: ')
print(f'{text:=^30}')

contados = 0
num = 0
resposta = 's'
maior = 0
menor = 999

while resposta == 's':
    num = int(input('\033[36mDigite um número: '))
    contados += 1
    resposta = input('\033[33mDeseja continuar? [S/N] ').lower().strip()
    if contados == 0:
        maior = num
        menor = num
    if num > maior:
        maior = num
    if num < menor:
        menor = num

media = num / contados
print(f'\033[32mDurante a Execução do Programa:\n\033[33m{contados} números foram digitados\na média entre eles é {media}\no maior número digitado é {maior}\no menor número digitado é {menor}')
