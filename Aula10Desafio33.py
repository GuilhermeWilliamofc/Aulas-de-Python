from emoji import emojize
text = emojize(' Desafio 33 :cold_face: ')
print(f'{text:=^30}')

num1 = int(input('Digite o Primeiro Número: '))
num2 = int(input('Digite o Segundo Número: '))
num3 = int(input('Digite o Terceiro Número: '))

if num1 == num1>num2 and num1>num3:
    print(f'{num1} é o maior número')
else:
    pass
if num1 == num1<num2 and num1<num3:
    print(f'{num1} é o menor número')
else:
    pass

if num2 == num2>num1 and num2>num3:
    print(f'{num2} é o maior número')
else:
    pass
if num2 == num2<num1 and num2<num3:
    print(f'{num2} é o menor número')
else:
    pass

if num3 == num3>num1 and num3>num2:
    print(f'{num3} é o maior número')
else:
    pass
if num3 == num3<num1 and num3<num2:
    print(f'{num3} é o menor número')
else:
    pass
