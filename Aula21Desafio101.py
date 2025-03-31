from emoji import emojize
text = emojize(' Desafio 101 (lá ele) :cold_face: ')
print(f'{text:=^30}')

def votacao():
    from datetime import date
    idade = date.today().year - ano
    if idade < 16:
        msg = '\033[31mNão vota'
    if idade >= 18 and idade < 65:
        msg = '\033[32mVoto Obrigatório'
    if idade > 65 or idade == 17 or idade == 16:
        msg = '\033[33mVoto Opcional'
    print(f'Com {idade} anos: {msg}')


ano = int(input('\033[33mEm que ano você nasceu? '))
# posso colocar esse input na função
votacao()
