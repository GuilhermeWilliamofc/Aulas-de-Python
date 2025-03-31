from emoji import emojize
text = emojize(' Desafio 102 :cold_face: ')
print(f'{text:=^30}')

def fatorial(n, show=False):
    """fatorial - Calcula o fatorial de um número

    Args:
        n (int): O número a ser calculado
        show (bool, optional): Mostrar ou não a conta. False por padrão.

    Returns:
        int: O valor do fatorial de um número n
    """
    f = 1
    for c in range(n, 0, -1):
        f *= c
        if show == True and c != 1:
            print(f'{c} x', end=' ')
        if show == True and c == 1:
            print(f'{c} =', end= ' ')
    return f

print(fatorial(5, show=True))
