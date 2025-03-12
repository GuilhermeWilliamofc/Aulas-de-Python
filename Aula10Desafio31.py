from emoji import emojize
text = emojize(' Desafio 31 :cold_face: ')
print(f'{text:=^30}')

viagem = float(input('Qual a distância da Sua Viagem? '))
if viagem <= 200:
    passagem1 = viagem * 0.50
    print(f'Distância da Sua Viagem: {viagem:.2f} Km\nO Preço da Sua Passagem é de R${passagem1:.2f}')
else:
    passagem2 = viagem * 0.45
    print(f'Distância da Sua Viagem: {viagem:.2f} Km\nO Preço da Sua Passagem é de R${passagem2:.2f}')
