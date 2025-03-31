from emoji import emojize
text = emojize(' Desafio 105 :cold_face: ')
print(f'{text:=^30}')

def notas(* num, sit=False):
    """Função para analisar notas e situações de vários alunos.

    Args:
        num (int): uma ou mais notas dos alunos (aceita várias)
        sit (bool, optional): Indica se deve adicionar ou não a situação. Falso por padrão.

    Returns:
        ficha (dict): dicionário com várias informações sobre a situação da turma
    """

    media = sum(num) / len(num)
    ficha = {}
    ficha['total'] = len(num)
    ficha['maior'] = max(num)
    ficha['menor'] = min(num)
    ficha['média'] = media
    if sit == True:
        if media > 7:
            situacao = 'Boa'
        elif media <= 6 and media >= 5:
            situacao = 'Razoável'
        elif media < 5:
            situacao = 'Ruim'
        ficha['situação'] = situacao
    
    return ficha


resp = notas(5.5, 2.5, 1.5, sit=True)
print(resp)
