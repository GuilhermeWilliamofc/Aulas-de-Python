def teste():
    x = 8
    print(f'Na função teste, n vale {n}')
    print(f'Na função teste, x vale {x}')
    # a variável x só funciona dentro do def pois foi declarada aqui
    # "x" é uma variável local e "n" é uma variável global


# programa principal
n = 2
print(f'No programa principal, n vale {n}')
teste()
