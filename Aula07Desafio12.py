text = 'Desafio 12'
print(f'{text:=^30}')

preco = float(input('\033[33mDigite seu preço - R$'))
desconto = 0.05
novopreco1 = preco*desconto
novopreco2 = preco-novopreco1
print(f'\033[36mO valor de R${preco:.2f} com 5% de desconto passa a valer R${novopreco2:.2f}')
