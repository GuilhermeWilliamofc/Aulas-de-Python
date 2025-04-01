def titulo(msg):
    from emoji import emojize
    text = emojize(f' Desafio {msg} :cold_face: ')
    print(f'{text:=^30}')
