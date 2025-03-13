from emoji import emojize
text = emojize(' Desafio 31 :cold_face: ')
print(f'{text:=^30}')

ciano = ('\033[36m')
amarelo = ('\033[33m')
roxo = ('\033[35m')

viagem = float(input(f'{ciano}Qual a distância da Sua Viagem? '))
if viagem <= 200:
    passagem1 = viagem * 0.50
    print(f'{roxo}Distância da Sua Viagem: {viagem:.2f} Km\n{amarelo}O Preço da Sua Passagem é de R${passagem1:.2f}')
else:
    passagem2 = viagem * 0.45
    print(f'{roxo}Distância da Sua Viagem: {viagem:.2f} Km\n{amarelo}O Preço da Sua Passagem é de R${passagem2:.2f}')
