from emoji import emojize
text = emojize(' Desafio 77 :cold_face: ')
print(f'{text:=^30}')

palavras = ('aprender', 'programar','linguagem','python','curso','grátis','estudar','praticar','trabalhar','mercado','programador','futuro')

for i in palavras:
    print(f'\nNa palavra {i.title()} temos: ', end = '')
    for letra in i:
        if letra.lower() in 'aáeiou':
            print(letra, end = ' ')
