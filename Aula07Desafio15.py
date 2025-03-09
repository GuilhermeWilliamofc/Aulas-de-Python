text = 'Desafio 15'
print(f'{text:=^30}')

dias = int(input('Quantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
alugueldias = dias*60
aluguelkm = km*0.15
alugueltotal = alugueldias+aluguelkm
print(f'O total a pagar é de R${alugueltotal:.2f}')
