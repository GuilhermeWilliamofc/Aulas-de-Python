def somar(a=0, b=0, c=0):
    """
    Faz a soma de 3 valores e aparece na tela
    """
    s = a + b + c
    print(f'A Soma é igual a {s}')

somar(3, 6, 9)
somar(2, 4)
somar(1)
help(somar)