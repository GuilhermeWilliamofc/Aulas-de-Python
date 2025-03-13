text = 'Desafio 05'
print(f'{text:=^30}')

n1 = int(input('\033[33mDigite um número: '))
ant = n1-1
suc = n1+1
print(f'\033[36mNúmero - {n1} \nAntecessor - {ant}\nSucessor - {suc}')
