from emoji import emojize
text = emojize(' Desafio 36 :cold_face: ')
print(f'{text:=^30}')

casa = float(input('\033[33mDigite o Valor da Casa: '))
salario = float(input('Digite seu salário: '))
anos = int(input('Digite em quantos anos vai pagar: '))
prestacao = casa / (anos * 12)
minimo = salario * 0.30
if prestacao > minimo:
    print(f'\033[31mSeu empréstimo foi negado, Você não pode financiar essa casa\nValor da casa: R${casa:.2f}\nAnos: {anos}\nValor da Prestação: R${prestacao:.2f}')
else:
    print(f'\033[32mSeu empréstimo foi aprovado, Você pode financiar esta casa\nValor da casa: R${casa:.2f}\nAnos: {anos}\nValor da Prestação: R${prestacao:.2f}')
