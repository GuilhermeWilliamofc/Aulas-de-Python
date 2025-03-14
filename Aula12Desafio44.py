from emoji import emojize
text = emojize(' Desafio 44 :cold_face: ')
print(f'{text:=^30}')

valor = float(input('Digite o valor do produto: '))
opcao = int(input('Escolha uma opção de pagamento:\n[ 1 ] para à vista no dinheiro/cheque\n[ 2 ] para à vista no cartão\n[ 3 ] para 2x no cartão\n[ 4 ] para 3x ou mais no cartão\nQual é a opção? '))
if opcao == 1:
    conta1 = valor - valor * 0.10
    print('Sua Opção: À Vista no Dinheiro/Cheque')
    print(f'Sua compra de R${valor:.2f} vai custar R${conta1:.2f} no final')
elif opcao == 2:
    conta2 = valor - valor * 0.05
    print('Sua Opção: À Vista no Cartão')
    print(f'Sua compra de R${valor:.2f} vai custar R${conta2:.2f} no final')
elif opcao == 3:
    print('Sua Opção: 2x no Cartão')
    print(f'Sua compra de R${valor:.2f} vai custar R${valor:.2f} no final')
elif opcao == 4:
    parcelas = float(input('Quantas parcelas? '))
    conta3 = valor * 0.20 + valor
    parcela2 = conta3 / parcelas
    print(f'Sua compra será parcelada em {parcelas:.0f}x de R${parcela2:.2f} COM JUROS')
    print(f'Sua compra de R${valor:.2f} vai custar R${conta3:.2f} no final')
else:
    print('Opção de pagamento inválida!')
