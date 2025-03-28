from emoji import emojize
text = emojize(' Desafio 90 :cold_face: ')
print(f'{text:=^30}')

aluno = {}

aluno['nome'] = input('\033[33mDigite o Nome do Aluno: ')
aluno['média'] = float(input(f'Digite a Média de {aluno["nome"]}: '))

print(f'O nome é igual a {aluno["nome"]}')
print(f'A média é igual a {aluno["média"]}')

if aluno['média'] >= 7:
    print('\033[32mA situação é igual a Aprovado')
elif aluno['média'] < 7 and aluno['média'] >= 5:
    print('\033[33mA sitação é igual a Recuperação')
else:
    print('\033[31mA situação é igual a Reprovado')
