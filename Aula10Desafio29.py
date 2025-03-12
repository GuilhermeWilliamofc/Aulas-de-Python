from emoji import emojize
text = emojize(' Desafio 29 :cold_face: ')
print(f'{text:=^30}')

velocidade = float(input('Qual a velocidade atual do carro? '))
if velocidade > 80.0:
    multa = (velocidade - 80) * 7.0
    print(f'Sua Velocidade: {velocidade:.2f} Km/H\nVocê foi multado! Você deve pagar uma multa de R${multa:.2f}!')
else:
    print(f'Sua Velocidade: {velocidade:.2f} Km/H\nA Velocidade está dentro do limite permitido!')
