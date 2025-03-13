text = 'Desafio 06'
print(f'{text:=^30}')

num = float(input('\033[36mDigite um número: '))
dobro = num*2
triplo = num*3
raiz = num**(1/2)
print(f'\033[35mSeu Número - {num}\nDobro do Seu Número - {dobro}\nTriplo do Seu Número - {triplo}\nRaiz Quadrada do Seu Número - {raiz:.2f}')
# usar **(1/2) ou pow(n,(1/2)) para raiz quadrada
