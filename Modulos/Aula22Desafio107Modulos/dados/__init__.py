from ..titulo import cabecalho

def leia_dinheiro(texto):
    n = ' '
    while not n.isnumeric() == True:
        n = input(texto).strip().replace(',', '.')
        if n.isnumeric() == True or n.isalpha() == False and '.' in n:
            n = float(n)
            break
        if n.isalpha() == True or n.isnumeric() == False:
            print(f'\033[31mErro: \"{n}\" é um preço inválido!\033[m')
            # \" não necessário aqui mas só para me lembrar de que dessa forma posso conseguir digitar aspas no print/input
    return n


def leiaint(texto):
    while True:
        try:
            n = int(input(texto))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número\033[m')
            n = 0
            break
        except:
            print('\033[31mErro: Por favor, digite um número inteiro válido\033[m')
        else:
            break
    return n


def leiafloat(texto):
    while True:
        try:
            n = float(input(texto))
        except KeyboardInterrupt:
            print('\033[31mO usuário preferiu não digitar esse número\033[m')
            n = 0
            break
        except:
            print('\033[31mErro: Por favor, digite um número real válido\033[m')
        else:
            break
    return n


def menuantigo(m1 = 'nada', m1_t = 20, op1 = 'nada', op2 = 'nada'):
    """Faz a estrutura de um menu

    Args:
        m1 (str, optional): Titulo do Menu. Defaults to 'nada'.
        m1_t (int, optional): Tamanho desejado das linhas. Defaults to 20.
        op1 (str, optional): primeira opção. Defaults to 'nada'.
        op2 (str, optional): segunda opção. Defaults to 'nada'.
    """
    cont = 0
    if m1 != 'nada':
        titulo = m1
        tamanho = len(m1) + m1_t
        print('-' * tamanho)
        print(titulo.center(tamanho))
        print('-' * tamanho)
    if op1 != 'nada':
        cont += 1
        opcao1 = 0
        opcao1 += cont
        print(f'\033[33m[ {cont} ] \033[m- \033[36m{op1}\033[m')
    if op2 != 'nada':
        cont += 1
        opcao2 = 0
        opcao2 += cont
        print(f'\033[33m[ {cont} ] \033[m- \033[36m{op2}\033[m')
    
    if m1 != 'nada':
        cont += 1
        sair = 0
        sair += cont
        print(f'\033[33m[ {cont} ] \033[m- \033[36mSair do Sistema\033[m')

    if op1 != 'nada':
        print('-' * tamanho)
        opcao = input('\033[32mSua Opção: \033[m')
        
    return opcao

    
def leiastring(texto):
    while True:
        try:
            n = input(texto).title().strip()
        except (KeyboardInterrupt):
            print('\033[31mO usuário decidiu não digitar o dado\033[m')
            return '<desconhecido>'
        if n.isnumeric() == True:
            print('\033[31mErro: Por favor digite um nome válido\033[m')
        if n.isnumeric() == False:
            break
    return n


def menu(m1 = 'nada', m1_t = 20, opcoes = None):
    """Faz a estrutura de um menu

    Args:
        m1 (str, optional): Titulo do Menu. Defaults to 'nada'.
        m1_t (int, optional): Tamanho desejado das linhas. Defaults to 20.
        opcoes (list, optional): Opções do menu. Defaults to [].
    """

    if opcoes is None:
        opcoes = []

    cont = 0
    if m1 != 'nada':
        titulo = m1
        tamanho = len(m1) + m1_t
        print('-' * tamanho)
        print(titulo.center(tamanho))
        print('-' * tamanho)

    for item in opcoes:
        cont += 1
        print(f'\033[33m[ {cont} ] \033[m- \033[36m{item}\033[m')

    if m1 != 'nada':
        cont += 1
        sair = 0
        sair += cont
        print(f'\033[33m[ {cont} ] \033[m- \033[36mSair do Sistema\033[m')

    if len(opcoes) != 0:
        print('-' * tamanho)
        opcao = input('\033[32mSua Opção: \033[m')
        
    return opcao

def arquivoExiste(nome):
    try:
        a = open(nome, 'rt')
        a.close()
    except FileNotFoundError:
        return False
    else:
        return True
    

def criarArquivo(nome):
    try:
        a = open(nome, 'wt+')
        a.close()
    except:
        print('\033[31mHouve um erro na criação do arquivo!\033[m')
    else:
        print(f'\033[32mArquivo {nome} criado com sucesso!\033[m')


def lerArquivo(nome = '', texto = '', dado1 = '', dado2 = ''):
    try:
        a = open(nome, 'rt')
    except:
        print('\033[31mErro ao ler o arquivo!\033[m')
    else:
        cabecalho(texto, 35)
        print(dado1.ljust(30), end= '')
        print(dado2.rjust(9))
        for linha in a:
            dado = linha.split(';')
            dado[1] = dado[1].replace('\n', '')
            print(f'{dado[0]:<30} {dado[1]:>3} ano(s)')
    finally:
        a.close()


def cadastrar(arq, nome = '<desconhecido>', idade = 0):
    try:
        a = open(arq, 'at')
    except:
        print('\033[31mHouve um erro na abertura do arquivo!\033[m')
    else:
        try:
            a.write(f'{nome};{idade}\n')
        except:
            print('\033[31mHouve um erro na hora de escrever os dados!\033[m')
            a.close()
