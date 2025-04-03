def titulo(msg):
    from emoji import emojize
    text = emojize(f' Desafio {msg} :cold_face: ')
    print(f'{text:=^30}')


def cabecalho(msg = '', tamanho = 20):
    if msg != '':
        linha = len(msg) + tamanho
        print('-' * linha)
        print(msg.center(linha))
        print('-' * linha)

        