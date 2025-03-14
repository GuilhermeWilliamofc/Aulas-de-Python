from emoji import emojize
text = emojize(' Desafio 36 :cold_face: ')
print(f'{text:=^30}')

casa = int(input('\033[33mDigite o Valor da Casa: '))
salario = int(input('Digite seu salário: '))
anos = int(input('Digite em quantos anos vai pagar: '))
salariototal = salario * (anos * 12)
meses = anos * 12
prestacao = casa / meses
if prestacao > salariototal * 0.30 + salariototal:
    print('\033[31mSeu empréstimo foi negado, Você não pode financiar essa casa')
else:
    print('\033[32mSeu empréstimo foi aprovado, Você pode financiar esta casa')
