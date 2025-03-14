from emoji import emojize
from datetime import date
from time import sleep
text = emojize(' Desafio 39 :cold_face: ')
print(f'{text:=^30}')

ano = int(input('\033[33mDigite seu ano de nascimento: '))
idade = date.today().year - ano
atras = idade - 18
estara = 18 - idade
print('\033[36mCarregando...')
sleep(1.5)
if idade == 18:
    print('\033[31mVocê está no ano de alistamento!')
elif idade > 18:
    print(f'\033[32mVocê esteve no ano de alistamento há {atras} ano(s) atrás...')
else:
    print(f'\033[33mVocê estará no ano de alistamento daqui {estara} ano(s)')
