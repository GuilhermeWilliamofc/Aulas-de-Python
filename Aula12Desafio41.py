from emoji import emojize
from datetime import date
text = emojize(' Desafio 41 :cold_face: ')
print(f'{text:=^30}')

ano = int(input('Digite seu ano de nascimento: '))
idade = date.today().year - ano
if idade <= 9:
    print(f'Sua Idade: {idade}\nSua Categoria: Mirim')
elif idade <= 14 and idade > 9:
    print(f'Sua Idade: {idade}\nSua Categoria: Infantil')
elif idade <= 19 and idade > 14:
    print(f'Sua Idade: {idade}\nSua Categoria: Júnior')
elif idade == 20:
    print(f'Sua Idade: {idade}\nSua Categoria: Sênior')
else:
    print(f'Sua Idade: {idade}\nSua Categoria: Master')
