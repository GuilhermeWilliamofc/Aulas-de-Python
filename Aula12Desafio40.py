from emoji import emojize
text = emojize(' Desafio 40 :cold_face: ')
print(f'{text:=^30}')

nota1 = float(input('\033[33mDigite a primeira nota: '))
nota2 = float(input('Digite a segunda nota: '))
media = (nota1 + nota2) / 2
if media >= 7.0:
    print(f'\033[32mSua Nota: {media:.1f}\nAprovado')
elif media >= 5.0 and media < 7.0:
    print(f'Sua Nota: {media:.1f}\nRecuperação')
else:
    print(f'\033[31mSua Nota: {media:.1f}\nReprovado')
