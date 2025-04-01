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

