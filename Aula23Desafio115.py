from Modulos.Aula22Desafio107Modulos.titulo import titulo
from Modulos.Aula22Desafio107Modulos.dados import *
from time import sleep

titulo(115)

arq = 'desafio115.txt'

if arquivoExiste(arq):
    print('\033[32mArquivo Encontrado Com Sucesso!\033[m')
else:
    print('\033[31mArquivo Não Encontrado!\033[m')
    criarArquivo(arq)

while True:
    try:
        opcao = int(menu('Menu Principal', 40, ['Ver Pessoas Cadastradas', 'Cadastrar uma nova Pessoa']))
    except (ValueError, KeyboardInterrupt):
        print(f'\033[31mErro: Por favor, digite um número inteiro válido\033[m')
    else:
        if opcao == 1:
            lerArquivo(arq, 'Pessoas Cadastradas', 'Nomes:', 'Idades:')

        if opcao == 2:
            cabecalho('Novo Cadastro', 41)
            nome = leiastring('Nome: ')
            idade = leiaint('Idade: ')
            cadastrar(arq, nome, idade)
            print(f'Novo registro de {nome} adicionado')

        if opcao == 3:
            break

        if opcao > 3 or opcao < 1:
            print(f'\033[31mErro: Por favor, digite uma opção válida\033[m')
        
        sleep(1)

cabecalho('\033[33m      Volte Sempre!\033[m', 28)
sleep(1)
