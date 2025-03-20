from emoji import emojize
text = emojize(' Desafio 72 :cold_face: ')
print(f'{text:=^30}')

extenso = ('zero','um','dois','três','quatro','cinco','seis','sete','oito','nove','dez','onze','doze','treze','catorze','quinze','dezesseis','dezessete','dezoito','dezenove','vinte')
num = ' '
while num not in range(0, 21):
    num = int(input('\033[33mDigite um número entre 0 e 20: '))
    if num not in range(0, 21):
        print('\033[31mNúmero Inválido Tente Novamente...')

print(f'\033[32mVocê digitou o número {extenso[num]}')
