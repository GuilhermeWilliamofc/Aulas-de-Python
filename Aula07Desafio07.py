text = 'Desafio 07'
print(f'{text:=^30}')

n1 = float(input('\033[33mDigite a Primeira Nota - '))
n2 = float(input('Digite a Segunda Nota - '))
media = n1+n2
divisao = media/2
print(f'\033[36mA Média das Notas {n1} e {n2} é igual a {divisao}')
