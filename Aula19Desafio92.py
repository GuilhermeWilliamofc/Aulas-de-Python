from emoji import emojize
from datetime import date
text = emojize(' Desafio 92 :cold_face: ')
print(f'{text:=^30}')

dados = {}
resposta = ' '

dados['nome'] = input('Digite o nome: ').title()
ano = int(input('Ano de Nascimento: '))
dados['idade'] = date.today().year - ano
while resposta not in 'sn':
    resposta = input('Tem Carteira de Trabalho? [S/N]: ').lower().strip()[0]
if resposta == 's':
    dados['clt'] = int(input('Carteira de Trabalho: '))
    dados['ano_contratacao'] = int(input('Ano de Contratação: '))
    dados['salario'] = float(input('Salário: R$'))

if resposta == 's':
    termino = ((dados['ano_contratacao'] + 35) - date.today().year) + dados['idade']

print(f'O Nome é {dados["nome"]}')
print(f'Tem {dados["idade"]} Anos de Idade')

if resposta == 's':
    print(f'A CTPS é {dados["clt"]}')
    print(f'O Ano de Contratação foi em {dados["ano_contratacao"]}')
    print(f'O Salário é de R${dados["salario"]:.2f}')
    if termino < dados['idade']:
        print(f'Já se aposentou com {termino} anos')
    else:
        print(f'Vai se aposentar com {termino} anos')
