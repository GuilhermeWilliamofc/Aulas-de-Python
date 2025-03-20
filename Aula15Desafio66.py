from emoji import emojize
text = emojize(' Desafio 66 :cold_face: ')
print(f'{text:=^30}')

soma = digitados = 0

while True:
    num = int(input('\033[33mDigite um número [999 para parar]: '))
    if num == 999:
        break
    soma += num
    digitados += 1

print(f'\033[32mDurante a Execução do Programa:\n\033[35m{digitados} Números Foram Digitados\nA Soma Entre Eles é Igual a {soma}')
