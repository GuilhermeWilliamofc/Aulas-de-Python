from emoji import emojize
from datetime import date
text = emojize(' Desafio 54 :cold_face: ')
print(f'{text:=^30}')

maior = 0
menor = 0
num = 0
for i in range(0, 7):
    num += 1
    ano = int(input(f'\033[33mDigite o ano de nascimento da {num}º pessoa: '))
    idade = date.today().year - ano
    if idade >= 21:
        maior += 1
    else:
        menor += 1
print(f'\033[32mDe 7 Pessoas, {maior} tem maioridade e {menor} ainda não atingiu a maioridade')
