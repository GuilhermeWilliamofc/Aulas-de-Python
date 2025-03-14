from emoji import emojize
text = emojize(' Desafio 42 :cold_face: ')
print(f'{text:=^30}')

lado1 = float(input('Digite o valor do primeiro lado: '))
lado2 = float(input('Digite o valor do segundo lado: '))
lado3 = float(input('Digite o valor do terceiro lado: '))
pitagoras = lado1 + lado2 > lado3 and lado1 + lado3 > lado2 and lado3 + lado2 > lado1
if pitagoras:
    print('\033[32mCom esses comprimentos dá para formar um triângulo')
else:
    print('\033[31mCom esses comprimentos não dá para formar um triângulo')
if lado1 == lado2 == lado3 and pitagoras:
    print('Formaria um triângulo equilátero')
elif lado1 == lado2 != lado3 and pitagoras or lado1 == lado3 != lado2 and pitagoras or lado2 == lado3 != lado1 and pitagoras:
    print('Formaria um triângulo isósceles')
elif lado1 != lado2 != lado3 and pitagoras:
    print('Formaria um triângulo escaleno')
