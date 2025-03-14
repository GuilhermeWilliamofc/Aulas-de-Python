from emoji import emojize
from time import sleep
text = emojize(' Desafio 43 :cold_face: ')
print(f'{text:=^30}')

peso = float(input('\033[36mDigite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)
imc_corrigido = (f'{imc:.2f}')

print('\033[35mCarregando...')
sleep(1.5)

print(f'\033[33mSeu IMC = {imc_corrigido}')
if imc < 18.5:
    print('\033[31mAbaixo do Peso')
elif imc >= 18.5 and imc < 25:
    print('\033[32mPeso Ideal')
elif imc >= 25 and imc < 30:
    print('\033[33mSobrepeso')
elif imc >= 30 and imc < 40:
    print('\033[31mObesidade')
else:
    print('\033[31mObesidade mórbida')
