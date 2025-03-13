from emoji import emojize
from time import sleep
text = emojize(' Desafio 29 :cold_face: ')
print(f'{text:=^30}')

vermelho = ('\033[31m')
verde = ('\033[32m')
amarelo = ('\033[33m')

velocidade = float(input(f'{amarelo}Qual a velocidade atual do carro? '))
print('Carregando...')
sleep(1)
if velocidade > 80.0:
    multa = (velocidade - 80) * 7.0
    print(f'{vermelho}Sua Velocidade: {velocidade:.2f} Km/H\nVocê foi multado! Você deve pagar uma multa de R${multa:.2f}!')
else:
    print(f'{verde}Sua Velocidade: {velocidade:.2f} Km/H\nA Velocidade está dentro do limite permitido!')
