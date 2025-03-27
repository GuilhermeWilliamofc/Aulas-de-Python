from emoji import emojize
text = emojize(' Desafio 90 :cold_face: ')
print(f'{text:=^30}')

aluno = {}

aluno['nome'] = input('\033[33mDigite o Nome do Aluno: ')
aluno['média'] = float(input('Digite a Média de Joaquim: '))

print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["média"]}')

if aluno['média'] < 7:
    print('\033[31mA situação é igual a Reprovado')
else:
    print('\033[32mA situação é igual a Aprovado')