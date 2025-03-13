text = 'Desafio 15'
print(f'{text:=^30}')

dias = int(input('\033[33mQuantos dias alugados? '))
km = float(input('Quantos Km rodados? '))
alugueldias = dias*60
aluguelkm = km*0.15
alugueltotal = alugueldias+aluguelkm
print(f'\033[32mO total a pagar é de R${alugueltotal:.2f}')
