from emoji import emojize
text = emojize(' Desafio 57 :cold_face: ')
print(f'{text:=^30}')

sexo = ''
while sexo != 'm' and sexo != 'f':
    sexo = input('\033[33mDigite seu sexo (M/F): ').strip().lower()[0]
    if sexo not in ['m', 'f']:
        print('\033[31mSexo Inválido! Digite Novamente')
if sexo == 'm':
    print('\033[36mSeu Sexo é: Masculino')
elif sexo == 'f':
    print('\033[35mSeu Sexo é: Feminino')
