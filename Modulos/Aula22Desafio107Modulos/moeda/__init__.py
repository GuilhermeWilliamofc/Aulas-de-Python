def metade(n = 0, show=False):
    conta = n / 2
    if show:
        return formatacaomoeda(conta)
    return conta


def dobro(n = 0, show=False):
    conta = n * 2
    if show:
        return formatacaomoeda(conta)
    return conta


def aumentarporcento(n = 0, p = 0, show=False):
    por = (n * (p / 100)) + n
    if show:
        return formatacaomoeda(por)
    return por


def diminuirporcento(n = 0, p = 0, show=False):
    por = n - (n * (p / 100))
    if show:
        return formatacaomoeda(por)
    return por


def formatacaomoeda(n = 0, cifrao = 'R$'):
    n = f'{cifrao}{n:.2f}'.replace('.', ',')
    return n

def resumo(n = 0, ap = 10, dp = 5, cifrao = 'R$'):

    """Faz o Resumo dos valores em forma de tabela

    Args:
        n (float): Valor desejado
        ap (float): % de Aumento
        dp (float): % de Redução
        cifrao (str, optional): Muda o cifrão da moeda. 'R$' por padrão.
    """

    msg = 'Resumo do Valor'
    dado1 = 'Preço Analisado:'
    dado2 = 'Dobro do Preço:'
    dobro_n = dobro(n)
    dado3 = 'Metade do Preço:'
    metade_n = metade(n)
    dado4 = f'{ap}% de aumento:'
    aumento_n = aumentarporcento(n, ap)
    dado5 = f'{dp}% de redução:'
    reducao_n = diminuirporcento(n, dp)
    print('-' * (len(msg) + 20))
    print(f'{msg:^{len(msg) + 20}}') 
    # dá para usar "preço analisado".center() tbm
    # \t pra tabular com mais facilidade
    print('-' * (len(msg) + 20))
    print(f'{dado1:<5}', end= ' ')
    print(f'{formatacaomoeda(n, cifrao)}')
    print(f'{dado2:<5}', end= ' ')
    print(f'{formatacaomoeda(dobro_n, cifrao)}')
    print(f'{dado3:<5}', end= ' ')
    print(f'{formatacaomoeda(metade_n, cifrao)}')
    print(f'{dado4:<5}', end= ' ')
    print(f'{formatacaomoeda(aumento_n, cifrao)}')
    print(f'{dado5:<5}', end= ' ')
    print(f'{formatacaomoeda(reducao_n, cifrao)}')
    print('-' * (len(msg) + 20))

